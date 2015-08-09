import unittest
try:
    from mock import patch, mock_open, call
except ImportError:
    from unittest.mock import patch, mock_open, call

import envtool


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

    @patch('os.listdir')
    @patch('envtool.open', mock_open(read_data="abcde"))
    def test_envdir_to_dict(self, listdir_stub):
        listdir_stub.return_value = ['A', 'B']
        res = envtool.envdir_to_dict('dirname')
        self.assertEqual(res, {'A': 'abcde', 'B': 'abcde'})
        self.assertEqual(envtool.open.mock_calls, [call('dirname/A'),
            call().__enter__(),
            call().read(),
            call().__exit__(None, None, None),
            call('dirname/B'),
            call().__enter__(),
            call().read(),
            call().__exit__(None, None, None)
        ])


if __name__ == '__main__':
    unittest.main()
