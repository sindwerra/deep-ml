import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	features = np.array(features, dtype=np.float32)
	labels = np.array(labels, dtype=np.int32)
	weights = np.array(weights, dtype=np.float32)
	h = features @ weights + bias
	prob = 1 / (1 + np.exp(-h))
	return prob.tolist(), float(((prob - labels) ** 2).mean())