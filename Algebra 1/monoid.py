from typing import TypeVar, List, Callable, Optional
from algebra.trace import *

T = TypeVar('T')


def isAssociative(q: List[T], op: Callable[[T, T], T]) -> bool:
    """Detect whether the given operation is associative over the
    given list of elements, q."""
    # CHALLENGE: student must complete the implementation.

    return all(op(a, op(b, c)) == op(op(a, b), c)
               for a in q
               for b in q
               for c in q)


def isClosed(q: List[T], op: Callable[[T, T], T]) -> bool:
    """Detect whether the given list of elements, q, is closed under
    the given operation."""
    # CHALLENGE: student must complete the implementation.

    return all(op(x, y) in q
               for x in q
               for y in q)


def findIdentity(q: List[T], op: Callable[[T, T], T]) -> bool:
    """Find the identity element of the given list of elements, q,
    under the given operation.  If no such element exists in the list,
    then return None."""
    # CHALLENGE: student must complete the implementation.

    for x in q:
        if all(op(x, y) == y and op(y, x) == y for y in q):
            return x
    return None


def isMonoid(q: List[T], op: Callable[[T, T], T], e: Optional[T]) -> bool:
    """Detect whether the given list of elements, q, forms a monoid
    under the given operation."""
    # CHALLENGE: student must complete the implementation.

    if e is None:
        e = findIdentity(q, op)
    return (e is not None) and isClosed(q, op) and isAssociative(q, op)


def isAbelian(q: List[T], op: Callable[[T, T], T]) -> bool:
    """Detect whether the given operation, op, is commutative for all
    elements in the given list, q."""
    # CHALLENGE: student must complete the implementation.

    return all(op(a, b) == op(b, a)
               for a in q
               for b in q)
