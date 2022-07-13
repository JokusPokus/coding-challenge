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
    """Fold a sequence into a single value.

    Iteratively apply the given (binary) function to combine each of the
    sequence's elements with the aggregate of all previous elements. Start
    with the initial value and the first element of the sequence.

    Args:
        sequence:
          The sequence to fold. May be empty.
        function:
          A function to iteratively aggregate sequence elements.
        initial_value:
          The initial value used for the first function call.
        right (optional): If True, the sequence is folded from right to left.
          Defaults to False.

    Returns:
        The folded value. If the sequence is empty, this will be the
          initial value.
    """
    if right:
        sequence = reversed(sequence)

    cumulator = initial_value

    for item in sequence:
        cumulator = function(cumulator, item)

    return cumulator
