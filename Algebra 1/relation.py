from typing import Set, Tuple


def is_relation(a: Set, b: Set, r: Set[Tuple]) -> bool:
    """a and b are given sets (Python set, not lset),
    r is a set of tuples (x,y).
    Determine whether r is a relation"""
    assert isinstance(a, set)
    assert isinstance(b, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return all(x in a and y in b
               for (x, y) in r)


def is_reflexive(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is reflexive"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return all((x, x) in r for x in a)


def is_irreflexive(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is irreflexive"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return all((x, x) not in r for x in a)


def is_symmetric(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is symmetric"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return all((y, x) in r for (x, y) in r)


def is_asymmetric(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is asymmetric"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return all((y, x) not in r for (x, y) in r)


def is_antisymmetric(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is antisymmetric"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return all(x == y
               for (x, y) in r
               if (y, x) in r)


def is_transitive(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is transitive"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return all((x, z) in r
               for (x, y) in r
               for z in a
               if (y, z) in r)


def is_equivalence(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is an equivalence relation"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return is_relation(a, a, r) \
        and is_reflexive(a, r) \
        and is_symmetric(a, r) \
        and is_transitive(a, r)


def is_partial_order(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is a partial-order rleation"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return is_relation(a, a, r) \
        and is_reflexive(a, r) \
        and is_antisymmetric(a, r) \
        and is_transitive(a, r)


def is_strict_partial_order(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is strict partial-order relation"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return is_relation(a, a, r) \
        and is_irreflexive(a, r) \
        and is_asymmetric(a, r) \
        and is_transitive(a, r)


def is_connected_relation(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is a connected relation."""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return is_relation(a, a, r) \
        and all(x == y or (x, y) in r or (y, x) in r
                for x in a
                for y in a)


def is_strongly_connected_relation(a: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is a strongly connected relation"""
    assert isinstance(a, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return is_relation(a, a, r) \
        and all((x, y) in r or (y, x) in r
                for x in a
                for y in a)


def is_function_relation(a: Set, b: Set, r: Set[Tuple]) -> bool:
    """a is a given set (Python set, not lset),
    r is a set of tuples (x,y) for which x is in a and y is in a.
    Determine whether the relation is function relation"""
    assert isinstance(a, set)
    assert isinstance(b, set)
    assert isinstance(r, set)
    # CHALLENGE: student must complete the implementation.

    return is_relation(a, b, r) \
        and all(any((x, y) in r
                    for y in b)
                for x in a) \
        and all(b1 == b2
                for (a1, b1) in r
                for (a2, b2) in r
                if a1 == a2)
