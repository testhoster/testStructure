# 🧠 Quantum KMeans Clustering on Iris Dataset

This project demonstrates both **Classical KMeans** and **Quantum-inspired KMeans (QKMeans)** clustering on the famous Iris dataset using Principal Component Analysis (PCA) for visualization. It uses the swap test from quantum computing to estimate similarity between vectors.

## 📌 Features

- Classical KMeans using scikit-learn
- Quantum KMeans using PennyLane and the swap test
- Dimensionality reduction with PCA
- Clean, modular code (each task in a separate file)
- Automatically saves clustering visualizations (`.png` format)


## 📁 Project Structure

```markdown
quantum_kmeans_project/
├── main.py                # Main script to run everything
├── classical_kmeans.py    # Classical KMeans logic
├── quantum_kmeans.py      # Quantum KMeans clustering logic
├── quantum_utils.py       # Quantum circuits (swap test, normalization)
├── data_utils.py          # Load data and apply PCA
├── plot_utils.py          # Save plots for classical and quantum clusters
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```


## 🛠️ Installation \& Setup

### 1. Clone the Repository

```bash
git clone https://github.com/testhoster/testStructure.git
cd testStructure/QuantumML

```


### 2. Create \& Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
```


### 3. Install Required Packages

```bash
pip install -r requirements.txt
```


## 🚀 How to Run

Make sure you're in the project root directory, then run:

```bash
python main.py
```

This will:

- Run classical KMeans
- Run quantum KMeans
- Save both clustering results as:
    - `classical_kmeans.png`
    - `quantum_kmeans.png`


## 📊 Sample Output

**Classical KMeans**
Output saved as `classical_kmeans.png`

**Quantum KMeans**
Output saved as `quantum_kmeans.png`

## 🧪 How Quantum KMeans Works

- Uses PennyLane for quantum simulation
- Employs the **swap test** to compute similarity between quantum-encoded vectors
- Centroid updates are performed classically
- The result is a **hybrid classical-quantum KMeans** implementation


# 👨‍💻 Author

Rithvik Koruturu
🌐 [Portfolio](https://rithvikkoruturu.netlify.app/)
🔗 [GitHub](https://github.com/Rithvik-Koruturu)[^1]
💼 [LinkedIn](https://www.linkedin.com/in/rithvikkoruturu/)[^2]



[^1]: https://github.com/Rithvik-Koruturu

[^2]: https://www.linkedin.com/in/rithvikkoruturu/

## 📚 References

- PennyLane Documentation
- Iris Dataset - UCI ML Repository


## 📌 Future Work Ideas

- Quantum KMeans with higher-dimensional embeddings
- Real quantum hardware backends via Qiskit or Amazon Braket
- QAOA-optimized or variational quantum clustering
