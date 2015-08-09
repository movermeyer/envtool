from future import standard_library
standard_library.install_aliases()

import os.path
import unittest
from sys import version_info
# if version_info[0] == 2:
#     from mock import patch, mock_open, call
# else:
#     from unittest.mock import patch, mock_open, call

import envtool


def _fixture(name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', name)


class MainTestCase(unittest.TestCase):
    def test_parse_envfile_contents(self):
        self.assertEqual(envtool.parse_envfile_contents("""
        # Comment
        a=b
        """), {'a': 'b'})

    def test_parse_invalid_envfile_contents(self):
        self.assertRaises(
            IOError,
            lambda: envtool.parse_envfile_contents("""
a
            """)
        )

    def test_envdir_to_dict(self, ):
        res = envtool.envdir_to_dict(_fixture('basic_envdir'))
        self.assertEqual(res, {'A': 'abcde', 'B': 'def'})


if __name__ == '__main__':
    unittest.main()
