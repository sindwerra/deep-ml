import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    n = X.shape[0]
    for _ in range(n_epochs):
        if method == "batch":
            weights -= learning_rate * (2 * X.T @ (X @ weights - y)) / n
        elif method == "stochastic":
            for i in range(n):
                weights -= learning_rate * (2 * (weights @ X[i] - y[i]) * X[i])
        else:
            for i in range(0, n, batch_size):
                bs = min(batch_size, n - i)
                batch_input = X[i:i + bs]
                batch_label = y[i:i + bs]
                weights -= learning_rate * (2 * batch_input.T @ (batch_input @ weights - batch_label)) / bs
            
    return weights
