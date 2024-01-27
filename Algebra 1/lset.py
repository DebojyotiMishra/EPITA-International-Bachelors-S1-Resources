from typing import List


def find_duplicates(s: List) -> List:
    """return a list of duplicate elements from a given list, s.
    The elements are returned in the same order as in the given list.
    E.g., [3,1,1,3, 2,1,2,3, 4] ==> [3,1,2]
    [[1, 2], [3, 4], [1, 2], [5, 6], [3, 4]] ==> [[1,2], [3,4]]"""
    # CHALLENGE: student must complete the implementation.

    dups = []
    for i in range(len(s)):
        if s[i] in s[i + 1:] and s[i] not in dups:
            dups.append(s[i])
    return dups


def is_lset(s: List) -> bool:
    """Is the given s of type list, and are all elements unique, ie no element is repeated?"""
    # CHALLENGE: student must complete the implementation.

    return isinstance(s, list) and (find_duplicates(s) == [])


def lset_subset(s: List, t: List) -> bool:
    """Is s a subset of t, in the sense of lsets?,
    We assume (without checking) that s and t are valid lsets."""
    # CHALLENGE: student must complete the implementation.

    return all(x in t for x in s)


def lset_equal(s: List, t: List) -> bool:
    """Given two lists, are they equal if interpreted as sets?
    I.e., are they lsets and do they contain the same elements
    but maybe in a different order."""
    # CHALLENGE: student must complete the implementation.

    return is_lset(s) and \
        is_lset(t) and \
        len(s) == len(t) and \
        lset_subset(s, t) and \
        lset_subset(t, s)


def lset_intersection(s: List, t: List) -> List:
    """Assuming the given s and t are lsets, compute and return the intersection."""
    # CHALLENGE: student must complete the implementation.

    return [x for x in s if x in t]


def lset_minus(s: List, t: List) -> List:
    """Assuming the given s and t are lsets, compute and return the lset of
    elements in s but not in t"""
    # CHALLENGE: student must complete the implementation.

    return [x for x in s if x not in t]


def lset_union(s: List, t: List) -> List:
    """Assuming the given s and t are lsets, compute and return the union."""
    # CHALLENGE: student must complete the implementation.

    return s + lset_minus(t, s)


def lset_xor(s: List, t: List) -> List:
    """Assuming the given s and t are lsets, compute and return the lset
    of elements which are in exactly 1 of s and t."""
    # CHALLENGE: student must complete the implementation.

    return lset_minus(s, t) + lset_minus(t, s)
