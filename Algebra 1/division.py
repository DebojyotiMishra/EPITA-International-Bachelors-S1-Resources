from typing import TypeVar, List, Tuple

T = TypeVar('T')


# In this file we consider a list of number, either a list of int or list
# of float as a list of coefficients of a polynomial.   coefs[0] is the
# coefficient of x^0, coefs[1] is the coefficient of x^1, ..., coefs[n]
# is the coefficient of x^n.
# Thus, the polynomial 2x^3 - x^2 + 4 is represented as [4, 0, -1, 2].
# Be careful, the order of the coefficients is reversed from the normal way a polynomial is usually written.
# For example, in the list mentioned above [4, 0, -1, 2], the coefficients correspond to the polynomial:
# 2x^3 (coefficient 2 for x^3 term)
# -x^2 (coefficient -1 for x^2 term)
# 0 (no x term, hence coefficient 0 for x^1 term)
# 4 (constant term)
# Thus, the polynomial 2x^3 - x^2 + 4 is represented by the list [4, 0, -1, 2].


def poly_divide(numerator: List[float], denominator: List[float]) -> Tuple[List[float], List[float]]:
    """Divide one polynomial by another producing a quotient and remainder.
    numerator / denominator.
    If the denominator is the zero polynomial, an except is raised."""
    from algebra.polynomial import poly_scale, poly_add
    if all(k == 0 for k in denominator):  # if denominator is the 0 polynomial
        raise Exception(f"polynomial division by zero: {numerator}/{denominator}")
    elif all(k == 0 for k in numerator):  # if numerator is the 0 polynomial
        return [0], [0]
    elif len(numerator) == len(denominator) == 1:  # if constant polynomial / constant polynomial
        return [numerator[0] / denominator[0]], [0]
    # (1 + x + x^2 + x^3)  / (1 + x + 0x^2)
    #  --> (1 + x + x^2 + x^3)  / (1 + x)
    elif denominator[-1] == 0:
        return poly_divide(numerator, denominator[0:-1])
    # (1 + x + x^2 + x^3 + 0x^4)  / (1 + x)
    #  --> (1 + x + x^2 + x^3)  / (1 + x)
    # elif numerator[-1] == 0:
    #     return poly_divide(numerator[0:-1], denominator)
    elif len(numerator) < len(denominator):  # if degree of numerator < degree of denominator
        return [0], numerator
    else:  # len(numerator) >=  len(denominator)
        # CHALLENGE: student must complete the implementation.
        d = len(numerator) - len(denominator)
        s = numerator[-1] / denominator[-1]
        q1 = [0] * d + poly_scale(-s, denominator)
        n2 = poly_add(numerator, q1)
        assert len(numerator) == len(n2)
        n2.pop()  # n2 should end in 0 +/- round-off error, which we can ignore
        q, r = poly_divide(n2, denominator)
        if q == [0]:
            return [0] * d + [s], r
        else:
            return q + [s], r


def divide_out_root(r: float, coefs: List[float]) -> Tuple[List[float], float]:
    """Divide the polynomial by (x-r).
    Return the quotient and remainder as (polynomial, coef)"""

    # CHALLENGE: student must complete the implementation.

    def synthetic(k, carry):
        if k >= 0:
            c2 = coefs[k] + carry
            return synthetic(k - 1, c2 * r) + [c2]
        else:
            return []

    s = synthetic(len(coefs) - 1, 0)
    return s[1:], s[0]


def divide_out_roots(rs: List[float], coefs: List[float]) -> Tuple[List[float], List[float]]:
    """Perform a sequence of divisions, one for each "suspected root" given in rs.
    Each division produces a quotient and remainder.  The remainder is 0 if the suspected
    root is an actual root.
    Return a tuple of the quotient polynomial, and the remainders of each successive
    division, in order.
    """
    # CHALLENGE: student must complete the implementation.

    c2 = coefs
    rems = []
    for r in rs:
        c2, rem = divide_out_root(r, c2)
        rems.append(rem)
    return c2, rems
