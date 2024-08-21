
def bisection(a, b, niter, function):
    if (function(a)*function(b) > 0):
        print("No hay raiz en este intervalo")
        return None
    else:
        mid = (a + b)/2
        iter = 0
        while (iter < niter):
            print("Iteracion: ", iter, mid)
            if (function(a)*function(mid) < 0):
                b = mid
            else:
                a = mid
            iter += 1
            mid = (a + b)/2
        return (a, b)

function = lambda x: x**2 - 4
a = 0
b = 3

niter = 300
print(bisection(a, b, niter, function))