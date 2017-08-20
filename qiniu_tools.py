# reference: https://developer.qiniu.com/kodo/sdk/1242/python

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

import argparse
import sys
import os

access_key = 'access_key'
secret_key = 'secret_key'


def parseopts():
    arguementparser = argparse.ArgumentParser()

    subparsers = arguementparser.add_subparsers(title='command', dest='command')

    upload_parser = subparsers.add_parser('upload')

    upload_parser.add_argument('file', nargs='+', help='files you want to upload')

    upload_parser.add_argument('-b', '--bucket', action='store', required=True, type=str,
                               metavar='<bucket>')

    options = arguementparser.parse_args()

    return options


def upload(options):
    q = Auth(access_key, secret_key)

    for file in options.file:
        print('dealing with {}'.format(file))

        if not os.path.isfile(file):
            print('{} is not a file'.format(file))
            continue


def main():
    options = parseopts()

    print(options)

    if options.command == 'upload':
        upload(options)


if __name__ == '__main__':
    sys.exit(main())
