#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re


def size_salt_range_type(size):
    size = int(size)
    if size < 0 or size > 1024:
        raise argparse.ArgumentTypeError("Salt size must be between 0 and 1024")
    return size


def round_range_type(round):
    round = int(round)
    if round < 1 or round > 4294967295:
        raise argparse.ArgumentTypeError("Number of rounds must be between 1 and 4294967295")
    return round


def __encrypt_password(args) -> str:
    if args.a == 'pbkdf2_sha1':
        from passlib.hash import pbkdf2_sha1 as algorithm
    elif args.a == 'pbkdf2_sha256':
        from passlib.hash import pbkdf2_sha256 as algorithm
    elif args.a == 'pbkdf2_sha512':
        from passlib.hash import pbkdf2_sha512 as algorithm
    elif args.a == 'bcrypt_sha256':
        from passlib.hash import bcrypt_sha256 as algorithm

        if args.s != 22:
            print('bcrypt_sha256 was selected as password hashing algorithm, setting salt size to 22')
            args.s = 22

        if args.r < 4:
            print('bcrypt_sha256 was selected as password hashing algorithm, increasing the number of rounds to 4')
            args.r = 4

        if args.r > 31:
            print('bcrypt_sha256 was selected as password hashing algorithm, reducing the number of rounds to 31')
            args.r = 31
    else:
        from passlib.hash import pbkdf2_sha256 as algorithm

    return algorithm.using(rounds=args.r, salt_size=args.s).hash(args.password)


def main():
    """
    ..todo:: Add a method to auto generate a password
    """

    parser = argparse.ArgumentParser(prog='encrypt_password.py',
                                     description='Encrypt a clear text password for an OXAP account configuration')

    parser.add_argument('password',
                        type=str,
                        nargs='?',
                        help='The clear text password to encrypt. Password cannot be empty, '
                             'or start / end with white-space')
    parser.add_argument('-s',
                        type=size_salt_range_type,
                        default=16,
                        metavar='<size>',
                        help='Optional number of bytes to use when autogenerating new '
                             'salts. Defaults to 16 bytes, but can be any value between '
                             '0 and 1024. If the \'bcrypt_sha256\' hashing algorithm was '
                             'selected the salt size will be set to 22 regardless')
    parser.add_argument('-r',
                        type=round_range_type,
                        default=29000,
                        metavar='<rounds>',
                        help='Optional number of rounds to use. Defaults to 29000, but '
                             'must be within range (1,4294967295). If the \'bcrypt_sha256\' '
                             'hashing algorithm was selected the number of rounds will '
                             'be reduced to 31 if the value specified is bigger than 31')
    parser.add_argument('--display-input',
                        action="store_true",
                        help='Specify if the original (cleartext) password should be displayed in result')
    parser.add_argument('--no-password-check',
                        action="store_true",
                        help='Skip the password check, otherwise: A digit must occur at least '
                             'once, a lower case letter must occur at least once, an upper case '
                             'letter must occur at least once, a special character must occur at '
                             'least once, no whitespace allowed in the entire string, minimum '
                             'password length is 8 characters')
    parser.add_argument('-a',
                        type=str,
                        choices=('pbkdf2_sha1', 'pbkdf2_sha256', 'pbkdf2_sha512', 'bcrypt_sha256'),
                        default='pbkdf2_sha256',
                        metavar='<algorithm>',
                        help='The password hashing algorithm to use for the password '
                             'encryption. Default is \'pbkdf2_sha256\', options are: '
                             '\'pbkdf2_sha1\', \'pbkdf2_sha256\', \'pbkdf2_sha512\', \'bcrypt_sha256\'')

    args = parser.parse_args()

    if not args.no_password_check:
        p = re.compile('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,}$')
        if not re.search(p, args.password):
            parser.print_help()
            exit(0)

    if args.display_input:
        print('Password (cleartext): ', args.password)
        print('Password (encrypted): ', __encrypt_password(args))
    else:
        print(__encrypt_password(args))


if __name__ == "__main__":
   main()
