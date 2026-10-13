#!/usr/bin/env python3
"""A small command-line tool for dev/test purposes.

Usage examples:

    python cli.py greet World
    python cli.py add 1 2 3.5
    python cli.py repeat hello --count 3
"""

import argparse
import sys

__version__ = "0.1.0"


def greet(name, shout=False):
    message = "Hello, {}!".format(name)
    return message.upper() if shout else message


def add(numbers):
    total = sum(numbers)
    return int(total) if total == int(total) else total


def repeat(text, count=1):
    return [text] * count


def build_parser():
    parser = argparse.ArgumentParser(
        prog="cli.py", description="A small dev/test command-line tool.")
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_greet = subparsers.add_parser("greet", help="print a greeting")
    p_greet.add_argument("name", help="who to greet")
    p_greet.add_argument("--shout", action="store_true",
                         help="print the greeting in upper case")

    p_add = subparsers.add_parser("add", help="add numbers together")
    p_add.add_argument("numbers", nargs="+", type=float,
                       help="numbers to add")

    p_repeat = subparsers.add_parser("repeat", help="print text repeatedly")
    p_repeat.add_argument("text", help="text to print")
    p_repeat.add_argument("--count", "-n", type=int, default=1,
                          help="number of times to print (default: 1)")

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.command == "greet":
        print(greet(args.name, shout=args.shout))
    elif args.command == "add":
        print(add(args.numbers))
    elif args.command == "repeat":
        for line in repeat(args.text, args.count):
            print(line)

    return 0


if __name__ == "__main__":
    sys.exit(main())
