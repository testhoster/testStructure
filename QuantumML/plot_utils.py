import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_classical_clusters(X_pca, labels, centroids, filename="classical_kmeans.png"):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette="viridis", s=70)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', label='Centroids', marker='X')
    plt.title("Classical KMeans Clustering")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"[✔] Saved classical clustering plot to '{filename}'")

def plot_quantum_clusters(clusters, centroids, filename="quantum_kmeans.png"):
    colors = ['r', 'g', 'b']
    plt.figure(figsize=(8, 6))
    for i, cluster_points in clusters.items():
        cluster_points = np.array(cluster_points)
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=colors[i], label=f"Cluster {i}")
        plt.scatter(centroids[i][0], centroids[i][1], color='black', marker='X', s=200)
    plt.title("Quantum KMeans Clustering")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"[✔] Saved quantum clustering plot to '{filename}'")
