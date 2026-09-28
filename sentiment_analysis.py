import os
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# --------------------------------------------------
# 1. Create data folder
# --------------------------------------------------

os.makedirs("data", exist_ok=True)

csv_file = "data/sentiment_data.csv"

# --------------------------------------------------
# 2. Create sample text dataset automatically
# --------------------------------------------------

texts = [
    "I absolutely love this product. It works perfectly!",
    "The service was excellent and the staff were very helpful.",
    "This is an amazing experience. I am very happy.",
    "The product quality is fantastic.",
    "I really enjoyed using this application.",
    "The delivery was fast and everything was perfect.",
    "This is one of the best products I have purchased.",
    "The customer support was very good.",
    "I am satisfied with the overall experience.",
    "The product is useful and easy to use.",

    "I hate this product. It stopped working immediately.",
    "The service was terrible and very disappointing.",
    "This is a horrible experience.",
    "The product quality is very poor.",
    "I am extremely unhappy with this purchase.",
    "The delivery was late and the package was damaged.",
    "This is one of the worst products I have purchased.",
    "The customer support was not helpful at all.",
    "I am disappointed with the overall experience.",
    "The application is difficult to use and frustrating.",

    "The product arrived today.",
    "The service is available during working hours.",
    "I received the product yesterday.",
    "The application has several features.",
    "The package contains the product and user manual.",
    "The store is located near the city center.",
    "The company released a new version.",
    "The delivery took three days.",
    "The product is available in multiple colors.",
    "The meeting is scheduled for tomorrow."
]

df = pd.DataFrame({
    "Text": texts
})

# Save original dataset
df.to_csv(csv_file, index=False)

print("========================================")
print("Sentiment dataset created successfully!")
print("========================================")
print(f"Dataset saved at: {csv_file}")

# --------------------------------------------------
# 3. Sentiment analysis using TextBlob
# --------------------------------------------------

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment


df["Sentiment"] = df["Text"].apply(analyze_sentiment)

# Calculate polarity
df["Polarity"] = df["Text"].apply(
    lambda text: TextBlob(text).sentiment.polarity
)

# --------------------------------------------------
# 4. Display results
# --------------------------------------------------

print("\nFirst 10 Sentiment Results:")
print(df.head(10))

print("\nSentiment Counts:")
print(df["Sentiment"].value_counts())

# --------------------------------------------------
# 5. Save analyzed dataset
# --------------------------------------------------

output_file = "data/sentiment_analysis_results.csv"

df.to_csv(output_file, index=False)

print("\nAnalyzed dataset saved at:")
print(output_file)

# --------------------------------------------------
# 6. Calculate percentages
# --------------------------------------------------

sentiment_percentages = (
    df["Sentiment"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nSentiment Percentages:")
print(sentiment_percentages)

# --------------------------------------------------
# 7. Visualization - Sentiment Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

df["Sentiment"].value_counts().plot(
    kind="bar"
)

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Texts")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# 8. Visualization - Sentiment Pie Chart
# --------------------------------------------------

plt.figure(figsize=(7, 7))

df["Sentiment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sentiment Percentage Distribution")
plt.ylabel("")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# 9. Polarity Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Polarity"],
    bins=10
)

plt.title("Sentiment Polarity Distribution")
plt.xlabel("Polarity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

print("\n========================================")
print("SENTIMENT ANALYSIS COMPLETED SUCCESSFULLY!")
print("========================================")