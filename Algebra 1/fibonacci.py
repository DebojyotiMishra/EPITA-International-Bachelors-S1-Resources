from typing import TypeVar, Callable, List
from algebra.recursion import power

T = TypeVar('T')


def fibonacci(n: int) -> int:
    """Compute the nth (one-based) digit of the fibonacci sequence:
    1, 1, 2, 3, 5, 8, ..."""
    assert n >= 1
    # CHALLENGE: student must complete the implementation.

    if n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 1


def fibonacci_as_matrix(n: int) -> int:
    """Compute the (n-1), n, and (n+1) Fibonacci numbers by raising the matrix
    (1 1
     1 0) to the nth power.  Then the matrix is of the form
     (F(n+1) F(n)
      F(n)   F(n-1)).
    The function, power, is used to raise a matrix to a power.
    Then return the upper-right or lower-left matrix entry.
    """
    # CHALLENGE: student must complete the implementation.

    ident = ((1, 0), (0, 1))

    def mult(x, y):
        ((a, b),
         (c, d)) = x
        ((e, f),
         (g, h)) = y
        return ((a * e + b * g, a * f + b * h),
                (c * e + d * g, c * f + d * h))

    return power(((1, 1), (1, 0)),
                 n,
                 mult,
                 ident)[1][0]
