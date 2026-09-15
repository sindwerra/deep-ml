import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	m = len(x)
	result = []
	base = np.array(f(x))
	for j in range(m):
		temp_x = x[::]
		temp_x[j] += h
		diff = (np.array(f(temp_x)) - base) / h
		result.append(diff)

	return np.array(result).T

