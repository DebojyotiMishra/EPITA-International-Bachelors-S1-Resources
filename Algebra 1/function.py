from typing import TypeVar, Callable, List

T = TypeVar('T')


def is_injection(f: Callable[[T], T], xs: List[T], ys: List[T]) -> bool:
    """Return a bool indicating whether the function f is an
    injection from domain:xs to range:ys"""
    # CHALLENGE: student must complete the implementation.

    return all(len([x for x in xs
                    if f(x) == y]) < 2
               for y in ys)


def is_surjection(f: Callable[[T], T], xs: List[T], ys: List[T]) -> bool:
    """Return a bool indicating whether the function f is an
        injection from domain:xs to range:ys"""
    # CHALLENGE: student must complete the implementation.

    values = [f(x) for x in xs]
    return all(y in values for y in ys)


def is_bijection(f: Callable[[T], T], xs: List[T], ys: List[T]) -> bool:
    """Return a bool indicating whether the function f is an
        injection from domain:xs to range:ys"""
    # CHALLENGE: student must complete the implementation.

    return is_surjection(f, xs, ys) and is_injection(f, xs, ys)
