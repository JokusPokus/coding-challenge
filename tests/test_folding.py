"""
Unit tests for pyfold package.
"""
import pytest

from pyfold import fold


NON_EMPTY_SEQUENCES = [
    pytest.param([1], 1, 2, id='single_int'),
    pytest.param([1, 2, 3], 1, 7, id='multiple_ints'),
    pytest.param(['b', 'c', 'd'], 'a', 'abcd', id='multiple_strings'),
    pytest.param([[1, 2], [3, 4]], [], [1, 2, 3, 4], id='multiple_lists'),
    pytest.param(('b', 'c', 'd'), 'a', 'abcd', id='tuple_sequence'),
    pytest.param(range(4), 0, 6, id='lazy_range_sequence'),
]

OPERATORS = [
    pytest.param(lambda x, y: x + y, 17, id='add'),
    pytest.param(lambda x, y: x * y, 144, id='multiply'),
    pytest.param(lambda x, y: max(x, y), 6, id='max'),
    pytest.param(lambda x, y: x % y, 0, id='modulo'),
]


class TestFolding:
    @pytest.mark.parametrize(
        'seq, initial_val, expected',
        NON_EMPTY_SEQUENCES
    )
    def test_left_folding_of_non_empty_sequence(
            self,
            seq,
            initial_val,
            expected
    ):
        actual = fold(seq, lambda x, y: x + y, initial_val)
        assert actual == expected

    def test_right_folding_of_non_empty_sequence(self):
        actual = fold(['y', 'e'], lambda x, y: x + y, 'h', right=True)
        assert actual == 'hey'

    @pytest.mark.parametrize('seq, initial_val, expected', NON_EMPTY_SEQUENCES)
    def test_folding_of_empty_sequence_returns_initial_value(
            self, seq, initial_val, expected
    ):
        actual_left = fold([], lambda x, y: x + y, initial_val)
        actual_right = fold([], lambda x, y: x + y, initial_val, right=True)
        assert actual_left == actual_right == initial_val

    @pytest.mark.parametrize('function, expected', OPERATORS)
    def test_folding_with_different_functions(self, function, expected):
        actual = fold([1, 2, 6, 4, 3], function, 1)
        assert actual == expected
