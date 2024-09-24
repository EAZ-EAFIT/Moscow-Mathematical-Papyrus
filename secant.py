import pandas as pd

def secant(x0, x1, niter, tol, function):
    table = []
    row = {}

    # initial call
    xn = x1 - function(x1)*(x1 - x0)/(function(x1) - function(x0))
    x_prev = x1
    x_prev2 = x0

    row["iter"] = 0
    row["x_n"] = x1
    row["x_n-1"] = x0
    row["f(x_n)"] = function(x1)
    row["abs_err"] = 0
    row["rel_err"] = 0
    table.append(row)

    err = 100
    iter = 0

    while (iter < niter and err > tol):
        iter += 1
        x_prev2 = x_prev
        x_prev = xn
        print(iter, x_prev, x_prev2)
        xn = x_prev - function(x_prev)*(x_prev - x_prev2)/(function(x_prev) - function(x_prev2))

        row = {}
        row["iter"] = iter
        row["x_n"] = xn
        row["x_n-1"] = x_prev
        row["f(x_n)"] = function(x1)
        row["abs_err"] = abs(xn - x_prev)
        row["rel_err"] = abs((xn - x_prev)/xn)
        table.append(row)

        err = row["abs_err"]

    df = pd.DataFrame(table)
    return df

def f(x):
    return x**2 - 4

x0 = 1
x1 = 2
niter = 10
tol = 1e-5

result = secant(x0, x1, niter, tol, f)
print(result)