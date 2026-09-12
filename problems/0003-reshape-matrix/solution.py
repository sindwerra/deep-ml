import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	flatten_list = [entry for row in a for entry in row]
	result, current = [], []
	i = 0
	if new_shape[0] * new_shape[1] != len(flatten_list):
		return []
	while i < len(flatten_list):
		if i % new_shape[1] == 0 and i != 0:
			result.append(current[:])
			current = [flatten_list[i]]
		else:
			current.append(flatten_list[i])
		i += 1
	result.append(current)
	return result