import pandas as pd

def incremental_search(xi, delta_x, niter, tol, tolerance_type, function):
    table = []
    row = {}
    Error = "Relative Error" if tolerance_type == "Significant Figures" else "Absolute Error"

    # initial call
    row["xi"] = xi
    row["f(xi)"] = function(xi)
    row[Error] = None
    table.append(row)
    iter = 0
    err = 100

    while (iter < niter and err > tol):
        old_xi= xi
        xi = xi + delta_x
        iter += 1

        row = {}
        row["xi"] = xi
        row["f(xi)"] = function(xi)
        row["f(xi - delta_x)"] = function(xi - delta_x)

        if Error == "Relative Error":
            row[Error] = abs((xi- old_xi)/xi)
        else:
            row[Error] = abs(xi - old_xi)
        table.append(row)

        err = row[Error]

    df = pd.DataFrame(table)
    return {"status":"success", "table":df}
