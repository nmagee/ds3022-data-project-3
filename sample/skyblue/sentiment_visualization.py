import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "cleaned_with_sentiment_toxicity.jsonl"

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"[ERROR] Input File '{INPUT_FILE}' not found in {os.getcwd()}")
        sys.exit(1)

    print(f"[INFO] Loading data from {INPUT_FILE} ...")
    df = pd.read_json(INPUT_FILE, lines = True)

    if "sentiment_label" not in df.columns or "sentiment_score" not in df.columns:
        print("[ERROR] Expected columns 'sentiment_label' and 'sentiment_score' not found.")
        print("Make sure you ran the sentiment_analysis script first.")
        sys.exit(1)
    
    print(f"[INFO] Loaded {len(df)} rwos with sentiment columns")

    #Sentiment Label Distribution (Bar Chart)
    print("[INFO] Plotting sentiment label distribution ...")
    plt.figure(figsize = (6,4))
    df["sentiment_label"].value_counts().plot(kind = "bar")
    plt.xlabel("Sentiment label")
    plt.ylabel("Count")
    plt.title("Sentiment Distribution of Bluesky Comments")
    plt.tight_layout()
    sentiment_plot_path = "sentiment_distribution.png"
    plt.savefig(sentiment_plot_path)
    plt.close()
    print(f"[INFO] Saved sentiment distribution plot to {sentiment_plot_path}")

    #Histogram of Probability for Negative Comments
    #We only want the rows that are predicted as negative and their sentiment score
    print("[INFO] Plotting negative comment probability histogram ...")

    #Handle labels with capitalized
    labels_lower = df["sentiment_label"].astype(str).str.lower()

    #Heurisitic: Anything containing neg will be considered negative
    neg_mask = labels_lower.str.contains("neg")

    num_neg = neg_mask.sum()
    if num_neg == 0:
        print("[WARN] No rows detected as negative; skipping negative probability plot.")
    else:
        neg_scores = df.loc[neg_mask, "sentiment_score"]

        plt.figure(figsize=(8,5))
        neg_scores.hist(bins=30)
        plt.xlabel("Model confidence for negative label")
        plt.ylabel("Number of Comments")
        plt.title("Probability distribution for negative comments")
        plt.tight_layout()
        neg_hist_path = "negative_probability_hist.png"
        plt.savefig(neg_hist_path)
        plt.close()
        print(f"[INFO] Saved negative probability histogram to {neg_hist_path}")

        #Print some quick stats
        print("\n[Summary] Negative Comments: ")
        print(f"Count of negative-labeled comments: {num_neg}")
        print(f"Mean Negative Probability: {neg_scores.mean():.3f}")
        print(f"Median Negative Probability: {neg_scores.median():.3f}")
        print(f"% with score >= 0.9: {(neg_scores >= 0.9).mean() * 100:.2f}%")

    print("\n[INFO] Done generating visualizations.")

if __name__ == "__main__":
    main()