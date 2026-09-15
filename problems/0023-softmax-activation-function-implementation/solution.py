import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)
    sum_scores = sum([math.exp(score - max_score) for score in scores])
    return [
        math.exp(score - max_score) / sum_scores for score in scores
    ]