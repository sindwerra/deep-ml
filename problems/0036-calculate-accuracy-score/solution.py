import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	n = y_true.shape[0]
	return (y_true == y_pred).sum() / n