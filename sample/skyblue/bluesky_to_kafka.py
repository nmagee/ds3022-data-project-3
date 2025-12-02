import websockets
import json
import os
import asyncio
from datetime import datetime
from quixstreams import Application

KAFKA_BROKER = os.getenv(
    "KAFKA_BROKER",
    "127.0.0.1:19092"
)

BLUESKY_URL = "wss://jetstream2.us-west.bsky.network/subscribe?wantedCollections=app.bsky.feed.post"

async def listen_to_bluesky():
    #Creating Kafka application inside async function
    MAX_MESSAGES = 100000

    app = Application(
        broker_address=KAFKA_BROKER, #Where the broker is 
        producer_extra_config={
            "broker.address.family": "v4", #Force IPv4
            "batch.size": 100000
        }
    )
    #Everything that I produce will land on bluesky-events as JSON
    topic = app.topic(
        name = "bluesky-events",
        value_serializer="json"
    ) 
    #Create a shared kafka producer I reuse for all messages
    producer = app.get_producer()
    message_count = 0 #To count how many messages I produce 
    start_time = datetime.now() 
    
    try:
        #Reconnect Loop
        while message_count < MAX_MESSAGES: #Runs until 100k
            try:
                print(f"[producer] Connecting to {BLUESKY_URL} ...")
                async with websockets.connect(
                    BLUESKY_URL,
                    ping_interval=20, #Send a Ping 20 seconds
                    ping_timeout=60, #If you don't get a ping within 60 seconds
                    close_timeout=10 #Time allowed for a clean closed
                ) as ws:
                    print(f"[producer] connected to Bluesky Jetstreams")

                    async for message in ws: #Listens for each incoming message from Jetstream.
                        #1 Parse JSON
                        try:
                            data = json.loads(message)
                        except json.JSONDecodeError as e:
                            print(f"[producer] JSON decode error: {e}")
                            continue

                        #2 Filter only commit events for posts
                        if data.get("kind") != "commit":
                            continue

                        commit = data.get("commit") or {}
                        if commit.get("collection") != "app.bsky.feed.post": #Avoid NoneType errors
                            continue

                        #3 Use rev as key (for partitioning)
                        rev = commit.get("rev")
                        if rev is None:
                            print("[producer] Missing 'rev' in commit, skipping")
                            continue

                        #4 Produce to Kafka with try/except
                        try:
                            serialized = topic.serialize(key = rev, value = data) #Serializing the key as bytes
                            producer.produce(#Actually sending messages to kafka topic
                                topic = topic.name,
                                key = serialized.key,
                                value = serialized.value,
                            )
                            message_count += 1

                            #Print rate every 100 messages
                            if message_count % 100 == 0:
                                elapsed = (datetime.now() - start_time).total_seconds()
                                if elapsed > 0:
                                    rate = message_count / elapsed
                                    print(
                                        f"[producer] Rate: {rate:.2f} msg/sec"
                                        f"(total: {message_count})"
                                    )
                            
                            if message_count >= MAX_MESSAGES:
                                print(
                                    f"[producer] Reached {MAX_MESSAGES} messages." "Stopping stream and flushing producer... "
                                )
                                break

                        except Exception as e:
                            print(f"[producer] Error producing to Kafka: {e}")

                    if message_count >= MAX_MESSAGES:
                        break

            except websockets.ConnectionClosed as e:
                if message_count >= MAX_MESSAGES:
                    break
                print(f"[producer] Websocket Closed: {e}. Reconnecting in 5 seconds ...")
                await asyncio.sleep(5)
            except Exception as e:
                if message_count >= MAX_MESSAGES:
                    break
                print(f"[producer] Connection Error: {e}. Reconnecting in 5 seconds ..." )
                await asyncio.sleep(5)
    finally:
        #Ensure we flush any buffered message before exiting 
        #"Send everything in the buffer right now"
        print("[producer] Flushing producer before exit ... ")
        try:
            producer.flush()
        except Exception as e:
            print(f"[producer] Error during final flush: {e}")
        print(f"[producer] Done. Total messages produced: {message_count}")

if __name__ == "__main__":
    try:
        asyncio.run(listen_to_bluesky())
    except KeyboardInterrupt:
        print("\n[producer] Stopping stream due to Keyboard Interrupt ... ")
