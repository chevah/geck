# See LICENSE for details.
'''
Build script for Chevah StyleGuide website.
'''
from __future__ import with_statement
import sys

from pavement_lib import (
    _p,
    default,
    pave,
    help,
    )
from paver.easy import needs, pushd, task, consume_args

# Workaround for lint
default
help

hyde_path = _p([pave.path.build, 'bin', 'hyde'])
python_27 = _p([pave.path.build, 'bin', 'python2.7'])
deploy_path = _p([pave.path.build, 'deploy'])


@task
def deps():
    pave.copyDefaultBuildtimeDeps()
    pave.execute([
        'virtualenv', '-p', '/usr/bin/python2.7', pave.path.build],
        output=sys.stdout,
        )
    with pushd(pave.path.build):
        pip_path = _p(['bin', 'pip'])
        pave.execute(
            [python_27, pip_path,
                'install',
                '-i', 'http://b.pypi.python.org/simple/',
                'docutils'],
            output=sys.stdout,
            )

        pave.execute(
            [python_27, pip_path,
                'install', '-e', 'git://github.com/chevah/hyde.git#egg=hyde'],
            output=sys.stdout,
            )


@task
def build():
    '''Build the static files.'''
    pave.execute([
        python_27, hyde_path, '-v', 'gen', '-r',
        '-c' 'site.yaml',
        '-d', deploy_path,
        ],
        output=sys.stdout)


@task
@needs('build')
def run():
    '''Generate content to be opened using local file URL.'''
    pave.execute([
        python_27, hyde_path, 'serve',
        '-c' 'site.yaml',
        '-d', deploy_path,
        ],
        output=sys.stdout)


@task
@consume_args
def hyde(args):
    '''Executes the hyde command.'''
    command = [python_27, hyde_path]
    command.extend(args)
    pave.execute(command, output=sys.stdout)


@task
@needs('build')
def publish():
    '''Upload the generated files.

    Before publishing the site, make sure the server key is cached.
    '''
    publish_user = 'chevah_site'
    publish_host = 'styleguide.chevah.com'
    publish_path = '/home/chevah_site/styleguide.chevah.com/'
    destination = '%s@%s:"%s"' % (publish_user, publish_host, publish_path)
    pave.execute([
        'rsync', '-aqcz', '-e', "'ssh'", deploy_path + '/', destination],
        output=sys.stdout)
    print 'Site published to %s' % (destination)
