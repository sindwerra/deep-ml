def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = []
	n, m = len(matrix), len(matrix[0])
	for i in range(n):
		cur = []
		for j in range(m):
			cur.append(matrix[i][j] * scalar)
		result.append(cur[:])
	return result