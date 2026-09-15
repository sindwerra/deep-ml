import torch

def linear_backward(grad_output, x, W):
    # TODO: return (grad_input, grad_W, grad_b) for y = x @ W.T + b
    n, o = grad_output.shape
    grad_b = grad_output.T @ torch.ones(n) # n, o * 
    grad_W = grad_output.T @ x # n, o * 
    grad_input = grad_output @ W # n, o * 
    return grad_input, grad_W, grad_b
 