"""
tests.test_utils
~~~~~~~~~~~~~~~~~~~
This module contains tests which validate the utility functions.
"""

import unittest
from unittest import mock
import floyd_warshall.utils as ut
from floyd_warshall.exceptions import InputValidationError


class TestUtils(unittest.TestCase):
    """
    Tests for helper functions
    """

    @staticmethod
    @mock.patch("floyd_warshall.utils.tabulate")
    def test_transform_graph(mock_tabulate):
        """
        Test for the graph transformation with tabulate call patched to isolate
        the functions core logic
        """

        input_graph = [
            [0, 7, 12, 8],
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0],
        ]

        transformed = [
            [0, 7, 12, 8],
            ["Null", 0, 5, 7],
            ["Null", "Null", 0, 2],
            ["Null", "Null", "Null", 0],
        ]

        ut.transform_graph(input_graph)
        mock_tabulate.assert_called_with(transformed)

        input_graph = [
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807],
        ]

        transformed = [
            ["Null", "Null", "Null", "Null"],
            ["Null", "Null", "Null", "Null"],
            ["Null", "Null", "Null", "Null"],
            ["Null", "Null", "Null", "Null"],
        ]

        ut.transform_graph(input_graph)
        mock_tabulate.assert_called_with(transformed)

        input_graph = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

        transformed = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

        ut.transform_graph(input_graph)
        mock_tabulate.assert_called_with(transformed)

    def test_validate_input(self):
        """
        Tests for validating input format of graphs
        """

        test_input = [[0, 2, 3], [0, 2, 3]]
        self.assertRaises(InputValidationError, ut.validate_input, test_input)

        test_input = "[[0, 2, 3], [0, 2, 3]]"
        self.assertRaises(InputValidationError, ut.validate_input, test_input)

        test_input = [[0, 2, 3], [0, 2, 3], [0, 1, "2"]]
        self.assertRaises(InputValidationError, ut.validate_input, test_input)

        test_input = [0, 1, 2, 3, 4]
        self.assertRaises(InputValidationError, ut.validate_input, test_input)

        test_input = [[0, 2, 3], [0, 2, 3], [0, 2, 3]]
        try:
            ut.validate_input(test_input)
        except InputValidationError:
            self.fail("Validation failed unexpectedly")


if __name__ == "__main__":
    unittest.main()
