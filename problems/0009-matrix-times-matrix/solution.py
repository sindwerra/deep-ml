def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    n, d = len(a), len(a[0])
    if len(b) != d:
        return -1
    d, m = len(b), len(b[0])
    result = [ [0] * m for _ in range(n)]
    for i in range(n):
        for j in range(d):
            for k in range(m):
                result[i][k] += a[i][j] * b[j][k]
    return result