import pandas as pd

def secant(x0, x1, niter, tol, function):
    table = []
    
    # Initial setup
    xn = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
    x_prev = x1
    x_prev2 = x0
    err = 100
    iter = 0

    # First iteration (iteration 0)
    row = {
        "Iteración": 0,
        "x_{n-1}": x0,
        "x_n": x1,
        "f(x_n)": function(x1),
        "Error Relativo (%)": None
    }
    table.append(row)

    # Secant method iterations
    while iter < niter and err >= tol:
        # Update xn
        xn = x_prev - function(x_prev) * (x_prev - x_prev2) / (function(x_prev) - function(x_prev2))
        
        # Calculate relative error
        err = abs((xn - x_prev) / xn)
        
        # Append row for current iteration
        row = {
            "Iteración": iter,
            "x_{n-1}": x_prev,
            "x_n": xn,
            "f(x_n)": function(xn),
            "Error Relativo (%)": err
        }
        table.append(row)

        iter += 1
        x_prev2 = x_prev
        x_prev = xn
        

    # Convert table to DataFrame and return
    df = pd.DataFrame(table)
    return df

# Define the function
def f(x):
    return -2 ** (-x) + x * (-1 + x) - x ** (2/3) - 2

# Parameters
x0 = 0.663
x1 = 0.664
niter = 1000
tol = 5e-6

# Run the secant method
result = secant(x0, x1, niter, tol, f)
print(result)
