import sympy as sp

def linear_spline_interpolation(x, y, decimals=None, x_sym=sp.symbols('x')):
    n = len(x)
    intervals = []
    splines = []
    
    for i in range(n - 1):
        # Calculate the slope (m) and intercept (b) for each segment
        slope = (y[i+1] - y[i]) / (x[i+1] - x[i])
        intercept = y[i] - slope * x[i]
        
        # Create the linear polynomial: y = m*x + b
        linear_segment = slope * x_sym + intercept
        
        if decimals is not None:
            # Optionally round the coefficients
            linear_segment = sp.simplify(sp.nsimplify(linear_segment, tolerance=10**(-decimals)))
        
        intervals.append(f"[{x[i]}, {x[i+1]}]")
        splines.append(linear_segment)
    
    return intervals, splines