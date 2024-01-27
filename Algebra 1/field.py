from typing import TypeVar, List, Callable, Optional

from algebra.group import *
from algebra.monoid import *
from algebra.ring import *

T = TypeVar('T')


def isField(q: List[T],
            add: Callable[[T, T], T],
            mult: Callable[[T, T], T]) -> bool:
    # CHALLENGE: student must complete the implementation.

    one = findIdentity(q, mult)
    zero = findIdentity(q, add)
    return one is not None and \
        zero is not None and \
        one != zero and \
        isRing(q, add, mult, zero, one) and \
        hasInverses([x for x in q if x != zero], mult, one)
