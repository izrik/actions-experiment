"""Placeholder tests so the CI workflow has something to run."""

import os.path


def test_arithmetic():
    assert 1 + 1 == 2


def test_string_formatting():
    assert "actions-{}".format("experiment") == "actions-experiment"


def test_repo_files_exist():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for name in ("README.md", "info.yaml", "Dockerfile"):
        assert os.path.exists(os.path.join(repo_root, name)), name
