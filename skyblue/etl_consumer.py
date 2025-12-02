import json
from quixstreams import Application
from confluent_kafka import Consumer

KAFKA_BROKER = "127.0.0.1:19092"
TOPIC_NAME = "bluesky-events"
MAX_RECORDS = 100000

def extract_english(record): #Filtering only english comments
    langs = record.get("langs", [])
    return len(langs) == 1 and langs[0] == "en"

def run_etl():
    conf = {
        "bootstrap.servers": KAFKA_BROKER,
        "group.id": "bluesky-etl-simple-v3",  # NEW consumer group
        "auto.offset.reset": "earliest",
    }
    consumer =  Consumer(conf)
    consumer.subscribe([TOPIC_NAME])

    print(f"[ETL] Starting ETL from topic '{TOPIC_NAME}")
    count = 0

    try:
        with open("cleaned.jsonl", "w", encoding = "utf-8") as outfile: 
            while count < MAX_RECORDS:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"[ETL] Kafka Error: {msg.error()}")
                    continue
                # Deserialize JSON from Kafka message
                try:
                    raw = json.loads(msg.value())
                except Exception as e:
                    print(f"[ETL] JSON decode error: {e}")
                    continue

                if raw.get("kind") != "commit":
                    continue
                commit = raw.get("commit", {})

                if commit.get("collection") != "app.bsky.feed.post":
                    continue
                record = commit.get("record", {})
                
                if count < 3:
                    print("[DEBUG] langs:", record.get("langs"))
                    print("[DEBUG] text snippet:", record.get("text", "")[:80])


                #English only
                if not extract_english(record):
                    continue

                #Extract Text
                text = record.get("text", "") #Removes empty text
                if not text:
                    continue

                text = text.strip()
                if not text:
                    continue

                created = record.get("createdAt") #Timestamp

                clean = {#Cleaned Dataset
                    "text": text,
                    "createdAt": created,
                    "lang": "en"
                }

                outfile.write(json.dumps(clean, ensure_ascii=False) + "\n")
                count += 1

                if count % 1000 == 0:
                    print(f"[ETL] Processed {count} messages")
            print(f"[ETL] Reached {MAX_RECORDS} cleaned messages. Stopping ..")

    finally:
        print("[ETL] Closing consumer")
        consumer.close()

if __name__ == "__main__":
    run_etl()