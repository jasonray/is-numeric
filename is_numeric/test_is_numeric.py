import pytest
from is_numeric import is_numeric


class TestIsNumeric():

    def test_is_numeric(self):
        assert is_numeric(1)

    @pytest.mark.parametrize("test_input,expected_result", [(1, True), (1.1, True), ("1", True), ("1.1", True), ("x", False)])
    def test_run_test(self, test_input, expected_result):
        print('test_run_test')
        assert is_numeric(test_input) == expected_result
