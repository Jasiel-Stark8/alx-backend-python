#!/usr/bin/env python3
"""unittest module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Class for access_nested_map"""
    @parameterized.expand([
        ({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']),
        ({'x': {'y': {'z': 2}}}, ['x', 'y', 'z'])
    ])
    def test_access_nested_map_valid_input(self, nested_map, path):
        """Test access_nested_map with valid input"""
        self.assertEqual(access_nested_map(nested_map, path))

    @parameterized.expand([
        ({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']),
        ({'x': {'y': {}}}, ['x', 'y', 'z']),
        ({'j': {}}, ['j', 'k'])
    ])
    def test_access_nested_map_invalid_input(self, nested_map, path):
        """Test access_nested_map with invalid input"""
        with self.assertRaises(keyError):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
