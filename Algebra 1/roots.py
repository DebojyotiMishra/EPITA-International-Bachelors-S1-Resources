from typing import List, Callable, Set

from algebra.polynomial import *
from algebra.limit import *


def poly_by_roots(rs: List[float]) -> List[float]:
    """Given a list of roots, generate the polynomial and return its coefficients."""
    # CHALLENGE: student must complete the implementation.

    terms = [[-r, 1] for r in rs]
    return polys_mult(terms)


def search_root(g: Callable[[float], float], left: float, right: float, epsilon: float) -> float:
    """Assuming the function, g, crosses the x-axis, find one such x value.

    If g(right) and g(left) are both positive, or both negative, then
    a recursive call is made with the new left-d and right+d,
    with d chosen so as to double the search interval.
    For this reason, search_root should never be called on a function
    which is always positive, or always negative because it will loop forever.
    """

    # CHALLENGE: student must complete the implementation.
    gl = g(left)
    if gl == 0:
        return left
    gr = g(right)
    if gr == 0:
        return right
    if gl * gr > 0:
        d = abs(right - left) / 2
        return search_root(g, left - d, right + d, epsilon)
    else:
        return find_x_intercept(g, left, right, epsilon)


def roots_quadratic(coefs: List[float], epsilon=0.00001) -> List[float]:  # TODO write unit test
    """Return a list of 2 roots (perhaps equal) if the polynomial has real roots,
    else return [] if the polynomial has no real roots."""
    from math import sqrt
    assert len(coefs) == 3
    c, b, a = coefs
    # CHALLENGE: student must complete the implementation.

    discr = b * b - 4 * a * c
    if discr >= 0 - epsilon:
        return sorted([(-b + sqrt(max(0, discr))) / (2 * a),
                       (-b - sqrt(max(0, discr))) / (2 * a)])
    else:
        return []


# def xyzzy():
#     import random
#     return max(((d, u, v, w, x, y, z)
#                    for r in range(1000000)
#                    for u in [random.randrange(-100,100)]
#                    for v in [random.randrange(-100, 100)]
#                    if v != 0
#                    for a in [u/v]
#                    for w in [random.randrange(-100, 100)]
#                    for x in [random.randrange(-100, 100)]
#                    if x != 0
#                    for b in [w/x]
#                    for y in [random.randrange(-100, 100)]
#
#                    for z in [random.randrange(-100, 100)]
#                    if z != 0
#                    for c in [y/z]
#                    for d in [b*b - 4 * a * c]
#                    if d < 0
#                ), key=lambda x: x[0])
#
# print(xyzzy())

def find_root_by_inflection_points(coefs: List[float], epsilon: float) -> List[float]:  # TODO write unit test
    """Given a polynomial specified by coefficients, return an iterable of roots.
    The method used is to find the roots of the derivative.  These roots
    identify inflection points.  We look at the inflection points in order
    of increasing x value, and find two consecutive for which the value of
    the original polynomial changes sign.  If such is found, then there is
    a root between the two x values, and it can be found using a binary
    search, for which the function search_root can be used.
    """

    # CHALLENGE: student must complete the implementation.

    f = poly_to_function(coefs)

    inflections = sorted(list(poly_roots(poly_derivative(coefs), epsilon / 10)))

    # find all adjacent inflection points where the function changes sign;
    #   binary search here for a root. Return a generator which generates
    #   these roots.  If the inflection points happen to be roots, they are
    #   returned also by this generator.
    def gen_roots():
        for k in range(len(inflections) - 1):
            fleft = f(inflections[k])
            if fleft == 0:
                yield inflections[k]
            fright = f(inflections[k + 1])
            if fright == 0:
                yield inflections[k + 1]
            if fleft * fright < 0:  # values have opposite signs
                yield search_root(f, inflections[k], inflections[k + 1], epsilon)
        if f(inflections[-1]) == 0:
            yield inflections[-1]

    return [x for x in gen_roots()]


def poly_roots(coefs: List[float], epsilon: float) -> List[float]:
    """Return a list (in increasing order) of roots of the given polynomial."""

    from algebra.division import divide_out_roots, divide_out_root
    assert (len(coefs) > 0)
    # CHALLENGE: student must complete the implementation.
    if all(x == 0 for x in coefs):
        raise Exception(f"cannot find roots of polynomial {coefs}")

    if len(coefs) == 1:
        return []

    if len(coefs) == 2:
        b, a = coefs
        return [-b / a]

    if coefs[0] == 0:
        # optimization:
        # if zero is a root, then just factor it out.
        # zero is a root iff the leading coefficient is zero
        return sorted([0] + poly_roots(coefs[1:], epsilon))

    # apply rational-roots-test.
    #   if all coefs are integers,
    #   let u = coefs[-1]
    #   let v = coefs[0]
    #  if there is a rational root of the form a/b (a,b integers)
    #  then a|u and b|v,
    #  so find all factors of coefs[-1] and all factors of coefs[0]
    #  then iterate two consecutive loops, and try +/- each
    #  to identify one or more roots.

    if all(isinstance(c, int) for c in coefs):
        from math import sqrt, ceil

        def factors(n: int) -> Set[int]:
            return {m for m in range(2, ceil(sqrt(abs(n))) + 1)
                    if n % m == 0}.union({1, abs(n)})

        # TODO, fixme, this algorithm fails to identify rational roots with multiplicity.
        rational_roots = {r for b in factors(coefs[-1])  # x^n term
                          for a in factors(coefs[0])  # x^0 term
                          for s in [-1, 1]
                          for r in [s * a if b == 1 else s*a/b]
                          if abs(poly_eval(coefs, r)) < epsilon}
        if rational_roots:
            for r in rational_roots:
                coefs, _ = divide_out_root(r, coefs)
            return sorted(list(rational_roots) + poly_roots(coefs, epsilon))

    def signum(x):
        if x == 0:
            return 0
        if x > 0:
            return 1
        return -1

    if len(coefs) % 2 == 0 and \
            len(coefs) > 2 and \
            all(coefs[x] == 0 for x in range(1, len(coefs) - 1)):  # odd degree
        root = -signum(coefs[0] * coefs[-1]) * abs(coefs[0] / coefs[-1]) ** (1 / (len(coefs) - 1))
        p1, _ = divide_out_root(root, coefs)
        return sorted([root] + poly_roots(p1, epsilon))

    if len(coefs) % 2 != 0 and \
            len(coefs) > 2 and \
            coefs[0] * coefs[-1] < 0 and \
            all(coefs[x] == 0 for x in range(1, len(coefs) - 1)):  # even degree
        root = abs(coefs[0] / coefs[-1]) ** (1 / (len(coefs) - 1))
        p1, _ = divide_out_root(root, coefs)
        p2, _ = divide_out_root(-root, p1)
        return sorted([root, -root] + poly_roots(p2, epsilon))

    if len(coefs) == 3:
        return roots_quadratic(coefs, epsilon)

    if len(coefs) % 2 == 0:  # even length, i.e. odd degree
        f = poly_to_function(coefs)
        r = search_root(f, -1.0, 1.0, epsilon)
        p2, remainder = divide_out_root(r, coefs)
        return sorted(poly_roots(p2, epsilon) + [r])

    # even degree
    rs = find_root_by_inflection_points(coefs, epsilon)
    if not rs:
        return []

    p2, remainder = divide_out_roots(rs, coefs)
    return sorted(poly_roots(p2, epsilon) + rs)
