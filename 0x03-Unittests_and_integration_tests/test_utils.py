#!/usr/bin/env python3
"""first test practice"""
import utils
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
import functools


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


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),

        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """test_get_json"""
        jsonMock = Mock(return_value=test_payload)
        mock_get.return_value.json = jsonMock
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test Memoize class"""

    def test_memoize(self):
        """Test memoize"""

        class TestClass:

            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_a:
            mock_a.return_value = 10
            instance = TestClass()
            result = instance.a_property
            self.assertEqual(instance.a_property, result)
            mock_a.assert_called_once()
