import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	base = np.log(np.exp(scores).sum())
	return np.log(np.exp(scores)) - base