import pandas as pd
import math

def regula_falsi(a, b, niter, tol, err_type, function):
    table = []
    row = {}

    # initial call
    row["iter"] = 0
    row["a"] = a
    row["b"] = b
    row["x_intersect"] = (function(b) * a - function(a) * b) / (function(b) - function(a))
    row["f(x_intersect)"] = function((function(b) * a - function(a) * b) / (function(b) - function(a)))
    row["abs_err"] = 0
    row["rel_err"] = 0
    table.append(row)

    err = 100

    if (function(a)*function(b) > 0):
        print("No hay raiz en este intervalo")
        return None
    else:
        x_intersect = (function(b) * a - function(a) * b) / (function(b) - function(a))
        iter = 0
        while (iter < niter and err > tol):
            if (function(a) == 0):
                return table
            if (function(a)*function(x_intersect) < 0):
                b = x_intersect
            else:
                a = x_intersect

            iter += 1
            old_intersect = x_intersect
            x_intersect = (function(b) * a - function(a) * b) / (function(b) - function(a))

            row = {}
            row["iter"] = iter
            row["a"] = a
            row["x_intersect"] = x_intersect
            row["b"] = b
            row["f(x_intersect)"] = function(x_intersect)
            row["abs_err"] = abs(x_intersect - old_intersect)
            row["rel_err"] = abs((x_intersect - old_intersect)/x_intersect)
            table.append(row)

            if (err_type == "abs"):
                err = row["abs_err"]
            else:
                err = row["rel_err"]

        df = pd.DataFrame(table)
        return df

# Example function
def example_function(x):
    return math.exp((-2*x+3))-3
# Parameters
a = 0
b = 2
niter = 100
tol = 5e-4

# Call the regula_falsi function
result = regula_falsi(a, b, niter, tol, "abs", example_function)
print(result)

""" # Print the result
if result is not None and not result.empty:
    last_row = result.iloc[-1]
    print(f"x_intersect: {last_row['x_intersect']}")
else:
    print("No result to display") """
