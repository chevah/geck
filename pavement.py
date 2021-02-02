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
    'Sphinx==3.4.3',
    'sphinx-autobuild==2020.9.1',
    'sphinx_rtd_theme==0.5.1',
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
    from sphinx.cmd.build import main
    main(argv=args)


@task
def generate():
    """
    Generate the site as local static files.
    """
    build_html = os.path.join(os.getcwd(), 'build', 'html')

    # Works: sphinx-build -b html -j 2 -n -W docs/ build/html/
    _run_sphinx(['-b', 'html', '-j', '2', '-n', '-W', 'docs/', build_html])
    print("Open the result in a browser: file://%s/index.html" % build_html)


@task
def test():
    """
    Run a few tests.
    """
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
