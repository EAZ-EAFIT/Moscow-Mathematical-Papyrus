def fixed_point_iteration(g, x0, tol, max_iter):
    iter_count = 0
    x_current = x0
    results = []

    while iter_count < max_iter:
        x_next = g(x_current)
        error = abs(x_next - x_current)
        results.append((iter_count, x_current, x_next, error))

        if error < tol:
            return x_next, results

        x_current = x_next
        iter_count += 1

    return None, results  # Si no converge
