#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.add_git_pre_commit_hook_black }}' == 'n':
        remove_file('pyproject.toml')

    if '{{ cookiecutter.manuscript_format }}' == 'R Markdown':
        remove_file('doc/main.tex')

    if '{{ cookiecutter.manuscript_format }}' == 'LaTeX':
        remove_file('doc/main.rmd')

    if '{{ cookiecutter.manuscript_format }}' == 'Other':
        remove_file('doc/main.rmd')
        remove_file('doc/main.tex')
        remove_file('doc/references.bib')
