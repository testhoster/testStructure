from sklearn.cluster import KMeans

def perform_kmeans(X, k=3, seed=42):
    model = KMeans(n_clusters=k, random_state=seed)
    labels = model.fit_predict(X)
    return labels, model.cluster_centers_
