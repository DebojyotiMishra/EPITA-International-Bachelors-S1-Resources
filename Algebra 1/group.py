from typing import TypeVar, List, Callable, Optional

from algebra.monoid import *

T = TypeVar('T')


def findInverse(x: T, q: List[T], op: Callable[[T, T], T], e: Optional[T]) -> Optional[T]:
    """Find the inverse of the given x:
    If no such inverse exists, return None.
    Otherwise, return the inverse."""
    # CHALLENGE: student must complete the implementation.

    if e is None:
        e = findIdentity(q, op)
    if e is None:
        return None
    else:
        for y in q:
            if op(y, x) == e:
                return y
        return None


def hasInverses(q: List[T], op: Callable[[T, T], T], e: Optional[T]) -> bool:
    """Detect whether each of the given list of elements has an inverse
    under the given operation."""
    # CHALLENGE: student must complete the implementation.

    if e is None:
        e = findIdentity(q, op)
    return all(findInverse(x, q, op, e) is not None
               for x in q)


def isGroup(q: List[T], op: Callable[[T, T], T], e: Optional[T]) -> bool:
    """Detect whether the given list of elements forms a group under the
    given operation"""
    # CHALLENGE: student must complete the implementation.

    if e is None:
        e = findIdentity(q, op)
    return isMonoid(q, op, e) and hasInverses(q, op, e)
