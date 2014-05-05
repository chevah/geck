# See LICENSE for details.
'''
Build script for Chevah StyleGuide website.
'''
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
    'git+https://github.com/chevah/hyde.git#egg=hyde'
    ]


@task
def deps():
    pave.pip(
        command='install',
        arguments=DEPENDENCIES,
        )


@task
def build():
    '''Build the static files.'''
    pave.execute([
        python_27, hyde_path, 'gen', '-r',
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
