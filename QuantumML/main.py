from data_utils import load_iris_data, apply_pca
from classical_kmeans import perform_kmeans
from quantum_kmeans import quantum_kmeans
from plot_utils import plot_classical_clusters, plot_quantum_clusters

def main():
    # Load and preprocess
    X, y = load_iris_data()
    X_pca = apply_pca(X)

    # Classical KMeans
    k = 3
    classical_labels, classical_centroids = perform_kmeans(X_pca, k)
    plot_classical_clusters(X_pca, classical_labels, classical_centroids)

    # Quantum KMeans
    quantum_clusters, quantum_centroids = quantum_kmeans(X_pca, k)
    plot_quantum_clusters(quantum_clusters, quantum_centroids)

if __name__ == "__main__":
    main()
