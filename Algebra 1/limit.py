from typing import Callable, List


def limit(f: Callable[[float], float], a: float, epsilon: float, delta: float) -> float:
    """Find (by approximation) the limit as x -> a of f(x).
    Begin looking at f(x-delta) and f(x+delta),
    and continue dividing delta by 2 until successive values
    of f are within epsilon of each other.
    I.e., return a value of f within epsilon distance of
    f(a) if a were continuous at x=a.
    This function NEVER calls f(a) as a might not be
    in the domain of f."""

    # CHALLENGE: student must complete the implementation.

    def approx(delta):
        return (f(a - delta) + f(a + delta)) / 2

    def recur(prev, delta):
        better = approx(delta)
        if abs(prev - better) < epsilon:
            return better
        else:
            return recur(better, delta / 2)

    return recur(approx(delta), delta / 2)


def deriv(f: Callable[[float], float], x: float, epsilon: float, delta: float) -> float:
    """Approximate the derivative of f at x, using the definition
    of the derivative                f(x+h) - f(x)
                      f'(x) = Limit ---------------
                              h->0         h

    epsilon is the value which controls the accuracy.  i.e., the computed
    derivative of the function at x is within epsilon distance of the actual
    derivative at x.

    delta is the initial guess for h.  The deriv function tries successively
    smaller values of h until consecutive values of the quotient are with
    epsilon distance of each other.

    This function is implemented using the limit function.
    The limit function requires a given epsilon and starting delta,
    use the epsilon and delta given to deriv to pass directly along to limit.
    ... limit(..,.., epsilon, delta)
    """

    # CHALLENGE: student must complete the implementation.

    def g(h):
        return (f(x + h) - f(x)) / h

    return limit(g, 0, epsilon, delta)


def poly_derivative(coefs: List[float]) -> List[float]:
    """Given the coefficients of a polynomial, compute (and return)
    the coefficients of its derivative."""
    # CHALLENGE: student must complete the implementation.

    return [coefs[n] * n
            for n in range(1, len(coefs))]


def find_x_intercept(g: Callable[[float], float], left: float, right: float, epsilon: float) -> float:
    """Given a unary function, g, which crosses the x-axis somewhere between left and right,
    find an x-value very close to the x-intercept.  I.e., find a value of x such that g(a) = 0
    for some value between x-epsilon/2 <= a <= x+epsilon/2
    Assume left < right.
    If g(left) and g(right) are both positive or both negative, raise an exception.
    The given function, g, is called once per iteration, except for the
    1st iteration where it is called 2 additional times.
    """
    assert left < right
    g_left = g(left)
    g_right = g(right)
    if g_left * g_right > 0:  # both positive or both negative
        raise Exception(f"function has same sign at {left} and {right}")

    # CHALLENGE: student must complete the implementation.
    def recur(left, right, gl, gr):
        # print(f"{left} & {right} & {gl} & {gr}")
        if abs(right - left) < epsilon:
            return left
        else:
            mid = (right + left) / 2
            g_mid = g(mid)
            if g_mid > 0:
                return recur(left, mid, gl, g_mid)
            else:
                return recur(mid, right, g_mid, gr)

    if g_left > g_right:
        def g2(x):
            return -g(x)

        return find_x_intercept(g2, left, right, epsilon)
    else:
        return recur(left, right, g_left, g_right)


def solve_for_x(g: Callable[[float], float], x, left: float, right: float, epsilon: float) -> float:
    """Given a unary function, g, which crosses the horizontal line y=a, somewhere between left and right,
        find an x-value very close the value g crosses that line.  I.e., find a value of x such that g(a) = 12
        for some value between x-epsilon/2 <= a <= x+epsilon/2
        If the value of g(x) > a at x=left and x=right, or if g(x) < a at x=left and x=right,
        raise an exception.
        """

    # CHALLENGE: student must complete the implementation.
    def g2(x1):
        return g(x1) - x

    return find_x_intercept(g2, left, right, epsilon)
