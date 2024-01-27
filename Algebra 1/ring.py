from typing import TypeVar, List, Callable
from algebra.monoid import *
from algebra.group import *
from algebra.trace import *

T = TypeVar('T')


def isDistributive(q: List[T],
                   add: Callable[[T, T], T],
                   mult: Callable[[T, T], T]):
    """Detect whether the distributive properties hold on right and left.
    a * (b+c) = a*b + a*c
    (b+c) * a = b*a + c*a
    """
    # CHALLENGE: student must complete the implementation.

    return all(mult(a, add(b, c)) == add(mult(a, b), mult(a, c)) and
               mult(add(b, c), a) == add(mult(b, a), mult(c, a))
               for a in q
               for b in q
               for c in q)


def isRing(q: List[T],
           add: Callable[[T, T], T],
           mult: Callable[[T, T], T],
           zero: T,
           one: T) -> bool:
    """Detect whether the given elements, q, form a ring under the given
        addition and multiplication operations.
        can be called with zero=findIdentity(q, add)
        and one=findIdentity(q, mult)
        """
    # CHALLENGE: student must complete the implementation.

    return zero is not None and \
        one is not None and \
        isGroup(q, add, zero) and \
        isAbelian(q, add) and \
        isMonoid(q, mult, one) and \
        isDistributive(q, add, mult)
