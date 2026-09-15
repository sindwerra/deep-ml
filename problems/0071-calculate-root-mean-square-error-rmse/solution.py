
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	n = y_true.shape[0]
	rmse_res = np.sqrt(((y_true - y_pred) ** 2).mean())
	return round(rmse_res,3)
