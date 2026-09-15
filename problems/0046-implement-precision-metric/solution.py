import numpy as np
def precision(y_true, y_pred):
	# Your code here
	pos = y_pred.sum()
	return ((y_true == 1) & (y_true == y_pred)).sum() / pos if pos != 0 else 0