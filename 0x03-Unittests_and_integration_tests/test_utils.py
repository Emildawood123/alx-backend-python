#!/usr/bin/env python3
"""first test practice"""
import utils
from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand(
        [
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map for check outputs"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test_access_nested_map_exception"""
        self.assertRaises(expected)
