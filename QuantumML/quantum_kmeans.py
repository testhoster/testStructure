import numpy as np
from quantum_utils import quantum_distance

def quantum_kmeans(X, k=3, iterations=5):
    np.random.seed(42)
    initial_idx = np.random.choice(len(X), k, replace=False)
    centroids = X[initial_idx]

    for _ in range(iterations):
        clusters = {i: [] for i in range(k)}
        for point in X:
            distances = [quantum_distance(point, c) for c in centroids]
            cluster_idx = np.argmin(distances)
            clusters[cluster_idx].append(point)

        new_centroids = []
        for i in range(k):
            if clusters[i]:
                new_centroids.append(np.mean(clusters[i], axis=0))
            else:
                new_centroids.append(centroids[i])
        centroids = new_centroids

    return clusters, centroids
