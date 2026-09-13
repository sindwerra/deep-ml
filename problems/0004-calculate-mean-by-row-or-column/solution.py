def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	n, m = len(matrix), len(matrix[0])
	if mode == "row":
		return [sum(row) / m for row in matrix]
	result = []
	for i in range(m):
		val = 0
		for j in range(n):
			val += matrix[j][i]
		result.append(val / n)
	return result