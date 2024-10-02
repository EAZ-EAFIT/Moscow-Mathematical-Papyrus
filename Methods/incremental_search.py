import pandas as pd

def generate_table(x0, niter, method, function):
    table = []
    row = {}

    # initial call
    args = {"x0": x0, "funtion": function, "niter": 1}
    initial = method(args)
    row["iter"] = 0
    row["xn"] = x0
    row["f(n)"] = function(initial["result"])
    row["abs_err"] = 0
    row["rel_err"] = 0
    table.append(row)

    iter = 1
    while (iter < niter) {
        res = method(args)
        row["iter"] = iter
        row["xn"] = res["result"]
        row["f(n)"] = function(res["result"])
        row["abs_err"] = abs(row["xn"] - table[iter-1]["xn"])
        args = res[args]
    }
    table.append(row)

    df = pd.DataFrame(table)
    print(df)



def inc_search(x0, delta_x, niter, function):
    xi = x0
    iter = 0
    while (iter < niter and function(xi)*function(xi+delta_x) > 0):
        print("paramos", function(xi)*function(xi+delta_x), iter)
        xi = xi + delta_x
        iter += 1
    return (xi, xi + delta_x)

function = lambda x: x**2 - 4
x0 = 0
delta_x = 0.01
niter = 300
print(inc_search(x0, delta_x, niter, function))
