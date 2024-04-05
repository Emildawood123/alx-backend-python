#!/usr/bin/env python3
"""first test practice"""
from parameterized import parameterized
from unittest.mock import patch
import unittest
import client


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient"""
    @parameterized.expand(
        [
            ("google", {"org": "google"}),
            ("abc", {"org": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, url, res, get_mock):
        """test_org"""
        initailize = client.GithubOrgClient(url)
        get_mock.return_value = res
        self.assertEqual(res, initailize.org)
        get_mock.assert_called_once()
