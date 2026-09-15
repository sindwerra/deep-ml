
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	cnt = Counter()
	for label, pred in data:
		if pred == 1 and label == 1:
			cnt["TP"] += 1
		elif pred == 1 and label == 0:
			cnt["FP"] += 1
		elif pred == 0 and label == 0:
			cnt["TN"] += 1
		else:
			cnt["FN"] += 1
	result = [[0, 0], [0, 0]]
	result[0][0] = cnt["TP"]
	result[1][1] = cnt["TN"]
	result[1][0] = cnt["FP"]
	result[0][1] = cnt["FN"]
	return result
		