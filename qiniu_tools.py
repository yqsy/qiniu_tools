# reference: https://developer.qiniu.com/kodo/sdk/1242/python

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

import argparse
import sys


def parseopts():
    arguementparser = argparse.ArgumentParser()

    subparsers = arguementparser.add_subparsers(title='command', dest='command')

    upload_parser = subparsers.add_parser('upload')

    upload_parser.add_argument('file', nargs='+', help='files you want to upload')

    upload_parser.add_argument('-b', '--bucket', action='store', required=True,
                               metavar='<bucket>')

    upload_parser.add_argument('-a', '--access_key', action='store', required=True,
                               metavar='<access_key>')

    upload_parser.add_argument('-s', '--secret_key', action='store', required=True,
                               metavar='<secret_key>')

    options = arguementparser.parse_args()

    print(options)

    return options


def main():
    options = parseopts()


if __name__ == '__main__':
    sys.exit(main())
