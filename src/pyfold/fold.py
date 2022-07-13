"""
Folding of sequences to single values.
"""
from typing import Callable, Sequence, TypeVar


T = TypeVar('T')


def fold(
        sequence: Sequence[T],
        function: Callable[[T, T], T],
        initial_value: T,
        right: bool = False
) -> T:
    if right:
        sequence = reversed(sequence)

    cumulator = initial_value

    for item in sequence:
        cumulator = function(cumulator, item)

    return cumulator
