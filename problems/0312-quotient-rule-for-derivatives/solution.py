import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    n, m = len(g_coeffs), len(h_coeffs)
    g_coe_derv = [(n - i - 1) * g_coeffs[i] for i in range(n - 1)]
    h_coe_derv = [(m - i - 1) * h_coeffs[i] for i in range(m - 1)]
    g = func(g_coeffs, x)
    h = func(h_coeffs, x)
    g_grad = func(g_coe_derv, x)
    h_grad = func(h_coe_derv, x)
    return g_grad / h - (g * h_grad) / (h ** 2)

def func(coeffs, x):
    n = len(coeffs)
    result = []
    for i in range(n):
        power = n - i - 1
        result.append(coeffs[i] * x ** power)
    return sum(result)


