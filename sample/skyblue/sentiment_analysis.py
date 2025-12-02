import pandas as pd
import os 
import sys
import torch 
import torch.nn.functional as F
import matplotlib.pyplot as plt
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

INPUT_FILE = "cleaned.jsonl"
OUTPUT_FILE = "cleaned_with_sentiment_toxicity.jsonl"

SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
TOXICITY_MODEL = "unitary/unbiased-toxic-roberta"

BATCH_SIZE = 256

def load_data():
    if not os.path.exists(INPUT_FILE):
        print(f"[ERROR] Input file '{INPUT_FILE}' not found in {os.getcwd()}")
        sys.exit(1)

    print(f"[INFO] Loading data from {INPUT_FILE} ...")
    df = pd.read_json(INPUT_FILE, lines = True)
    if "text" not in df.columns:
        print("[ERROR] 'text' column not found in input file.")
        sys.exit(1)
    
    print(f"[INFO] Loaded {len(df)} rows")
    return df

def run_sentiment(df):
    print(f"[INFO] Loading sentiment model '{SENTIMENT_MODEL}' ... ")
    sentiment_pipe = pipeline(
        task = "sentiment-analysis",
        model = SENTIMENT_MODEL,
        tokenizer = SENTIMENT_MODEL,
        truncation = True,
        padding = True,
        max_length = 128,
    )
    print("[INFO] Sentiment model loaded.")

    texts = df["text"].astype(str).tolist()
    n = len(texts)

    labels = []
    scores = []

    print(f"[INFO] Running sentiment analysis on {n} texts (batch_size={BATCH_SIZE})")
    for start in range(0, n, BATCH_SIZE):
        end = min(start + BATCH_SIZE, n)
        batch = texts[start:end]
        results = sentiment_pipe(batch)

        labels.extend([r["label"] for r in results])
        scores.extend([r["score"] for r in results])

        if (start // BATCH_SIZE) % 50 == 0:
            print(f"[INFO] Sentiment Processed {end}/{n} texts")

    df["sentiment_label"] = labels
    df["sentiment_score"] = scores
    return df 

def main():
    df = load_data()
    df = run_sentiment(df)

    print(f"[INFO] Saving results to {OUTPUT_FILE} ...")
    df.to_json(OUTPUT_FILE, orient = "records", lines = True, force_ascii = False)
    print("[INFO] Done.")

    print("\n[Summary] Sentiment counts:")
    print(df["sentiment_label"].value_counts())
    print("\n[Summary] Sample rows:")
    print(df[["text", "sentiment_label", "sentiment_score"]].head())

if __name__ == "__main__":
    main()