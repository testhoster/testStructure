from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

def load_iris_data():
    iris = load_iris()
    return iris.data, iris.target

def apply_pca(data, n_components=2):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)
