import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	n = X.shape[0]
	for i in range(0, n, batch_size):
		batch = [
			X[i:i+batch_size]
		] if y is None else [
			X[i:i+batch_size],
			y[i:i+batch_size]
		]
		yield batch