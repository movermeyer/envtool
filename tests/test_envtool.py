import os.path
# from sys import version_info
# if version_info[0] == 2:
#     from mock import patch, mock_open, call
# else:
#     from unittest.mock import patch, mock_open, call

from pytest import fail

import envtool


def _fixture(name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', name)


def test_envfile_to_dict():
    assert envtool.envfile_to_dict(_fixture('basic_envfile')) == {'A': 'abcde', 'B': 'def'}

def test_parse_envfile_contents():
    assert envtool.parse_envfile_contents("""
        # Comment
        a=b
        """) == {'a': 'b'}

def test_parse_invalid_envfile_contents():
    try:
        envtool.parse_envfile_contents("""
a
        """)
        fail()
    except IOError:
        assert True

def test_envdir_to_dict():
    res = envtool.envdir_to_dict(_fixture('basic_envdir'))
    assert res == {'A': 'abcde', 'B': 'def'}

if __name__ == '__main__':
    pytest.main()
