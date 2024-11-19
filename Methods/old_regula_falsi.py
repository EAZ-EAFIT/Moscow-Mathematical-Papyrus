import pandas as pd

def regula_falsi(args):
    x0 = args["x0"]
    function = args["function"]
    niter = args["niter"]
    a = x0
    b = args["b"]
    if (function(a)*function(b) > 0):
        return None
    else:
        x_intersect = (function(b) * a - function(a) * b) / (function(b) - function(a)) 
        iter = 0
        while (iter < niter):
            if (function(a) == 0):
                args["x0"] = a
                args["b"] = b
                return {"finish":True, "result": a, "x0": a, "b": b, "function": function, "niter": niter, "args": args}
            if (function(a)*function(x_intersect) < 0):
                b = x_intersect
            else:
                a = x_intersect
            iter += 1
            x_intersect = (function(b) * a - function(a) * b) / (function(b) - function(a))

        args["x0"] = a
        args["b"] = b
        return {"finish":False, "result": a, "function": function, "niter": niter, "args": args}
