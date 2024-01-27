from typing import TypeVar, Callable, List

T = TypeVar('T')


def factorial(n: int) -> int:
    """Compute n! assuming n is an integer, and n >= 0"""
    assert isinstance(n, int)
    assert n >= 0
    # CHALLENGE: student must complete the implementation.

    if n > 2:
        return n * factorial(n - 1)
    elif n == 2:
        return 2
    else:
        return 1


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b using
    the Euclidian algorithm"""
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert a > 0
    assert b >= 0
    # CHALLENGE: student must complete the implementation.

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def continued_fraction(x: float, n: int) -> float:
    """Compute the value of the function which maps
    0 -> x
    1 -> 1 / (1 + x)
    2 -> 1 / (1 / (1+x))
    3 -> 1 / (1 / (1 / (1+x)))
    ...
    We may think of this as computing the nth
    element of the following array:
    a[0] = x,
    a[1] = 1/(1 + a[0])
    a[2] = 1/(1 + a[1])
    ...
    a[n] = 1/(1 + a_[n-1])
    """
    assert isinstance(n, int)
    assert n >= 0
    # CHALLENGE: student must complete the implementation.

    if n == 0:
        return x
    else:
        return 1 / (1 + continued_fraction(x, n - 1))


def power(b: T, p: int, mult: Callable[[T, T], T], ident: T) -> T:
    """Compute base, b, raised to integer power p, assuming p >= 0.
    To multiply two values, x and y, call mult(x,y).
    ident is the identity for multiplication, i.e., mult(x,ident)=mult(ident,x)=x.
    ident is only used if p == 0.
    It is guaranteed that mult is not called more than 2*log(p)  (log base 2)"""
    assert isinstance(p, int)
    assert p >= 0
    # CHALLENGE: student must complete the implementation.
    if p == 0:
        return ident
    elif p == 1:
        return b
    elif p % 2 == 0:  # p even
        return power(mult(b, b), p // 2, mult, ident)
    else:  # p odd
        return mult(b, power(b, p - 1, mult, ident))
