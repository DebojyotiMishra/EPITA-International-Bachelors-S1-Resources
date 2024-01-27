from typing import TypeVar, Callable, List
from algebra.recursion import factorial

T = TypeVar('T')


def prime_factors(n: int) -> List[int]:
    """Returns the list of prime factors of the given integer,
    in increasing order.  If a factor occurs multiple times, it is included
    that many times in the result, so that the product of the factors
    is the given numbers.   The list of factors of 12 is [2, 2, 3].
    Note that the list of prime factors of 1 is [].
    This function should never be called with n=0, as it is impossible to
    return a list of prime numbers whose product is 0."""
    from math import sqrt, ceil
    assert n > 0

    # CHALLENGE: student must complete the implementation.

    def loop(k, m, upper):
        if m == 1:
            return []
        elif k > upper:
            # don't try to find factor larger than sqrt(m)
            return [m]
        elif m % k == 0:
            return [k] + loop(k, m // k, ceil(sqrt(m // k)))
        else:
            return loop(k + 1, m, upper)

    if n == 1:
        return []
    else:
        return loop(2, n, ceil(sqrt(n)))


def factorial_factors(n: int) -> List[int]:
    """Return the list of prime factors of n! in ascending order. [2,2,3,....]
    If a prime number appears more than once as a factor of n!, it should appear
    multiple times in the returned list.
    The product of the values of the list must equal n!.
    However, this function does not compute n! explicitly, and does
    not call the factorial function.
    Note, the list of prime factors of 1! is []
    Also, the list of prime factors of 0! is []
    """

    # CHALLENGE: student must complete the implementation.

    def loop(n):
        if n == 1:
            return []
        else:
            return prime_factors(n) + loop(n - 1)

    if n == 0:
        return []
    else:
        return sorted(loop(n))


def choose_direct(n: int, k: int) -> int:
    """Compute n choose k directly as n! / ( k! * (n-k)!).
    n! is computed by a call to factorial."""
    # CHALLENGE: student must complete the implementation.
    return factorial(n) // (factorial(k) * factorial(n - k))


def choose_pascal(n: int, k: int) -> int:
    """Compute n choose k by Pascal's triangle.
    I.e., compute an entry by adding the two entries
    (left and right) in the line above in Pascals triangle.
    The recursion terminates which a 1 on the boundary is encountered.
    This function has exponential complexity, so it will not work for
    large values of n. You should be able to test the function at least
    up to n=20"""
    assert isinstance(n, int)
    assert isinstance(k, int)
    assert n >= k
    assert n > 0
    assert k >= 0
    # CHALLENGE: student must complete the implementation.

    if k == 0:
        return 1
    elif k == n:
        return 1
    else:
        return choose_pascal(n - 1, k - 1) + choose_pascal(n - 1, k)


def choose_factors(n: int, k: int) -> int:
    """Compute n choose k by computing the prime factors of n!, k! and (n-k)!,
    then removing all the factors of k! and (n-k)! from the factors of n!.
    The un-cancelled factors of n! can then be multiplied together to obtain
    the desired result.
    This function does not make any call to factorial.  Prime factors
    of n! are computed by a call to factorial_factors."""
    assert isinstance(n, int)
    assert isinstance(k, int)
    assert n >= k
    assert n > 0
    assert k >= 0
    # CHALLENGE: student must complete the implementation.
    from math import prod
    num_factors = factorial_factors(n)
    den_factors = sorted(factorial_factors(k) + factorial_factors(n - k))

    acc = 1
    while den_factors:
        if den_factors[-1] == num_factors[-1]:
            den_factors.pop()
            num_factors.pop()
        else:
            acc *= num_factors.pop()

    return prod(num_factors) * acc


def choose_linear(n: int, k: int) -> int:
    """Compute the number of combinations of n things taken k at a time.
    We assume that n and k are both integers, and that n > 0, k >= 0,
    and n >= k.
    The method used is to multiply n-1 choose k-1 by n//k.
    Careful of the cases which must terminate the recursion.
    """
    assert isinstance(n, int)
    assert isinstance(k, int)
    assert n >= k
    assert n > 0
    assert k >= 0
    # CHALLENGE: student must complete the implementation.

    if k == 0:
        return 1
    elif k == 1:
        return n
    elif n - k < k:
        return choose_linear(n, n - k)
    else:
        return choose_linear(n - 1, k - 1) * n // k
