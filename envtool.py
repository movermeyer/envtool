#!/usr/bin/env python

from __future__ import print_function

import io
import os.path

import click

version = __version__ = '0.0.0'

def envdir_to_dict(d):
    result = {}
    for fname in os.listdir(d):
        path = os.path.join(d, fname)
        with open(path) as c:
            result[fname] = c.read()
    return result


def dict_to_envdir(env_vars, dpath):
    if not os.path.exists(dpath):
        os.mkdir(dpath)
    for k, v in env_vars.items():
        with open(os.path.join(dpath, k), 'w') as f:
            f.write(v)


def parse_envfile_contents(contents):
    result = {}
    try:
        for line in contents.strip().splitlines():
            if line.strip() and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                result[k] = v
    except ValueError:
        raise IOError("Invalid env file format: {0}".format(line))
    return result


def envfile_to_dict(fpath, encoding='utf-8'):
    with io.open(fpath, encoding=encoding) as f:
        return parse_envfile_contents(f.read())


def dict_to_envfile(env_vars, fpath):
    with open(fpath, 'w') as f:
        for k, v in env_vars.items():
            print('{0}={1}'.format(k, v), file=f)


@click.group()
def main():
    pass


def convert_from_dir(src, dest):
    print("Converting from directory {0} to {1}".format(src, dest))


def convert_from_file(src, dest):
    print("Converting from file {0} to {1}".format(src, dest))


@main.command()
@click.argument('src', type=click.Path(exists=True))
@click.argument('dest', type=click.Path())
def convert(src, dest):
    if os.path.isdir(src) and (os.path.isfile(dest) or not os.path.exists(dest)):
        convert_from_dir(src, dest)
    elif os.path.isfile(src) and (os.path.isdir(dest) or not os.path.exists(dest)):
        convert_from_file(src, dest)

if __name__ == '__main__':
    main()
