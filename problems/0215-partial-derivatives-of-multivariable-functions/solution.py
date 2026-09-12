import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	poly2d_drv = lambda x: [
		2 * x[0] * x[1] + x[1] ** 2,
		x[0] ** 2 + 2 * x[0] * x[1]
	]
	exp_sum_drv = lambda x: [
		np.exp(x[0] + x[1]),
		np.exp(x[0] + x[1]),
	]
	prod_sin_drv = lambda x: [
		np.sin(x[1]),
		x[0] * np.cos(x[1])
	]
	poly3d_drv = lambda x: [
		2 * x[0] * x[1],
		x[0] ** 2 + x[2] ** 2,
		2 * x[1] * x[2],
	]
	sqrt_err_drv = lambda x: [
		2 * (x[0] - x[1]),
		-2 * (x[0] - x[1]),
	]
	func_dict = {
		"poly2d": poly2d_drv,
		"exp_sum": exp_sum_drv,
		"product_sin": prod_sin_drv,
		"poly3d": poly3d_drv,
		"squared_error": sqrt_err_drv,
	}
	return func_dict[func_name](point)

