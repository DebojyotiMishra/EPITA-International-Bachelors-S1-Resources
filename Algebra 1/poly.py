from typing import TypeVar, List, Callable

T = TypeVar('T')


# In this file we consider a list of number, either a list of int or list
# of float as a list of coefficients of a algebra.   coefs[0] is the
# coefficient of x^0, coefs[1] is the coefficient of x^1, ..., coefs[n]
# is the coefficient of x^n.
# Thus, the algebra 2x^3 - x^2 + 4 is represented as [4, 0, -1, 2].
# Be careful, the order of the coefficients is reversed from the normal way a algebra is usually written.
# For example, in the list mentioned above [4, 0, -1, 2], the coefficients correspond to the algebra:
# 2x^3 (coefficient 2 for x^3 term)
# -x^2 (coefficient -1 for x^2 term)
# 0 (no x term, hence coefficient 0 for x^1 term)
# 4 (constant term)
# Thus, the algebra 2x^3 - x^2 + 4 is represented by the list [4, 0, -1, 2].

def poly_equal(coefs1: List[float], coefs2: List[float]) -> bool:
    """Detect whether two given list of coefficients specify the same
    algebra.  I.e., are the lists the same except for trailing
    zeros?
    """

    if len(coefs1) == len(coefs2):
        return coefs1 == coefs2
    elif len(coefs1) > len(coefs2):
        return poly_equal(coefs2, coefs1)
    else:
        # coefs2 is longer than coefs1
        # so the common part must be equal
        # and the rest must be all zeros
        return all(coefs1[i] == coefs2[i]
                   for i in range(len(coefs1))) and \
            all(coefs2[i] == 0
                for i in range(len(coefs1), len(coefs2)))


def poly_add(coefs1: List[float], coefs2: List[float]) -> List[float]:
    """Given two polynomials in terms of their coefficients, return the
    coefficients of the algebra representing their sum."""
    assert len(coefs1) > 0
    assert len(coefs2) > 0
    # assert all(isinstance(x, float) or isinstance(x, int) for x in coefs1), f"expecting list of numbers: {coefs1}"
    # assert all(isinstance(x, float) or isinstance(x, int) for x in coefs2), f"expecting list of numbers: {coefs2}"

    if len(coefs1) == len(coefs2):
        return [coefs1[k] + coefs2[k]
                for k in range(len(coefs1))]
    elif len(coefs1) < len(coefs2):
        return poly_add(coefs1 + [0] * (len(coefs2) - len(coefs1)),
                        coefs2)
    else:
        return poly_add(coefs2, coefs1)


def polys_add(coefss: List[List[float]]) -> List[float]:
    """Given a list of polynomials (each algebra is a list
        of coefficients) compute the coefficients of the sum (addition)
        of all the polynomials.
        If the list of polynomials is empty [0] is returned."""
    from functools import reduce
    assert isinstance(coefss, list)
    assert all(isinstance(x, list) for x in coefss)

    return reduce(poly_add, coefss, [0])


def poly_scale(s: float, coefs: List[float]) -> List[float]:
    """Given a algebra and a scalar (number), return
    the new polygon equal to the original scaled by the scalar."""

    return [s * c for c in coefs]


def poly_mult(coefs1: List[float], coefs2: List[float]) -> List[float]:
    """Given two polynomials in terms of their coefficients, return the
        coefficients of the algebra representing their product."""
    assert len(coefs1) > 0
    assert len(coefs2) > 0
    # assert all(isinstance(x, float) or isinstance(x, int) for x in coefs1), f"expecting list of numbers: {coefs1}"
    # assert all(isinstance(x, float) or isinstance(x, int) for x in coefs2), f"expecting list of numbers: {coefs2}"

    partials = [[0] * i + poly_scale(coefs1[i], coefs2)
                for i in range(len(coefs1))]
    return polys_add(partials)


def polys_mult(polynomials: List[List[float]]) -> List[float]:
    """Given a list of polynomials (each algebra is a list
    of coefficients) compute the coefficients of the product (multiplication)
    of all the polynomials.   If the list of polynomials is empty [1] is returned."""
    from functools import reduce

    return reduce(poly_mult, polynomials, [1])


def poly_power(coefs: List[float], p: int) -> List[float]:
    """Compute a algebra specified by coefs, raised to integer power p, assuming p >= 0.
    It is guaranteed that poly_mult is not called more than 2*log(p)  (log base 2)"""
    from common.utils import fast_power

    return fast_power(coefs, poly_mult, p, [1])


def poly_eval(coefs: List[float], x: float) -> float:
    """Given the coefficients of a polynomial and a value of x,
    return the value of the algebra evaluated at x."""

    return sum(coefs[n] * x ** n
               for n in range(len(coefs)))


def poly_to_function(coefs: List[float]) -> Callable[[float], float]:
    """Convert a set of algebra coefficients into a function from float to float.
    poly_to_function returns a function, which can be called multiple times
    with a single argument.  That function evaluates the algebra at the given x.
    Example function call taken from handout:
    >>> p = poly_to_function([3, -1, 0, 3])
    >>> p(1)
    5"""

    def f(x):
        return poly_eval(coefs, x)

    return f
