# See LICENSE for details.
"""
Build script for Chevah StyleGuide website.
"""
from __future__ import print_function
from pkg_resources import load_entry_point
import sys

from brink.pavement_commons import (
    default,
    help,
    pave,
    SETUP,
    )
from paver.easy import needs, pushd, task, consume_args

# Workaround for lint
default
help

SETUP['pypi']['index_url'] = 'http://pypi.chevah.com:10042/simple'

hyde_path = pave.fs.join([pave.path.build, 'bin', 'hyde'])
python_27 = pave.fs.join([pave.path.build, 'bin', 'python'])
deploy_path = pave.fs.join([pave.path.build, 'deploy'])

DEPENDENCIES = [
    'docutils',
    'pelican==3.3',
    'ghp-import==0.4.1'
    ]


@task
def deps():
    pave.pip(
        command='install',
        arguments=DEPENDENCIES,
        )


@task
def build():
    """
    Build the static files.
    """
    sys.argv = ['pelican']
    load_entry_point('pelican==3.3', 'console_scripts', 'pelican')()


@task
def dev():
    """
    Build the static files.
    """
    sys.argv = ['pelican', '-r']
    load_entry_point('pelican==3.3', 'console_scripts', 'pelican')()


@task
@needs('build')
def run():
    """
    Generate content to be opened using local file URL.
    """
    print('Listening on http://localhost:8080. Ctrl+C to stop.')
    with pushd('deploy'):
        import SocketServer
        SocketServer.TCPServer.allow_reuse_address = True
        # Side-effect import.
        sys.argv = ['pelican-server', '8080']
        from pelican import server


@task
@needs('build')
def publish():
    """
    Upload the generated files to gh-pages branch.
    """
    print('Publishing changes to GitHub gh-pages branch...')
    ghp_import = pave.fs.join([pave.path.build, 'bin', 'ghp-import'])
    pave.execute(
        command=[ghp_import, '-p', '-r', 'origin', '-b', 'gh-pages', 'deploy'],
        output=sys.stdout,
        )