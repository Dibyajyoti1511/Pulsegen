from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering

model = SentenceTransformer("all-MiniLM-L6-v2")

def canonicalize_topics(raw_topics):
    embeddings = model.encode(raw_topics)

    clustering = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=1.0,
        metric="cosine",
        linkage="average"
    )

    labels = clustering.fit_predict(embeddings)

    clusters = {}
    for topic, label in zip(raw_topics, labels):
        clusters.setdefault(label, []).append(topic)

    canonical_map = {}
    for cluster in clusters.values():
        canonical_topic = sorted(cluster, key=len)[0]
        canonical_map[canonical_topic] = list(set(cluster))

    return canonical_map
