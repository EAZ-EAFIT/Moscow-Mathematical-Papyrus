import pandas as pd

def secant(x0, x1, niter, tol, err_type, function):
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
    row["abs_err"] = 100
    row["rel_err"] = 100
    table.append(row)

    err = 100
    iter = 0

    while (iter < niter and err > tol):
        iter += 1

        row = {}
        row["iter"] = iter
        row["x_n"] = xn
        row["x_n-1"] = x_prev
        row["f(x_n)"] = function(x1)
        row["abs_err"] = abs(xn - x_prev)
        row["rel_err"] = abs((xn - x_prev)/xn)
        table.append(row)

        x_prev2 = x_prev
        x_prev = xn
        print(iter, x_prev, x_prev2)
        xn = x_prev - function(x_prev)*(x_prev - x_prev2)/(function(x_prev) - function(x_prev2))

        if (err_type == "abs"):
            err = row["abs_err"]
        else:
            err = row["rel_err"]

    df = pd.DataFrame(table)
    return df

def f(x):
    return -pow(2, -x) + x*(-1+x)-pow(x, 2/3) - 3

x0 = 0.663
x1 = 0.664
niter = 100
tol = 5e-6 

result = secant(x0, x1, niter, tol, "rel", f)
print(result)