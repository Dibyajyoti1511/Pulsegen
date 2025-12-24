def extract_topics(text):
    text = text.lower()
    topics = []

    rules = {
        "late": "delivery delay",
        "delay": "delivery delay",
        "rude": "delivery partner rude",
        "impolite": "delivery partner rude",
        "cold": "food temperature issue",
        "stale": "food quality issue",
        "refund": "refund issue",
        "cancel": "order cancellation issue",
        "map": "maps not working properly",
        "location": "maps not working properly",
        "instamart": "instamart availability",
        "bolt": "10 minute bolt delivery",
        "price": "pricing issue",
        "expensive": "pricing issue",
        "support": "customer support issue"
    }

    for keyword, topic in rules.items():
        if keyword in text:
            topics.append(topic)

    # fallback → high recall
    if not topics:
        topics.append("general feedback")

    return list(set(topics))
