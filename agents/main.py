from agents.ingestion_agent import fetch_reviews
from agents.topic_mining_agent import extract_topics
from agents.canonical_agent import canonicalize_topics
from agents.trend_agent import build_trend_table

APP_ID = "in.swiggy.android"
START_DATE = "2024-06-01"
TARGET_DATE = "2025-12-24"   # change if needed

print("Fetching reviews...")
reviews = fetch_reviews(APP_ID, START_DATE)

raw_topics = []
topic_date_pairs = []

print("Extracting topics...")
for _, row in reviews.iterrows():
    topics = extract_topics(row["content"])
    for topic in topics:
        raw_topics.append(topic)
        topic_date_pairs.append((topic, row["date"]))

print("Canonicalizing topics...")
canonical_map = canonicalize_topics(raw_topics)

final_pairs = []
for canonical, variants in canonical_map.items():
    for topic, date in topic_date_pairs:
        if topic in variants:
            final_pairs.append((canonical, date))

print("Building T-30 trend table...")
trend_table = build_trend_table(final_pairs, TARGET_DATE)

trend_table.to_csv("outputs/trend_report.csv")
print(" Saved: outputs/trend_report.csv")
