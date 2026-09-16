import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    base_res = f(x)
    n = x.shape[0]
    result = []
    for i in range(n):
        epsilon_arry = np.zeros(n)
        epsilon_arry[i] = epsilon
        result.append((f(x + epsilon_arry) - base_res) / epsilon)
    result = np.array(result)
    diff_norm = np.linalg.norm(result - analytical_grad)
    comp_grad = np.linalg.norm(result)
    anal_grad = np.linalg.norm(analytical_grad)
    if comp_grad + anal_grad != 0:
        diff = diff_norm / (comp_grad + anal_grad)
    else:
        diff = 0 
    return (result, diff)

