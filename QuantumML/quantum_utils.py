import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=3)

def normalize(vec):
    norm = np.linalg.norm(vec)
    return vec / norm if norm != 0 else vec

@qml.qnode(dev)
def swap_test(x, y):
    qml.Hadamard(wires=0)
    qml.MottonenStatePreparation(normalize(x), wires=[1])
    qml.MottonenStatePreparation(normalize(y), wires=[2])
    qml.CSWAP(wires=[0, 1, 2])
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)

def quantum_distance(x, y):
    prob0 = swap_test(x, y)[0]
    return np.sqrt(1 - prob0)
