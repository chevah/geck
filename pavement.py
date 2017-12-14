# Copyright (c) 2017 Adi Roiban.
# See LICENSE for details.
"""
Build script for Python binary distribution.
"""
from __future__ import unicode_literals, print_function
import os
import sys
from paver.easy import path, task


RUN_PACKAGES = [
    'sphinx',
    'sphinx-autobuild',
    'sphinx_rtd_theme',
    ]


@task
def deps():
    """
    Copy external dependencies.
    """
    print('Installing dependencies to ...')
    from pip import main
    main(args=['install'] + RUN_PACKAGES)


def _run_sphinx(args):
    """
    Run sphinx build with `args`.
    """
    from sphinx import main
    main(argv=['build'] + args)


@task
def generate():
    """
    Generate the site as local static files.
    """
    build_html = os.path.join(os.getcwd(), 'build', 'html')
    _run_sphinx(['-b', 'html', '-j', '2', '-n', 'docs/', build_html])
    print("Open the result in a browser: file://%s/index.html" % build_html)


@task
def test():
    build_errors = os.path.join(os.getcwd(), 'build', 'errors')
    path(build_errors).remove()

    build_html = os.path.join(os.getcwd(), 'build', 'html')
    _run_sphinx([
        '-b', 'html',
        '-j', '2',
        '-Ean', '-w', build_errors,
        'docs/', build_html,
        ])
    errors = open(build_errors, 'r').read()
    if errors:
        print('Errors summary:\n\n')
        print(errors)
        sys.exit(1)
