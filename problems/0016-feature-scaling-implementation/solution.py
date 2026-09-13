import numpy as np


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	feature_mean = np.mean(data, axis=0)
	feature_std = np.std(data, axis=0)
	standardized_data = (data - feature_mean[None, :]) / feature_std[None, :]
	max_val, min_val = np.max(data, axis=0), np.min(data, axis=0)
	dist = max_val - min_val
	normalized_data = (data - min_val) / dist
	return standardized_data, normalized_data