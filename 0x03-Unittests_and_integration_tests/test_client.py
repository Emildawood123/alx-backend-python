#!/usr/bin/env python3
"""first test practice"""
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from fixtures import TEST_PAYLOAD
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

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """test_has_license"""
        re_fun = client.GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(expected, re_fun)

    @patch("client.get_json")
    def test_public_repos(self, get_mock_json):
        """test_public_repos method"""
        get_mock_json.return_value = "www.test.com"
        with patch('client.GithubOrgClient._public_repos_url') as mock:
            """patch context"""
            mock.return_value = {"repos": ["r1", "r2", "r3", "...etc"]}
            inp = client.GithubOrgClient("test").repos_payload
            self.assertEqual(inp, get_mock_json.return_value)
            get_mock_json.assert_called_once()


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient
    """

    class setUpClass:
        """
        Set up class for integration test
        """

        @patch("client.get_json")
        def setUp(self, mock_get_json):
            """
            Set up method for class
            """
            self.test_class = GithubOrgClient("test")
            self.org_payload = {"repos_url": "www.test.com"}
            self.repos_payload = [
                {"name": "repo1", "license": {"key": "my_license"}},
                {"name": "repo2", "license": {"key": "other_license"}},
            ]
            mock_get_json.side_effect = [
                self.org_payload,
                self.repos_payload,
            ]


@parameterized_class(

    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """class method set up to init"""
        config = {
            "return_value.json.side_effect": [
                cls.org_payload,
                cls.repos_payload,
                cls.org_payload,
                cls.repos_payload,
            ]
        }
        cls.get_patcher = patch("requests.get", **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """test_pubplic_repos method"""
        test_class = client.GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """test_public_repos_with_license"""
        test_class = client.GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """tearDown after setUp"""
        cls.get_patcher.stop()
