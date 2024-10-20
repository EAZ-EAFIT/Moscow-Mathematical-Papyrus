import pandas as pd


def bisection(a, b, niter, tol, err_type, function):
    table = []
    row = {}

    # initial call
    row["iter"] = 0
    row["a"] = a
    row["b"] = b
    row["mid"] = (a + b)/2
    row["f(a)"] = function(a)
    row["f(mid)"] = function((a + b)/2)
    row["f(b)"] = function(b)
    row["abs_err"] = 0
    row["rel_err"] = 0
    table.append(row)

    err = 100

    if (function(a)*function(b) > 0):
        print("No hay raiz en este intervalo")
        return None
    else:
        mid = (a + b)/2
        iter = 0
        while (iter < niter and err > tol):
            print("Iteracion: ", iter, mid)
            if (function(a)*function(mid) < 0):
                b = mid
            else:
                a = mid
            iter += 1
            prev_mid = mid
            mid = (a + b)/2

            row = {}
            row["iter"] = iter
            row["a"] = a
            row["b"] = b
            row["mid"] = mid
            row["f(a)"] = function(a)
            row["f(mid)"] = function(mid)
            row["f(b)"] = function(b)
            row["abs_err"] = abs(mid - prev_mid)
            row["rel_err"] = abs((mid - prev_mid)/mid)
            table.append(row)

            if (err_type == "abs"):
                err = row["abs_err"]
            else:
                err = row["rel_err"]

        df = pd.DataFrame(table)
        return df


function = lambda x: x**2 - 2
a = -40
b = 1.3

niter = 300
print(bisection(a, b, niter, 0.5e-4, "abs", function))