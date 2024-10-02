import pandas as pd

def regula_falsi(a, b, niter, tol, function):
    table = []
    row = {}

    # initial call
    row["iter"] = 0
    row["a"] = a
    row["b"] = b
    row["x_intersect"] = (function(b) * a - function(a) * b) / (function(b) - function(a))
    row["f(a)"] = function(a)
    row["f(x_intersect)"] = function((function(b) * a - function(a) * b) / (function(b) - function(a)))
    row["f(b)"] = function(b)
    row["abs_err"] = 0
    row["rel_err"] = 0
    table.append(row)

    if (function(a)*function(b) > 0):
        print("No hay raiz en este intervalo")
        return None
    else:
        x_intersect = (function(b) * a - function(a) * b) / (function(b) - function(a))
        iter = 0
        while (iter < niter and abs(function(x_intersect)) > tol):
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
            row["f(a)"] = function(a)
            row["f(x_intersect)"] = function(x_intersect)
            row["f(b)"] = function(b)
            row["abs_err"] = abs(x_intersect - old_intersect)
            row["rel_err"] = abs((x_intersect - old_intersect)/x_intersect)
            table.append(row)

        df = pd.DataFrame(table)
        return df

# Example function
def example_function(x):
    return x**3 - x - 2

# Parameters
a = 1
b = 2
niter = 100
tol = 1e-6

# Call the regula_falsi function
result = regula_falsi(a, b, niter, tol, example_function)

# Print the result
if result is not None and not result.empty:
    last_row = result.iloc[-1]
    print(f"x_intersect: {last_row['x_intersect']}")
else:
    print("No result to display")
