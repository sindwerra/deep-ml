import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	try:
		t_inv = np.linalg.inv(T)
		s_inv = np.linalg.inv(S)
	except np.linalg.LinAlgError:
		return -1
	
	return t_inv @ A @ S