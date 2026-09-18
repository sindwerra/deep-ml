import numpy as np

def superposition_reconstruct(W, b, X):
    """
    Compute reconstructed features for the toy superposition model.

    Args:
        W: array of shape (n_hidden, n_features)
        b: array of shape (n_features,)
        X: array of shape (batch_size, n_features)

    Returns:
        list of lists of shape (batch_size, n_features) with reconstructed features
    """
    def ReLU(x):
        x[x < 0] = 0
        return x
    W = np.array(W)
    b = np.array(b)
    X = np.array(X)
    return ReLU((W.T @ W @ X.T).T + b)
