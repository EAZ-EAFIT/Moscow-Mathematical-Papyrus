def generate_table(x0, niter, method, function, args):
    table = []
    row = {}

    # initial call
    initial = method(args)
    row["iter"] = 0
    row["xn"] = x0
    row["f(n)"] = function(initial["result"])
    row["abs_err"] = 0
    row["rel_err"] = 0
    table.append(row)
    print(table)

    iter = 1
    while (iter < niter):
        row = {}
        res = method(args)
        row["iter"] = iter
        row["xn"] = res["result"]
        row["f(n)"] = function(res["result"])
        row["abs_err"] = abs(row["xn"] - table[iter-1]["xn"])
        #print(row["xn"], table[iter-1]["xn"])
        args = res["args"]

        if (res["finish"]):
            table.append(row)
            print("helo")
            print(table)

            df = pd.DataFrame(table)
            print(df)
            return 0

        print(row)
        print(table)
        table.append(row)
        print()
        print(table)
        iter += 1

    df = pd.DataFrame(table)
    print(df)