import click
import os
import subprocess


@click.group('branch')
def cli():
    pass


@cli.command('list-merged')
@click.option('-b', '--branch',
              required=False,
              default='master',
              help='Default branch/trunk')
@click.option('-t', '--type', 'p_type',
              required=False,
              default='local',
              help='Run against local or remote branches',
              type=click.Choice(['local', 'remote']))
@click.option('--delete',
              is_flag=True,
              default=False,
              help='Delete merged branches')
def list_merged(branch, p_type, delete):
    process = subprocess.run([_get_scripts_dir() + '/branch-list.sh',
                              branch,
                              p_type,
                              'true'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    if process.stdout == '':
        return
    click.secho(process.stdout)


@cli.command('list-wip')
@click.option('-b', '--branch',
              required=False,
              default='master',
              help='Default branch/trunk')
@click.option('-t', '--type', 'p_type',
              required=False,
              default='local',
              help='Run against local or remote branches',
              type=click.Choice(['local', 'remote']))
def list_wip(branch, p_type):
    process = subprocess.run([_get_scripts_dir() + '/branch-list.sh',
                              branch,
                              p_type,
                              'false'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    if process.stdout == '':
        return
    click.secho(process.stdout)


def _get_scripts_dir():
    return os.path.realpath(
        os.path.dirname(
            os.path.realpath(__file__)) + '/../scripts')
