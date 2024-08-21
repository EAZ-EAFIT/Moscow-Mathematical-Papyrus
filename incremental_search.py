
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
