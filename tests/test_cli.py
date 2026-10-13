"""Tests for the dev/test command-line tool in cli.py."""

import os.path
import subprocess
import sys

import pytest

import cli

CLI_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cli.py")


def test_greet():
    assert cli.greet("World") == "Hello, World!"
    assert cli.greet("World", shout=True) == "HELLO, WORLD!"
    assert cli.greet("Steve") == "Hello, Steve!"
    assert cli.greet("sTeVe", shout=True) == "HELLO, STEVE!"


def test_add():

    assert cli.add([]) == 0
    assert cli.add([1]) == 1
    assert cli.add([1, 2]) == 3
    assert cli.add([1, 2, 3]) == 6
    assert cli.add([1, 2, 3, 4]) == 10
    assert cli.add([2, 3, 4]) == 9
    assert cli.add([3, 4]) == 7
    assert cli.add([4]) == 4
    assert cli.add([1.5, 2]) == 3.5
    with pytest.raises(TypeError) as e:
        cli.add(["a", "b", "c"]) == "abc"


def test_repeat():
    assert cli.repeat("hi", 3) == ["hi", "hi", "hi"]


def test_main_greet(capsys):
    assert cli.main(["greet", "World", "--shout"]) == 0
    assert capsys.readouterr().out == "HELLO, WORLD!\n"


def test_main_add(capsys):
    assert cli.main(["add", "1", "2", "3.5"]) == 0
    assert capsys.readouterr().out == "6.5\n"


def test_main_repeat(capsys):
    assert cli.main(["repeat", "hi", "-n", "2"]) == 0
    assert capsys.readouterr().out == "hi\nhi\n"


def test_main_requires_command():
    with pytest.raises(SystemExit) as exc_info:
        cli.main([])
    assert exc_info.value.code == 2


def test_script_runs_as_subprocess():
    result = subprocess.run(
        [sys.executable, CLI_PATH, "greet", "CI"],
        capture_output=True, text=True, check=True)
    assert result.stdout == "Hello, CI!\n"
