import pandas as pd



def newton(x0, niter, tol, function, derivative):
    table = []
    row = {}

    # initial call
    xn = x0 - function(x0)/derivative(x0)
    x_prev = x0

    row["iter"] = 0
    row["x_n"] = x0
    row["f(x_n)"] = function(x0)
    row["f'(x_n)"] = derivative(x0)
    row["abs_err"] = 0
    row["rel_err"] = 0
    table.append(row)

    err = 100
    iter = 0

    while (iter < niter and err > tol):
        iter += 1
        x_prev = xn
        xn = xn - function(xn)/derivative(xn)

        row = {}
        row["iter"] = iter
        row["x_n"] = xn
        row["f(x_n)"] = function(xn)
        row["f'(x_n)"] = derivative(xn)
        row["abs_err"] = abs(xn - x_prev)
        row["rel_err"] = abs((xn - x_prev)/xn)
        table.append(row)

        err = row["abs_err"]

    df = pd.DataFrame(table)
    return df

def function(x):
    return x**2 - 2

def derivative(x):
    return 2*x

x0 = 1.0
niter = 10
tol = 1e-6
print(newton(x0, niter, tol, function, derivative))