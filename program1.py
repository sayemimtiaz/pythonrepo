_INVALID_INPUT_TEST_CASES = [
    dict(
        testcase_name="list_of_non_dict",
        test_input=[1, 2],
        expected_error=ValueError,
        expected_error_regexp="Unexpected Arrow type created from input",
        expected_error=RuntimeError,
        expected_error_regexp="Unsupported numpy type")
]
