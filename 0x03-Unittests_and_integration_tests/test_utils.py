#!/usr/bin/env python3
"""unittest module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test Class for access_nested_map"""

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"x": {"y": {"z": 2}}}, ["x", "y", "z"], 2),
        # Add more test cases here
    ])
    def test_access_nested_map_valid(self, nested_map, path, expected):
        """Test access_nested_map with valid input"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "d"]),
        ({"x": {}}, ["x", "y"]),
        # Add more test cases for invalid input here
    ])
    def test_access_nested_map_invalid(self, nested_map, path):
        """Test access_nested_map with invalid input"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

if __name__ == "__main__":
    unittest.main()