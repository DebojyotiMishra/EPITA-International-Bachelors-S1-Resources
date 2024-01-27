from typing import Set, Tuple, List


def find_primes(n: int, m: int) -> List[int]:
    """Return the list of prime numbers, in increasing order.
    The list should start with n or the first prime larger
    than n, and end with the largest prime less than m.  The returned
     list might contain n (if n is prime), but must not contain m.
     You may assume that 1 < n < m"""
    from math import ceil, sqrt
    # CHALLENGE: student must complete the implementation.

    def is_prime(p):
        if p == 1:
            return False
        elif p == 2:
            return True
        else:
            return all(p % a != 0 for a in range(2, ceil(sqrt(p)) + 1))

    return [p for p in range(n, m) if is_prime(p)]


def pythagorean_triples(n: int) -> Set[Tuple[int, int, int]]:
    """Return a set of triples (a,b,c) which 1 <= a <= b < n,
    for which a^2 + b^2 = c^2
    """
    from math import sqrt
    # CHALLENGE: student must complete the implementation.

    def is_sqr(s):
        t = round(sqrt(s))
        return t * t == s

    return {(a, b, round(sqrt(a * a + b * b)))
            for a in range(1, n)
            for b in range(a, n)
            if is_sqr(a * a + b * b)}


def sum_cubes(n: int) -> Set[Tuple[int, int, int]]:
    """Return set list of all (a,b,c) where
    -n <= a <= b <= c < n,
    for which a^3 + b^3 + c^3 == 1.
    Omit all results for which a, b, or c is 0, -1, or 1"""
    # CHALLENGE: student must complete the implementation.

    ignore = [0, 1, -1]
    return {(a, b, c) for a in range(-n, n)
            if a not in ignore
            for b in range(a, n)
            if b not in ignore
            for c in range(b, n)
            if c not in ignore
            if a * a * a + b * b * b + c * c * c == 1}


def linear_diaphantine(a: int, b: int, c: int, n: int) -> Set[Tuple[int, int]]:
    """Return a set of pairs (x,y) such that a*x + b*y == c
    for 0 <= x < n
    and 0 <= y < n"""
    # CHALLENGE: student must complete the implementation.

    return {(x, y)
            for x in range(n)
            for y in range(n)
            if a * x + b * y == c}


def taxi_cab_numbers(n: int) -> Set[Tuple[int, int, int, int, int]]:
    """Compute the set of integers t in the range: 0 < t < n,
    but excluding t=0,
    for each n can be written as the sum of two different pairs
    of cubes.   For example 1729 = 12^3 + 1^3 = 9^3 + 10^3.
    Notice that 3^3 + (-3)^3 = 2^3 + (-2)^3 = 0,
    so don't include this case in the solution.
    The return value should be a set of 5-tuples (s,a,b,c,d)
    where s == a^3 + b^3 == c^3 + d^3.
    Also do not include 5-tuples such as
    (9,1,2,2,1), because (1,2) is really the same pair of
    integers as (2,1).
    The rule to use is the following:
    Only collect (s,a,b,c,d) if -n<=a<b<n, a<c<n, c<d<n, a != 0, b != 0
    """
    # CHALLENGE: student must complete the implementation.

    return {(s1, a, b, c, d)
            for a in range(-n, n)
            if a != 0
            for b in range(a + 1, n)
            if b != 0
            for s1 in [a * a * a + b * b * b]
            if -n <= s1 < n
            if s1 > 0
            for c in range(a + 1, n)
            for d in range(c + 1, n)
            for s2 in [c * c * c + d * d * d]
            if s1 == s2
            if {a, b} != {c, d}
            }
