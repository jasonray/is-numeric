import pytest
from is_numeric import is_numeric, _is_numeric_regex_plus_isnumeric, _is_numeric_using_error, _is_numeric_regex


def run_test(algorithm_f, test_input, expected_result):
    result = _is_numeric_regex(test_input) == expected_result
    print(f'run_test {algorithm_f=} {test_input=} {result=} {expected_result=}')
    assert result == expected_result


class Test_Is_Numeric():

    def test_is_numeric(self):
        assert is_numeric(1)

    def test_is_numeric_sampling(self):
        print(is_numeric(1))
        print(is_numeric(-1))
        print(is_numeric(123))
        print(is_numeric(123.456))
        print(is_numeric("123.456"))
        print(is_numeric("x"))
        print(is_numeric("1x"))

    @pytest.mark.parametrize("test_input,expected_result", [
        (1, True),
        (-1, True),
        (123, True),
        (-123, True),
        (1.1, True),
        (-1.1, True),
        (1234567890, True),
        (123450.6789, True),
        (-1234567890, True),
        (-123450.6789, True),
        ('1', True),
        ('-1', True),
        ('123', True),
        ('-123', True),
        ('1.1', True),
        ('-1.1', True),
        ('1234567890', True),
        ('123450.6789', True),
        ('-1234567890', True),
        ('-123450.6789', True),
    ])
    def test_run_test(self, test_input, expected_result):
        run_test(is_numeric, test_input, expected_result)


class Test_is_numeric_regex():

    @pytest.mark.parametrize("test_input,expected_result", [
        (1, True),
        (-1, True),
        (123, True),
        (-123, True),
        (1.1, True),
        (-1.1, True),
        (1234567890, True),
        (123450.6789, True),
        (-1234567890, True),
        (-123450.6789, True),
        ('1', True),
        ('-1', True),
        ('123', True),
        ('-123', True),
        ('1.1', True),
        ('-1.1', True),
        ('1234567890', True),
        ('123450.6789', True),
        ('-1234567890', True),
        ('-123450.6789', True),
    ])
    def test_run_test(self, test_input, expected_result):
        run_test(_is_numeric_regex, test_input, expected_result)


class Test_is_numeric_regex_plus_isnumeric():

    @pytest.mark.parametrize("test_input,expected_result", [
        (1, True),
        (-1, True),
        (123, True),
        (-123, True),
        (1.1, True),
        (-1.1, True),
        (1234567890, True),
        (123450.6789, True),
        (-1234567890, True),
        (-123450.6789, True),
        ('1', True),
        ('-1', True),
        ('123', True),
        ('-123', True),
        ('1.1', True),
        ('-1.1', True),
        ('1234567890', True),
        ('123450.6789', True),
        ('-1234567890', True),
        ('-123450.6789', True),
    ])
    def test_run_test(self, test_input, expected_result):
        run_test(_is_numeric_regex_plus_isnumeric, test_input, expected_result)


class Test_is_numeric_using_error():

    @pytest.mark.parametrize("test_input,expected_result", [
        (1, True),
        (-1, True),
        (123, True),
        (-123, True),
        (1.1, True),
        (-1.1, True),
        (1234567890, True),
        (123450.6789, True),
        (-1234567890, True),
        (-123450.6789, True),
        ('1', True),
        ('-1', True),
        ('123', True),
        ('-123', True),
        ('1.1', True),
        ('-1.1', True),
        ('1234567890', True),
        ('123450.6789', True),
        ('-1234567890', True),
        ('-123450.6789', True),
    ])
    def test_run_test(self, test_input, expected_result):
        run_test(_is_numeric_using_error, test_input, expected_result)


# class Test_str_isnumeric():
#     @pytest.mark.parametrize("test_input,expected_result", [
#         (1, True),
#         (-1, True),
#         (123, True),
#         (-123, True),
#         (1.1, True),
#         (-1.1, True),
#         (1234567890, True),
#         (123450.6789, True),
#         (-1234567890, True),
#         (-123450.6789, True),
#         ('1', True),
#         ('-1', True),
#         ('123', True),
#         ('-123', True),
#         ('1.1', True),
#         ('-1.1', True),
#         ('1234567890', True),
#         ('123450.6789', True),
#         ('-1234567890', True),
#         ('-123450.6789', True),
#         ])
#     def test_run_test(self, test_input, expected_result):
# run_test (str_isnumeric ,test_input ,expected_result )

# class TestPerfDifferences():
#     def test_perf(self):
# from statman import Statman
#         iterations = 1000000
#         perc_non_numeric_list = [0, .2, .5 , .8]
#         algorithm_list = [('is_numeric', is_numeric),  ('is_numeric_using_error', _is_numeric_using_error) , ('is_numeric_regex', _is_numeric_regex), ('is_numeric_regex_plus_isnumeric', _is_numeric_regex_plus_isnumeric) ]

#         for perc_non_numeric in perc_non_numeric_list:
#             test_inputs = [
#             (1, True),
#             (-1, True),
#             (123, True),
#             (-123, True),
#             (1.1, True),
#             (-1.1, True),
#             (1234567890, True),
#             (123450.6789, True),
#             (-1234567890, True),
#             (-123450.6789, True),
#             ('1', True),
#             ('-1', True),
#             ('123', True),
#             ('-123', True),
#             ('1.1', True),
#             ('-1.1', True),
#             ('1234567890', True),
#             ('123450.6789', True),
#             ('-1234567890', True),
#             ('-123450.6789', True) ]

#             # the test results will change based upon number of non_numeric values
#             num_non_numerics_to_add = int(round( perc_non_numeric * len(test_inputs) / (1-perc_non_numeric) , 0) )
#             for i in range(0, num_non_numerics_to_add):
#                 test_inputs.append( ('xyz', False)  )

#             for algorithm_pair in algorithm_list:
#                 algorithm_name, f  = algorithm_pair
#                 # print(f'running test for {algorithm_name}')
#                 Statman.stopwatch(name=algorithm_name).start()
#                 for i in range(1, iterations+1):
#                     # print(f'running test for {algorithm_name} {i}')
#                     for test_input in test_inputs:
#                         input, expected_result = test_input
#                         assert f(input) == expected_result

#                 Statman.stopwatch(name=algorithm_name).stop()
#                 print(f'Test {algorithm_name=} {perc_non_numeric=} {iterations=} time={Statman.stopwatch(name=algorithm_name).value}')

#         1/0
