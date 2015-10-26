# -*- coding: utf-8 -*-
"""Test that the package exists and has specified metadata."""

import {{ cookiecutter.project_slug }}


def test_version():
    assert {{ cookiecutter.project_slug }}.__version__ == '{{ cookiecutter.version }}'
