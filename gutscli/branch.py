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
@click.option('-f', '--filter',
              required=False,
              default='',
              help='Filter output (case-insensitive)')
@click.option('--delete',
              is_flag=True,
              default=False,
              help='Delete merged branches')
def list_merged(branch, p_type, filter, delete):
    """List all other branches that are merged to given branch.
    """
    process = subprocess.run([_get_scripts_dir() + '/branch-list.sh',
                              branch,
                              p_type,
                              'true',
                              filter],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    if process.stdout == '':
        return
    output = process.stdout.strip()
    click.echo(output)

    if delete:
        for x in output.splitlines():
            if p_type == 'remote':
                params = [_get_scripts_dir() + '/branch-delete.sh',
                          p_type,
                          'origin',
                          x]
            else:
                params = [_get_scripts_dir() + '/branch-delete.sh',
                          p_type,
                          x]

            click.echo(subprocess.run(params,
                                      stdout=subprocess.PIPE,
                                      universal_newlines=True
                                      ).stdout.strip())


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
@click.option('-f', '--filter',
              required=False,
              default='',
              help='Filter output (case-insensitive)')
@click.option('--delete',
              is_flag=True,
              default=False,
              help='Delete merged branches')
def list_wip(branch, p_type, filter, delete):
    """List all other branches that are NOT merged to given branch.
    """
    process = subprocess.run([_get_scripts_dir() + '/branch-list.sh',
                              branch,
                              p_type,
                              'false',
                              filter],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    if process.stdout == '':
        return
    output = process.stdout.strip()
    click.echo(output)

    if delete:
        for x in output.splitlines():
            if p_type == 'remote':
                params = [_get_scripts_dir() + '/branch-delete.sh',
                          p_type,
                          'origin',
                          x]
            else:
                params = [_get_scripts_dir() + '/branch-delete.sh',
                          p_type,
                          x]

            click.echo(subprocess.run(params,
                                      stdout=subprocess.PIPE,
                                      universal_newlines=True
                                      ).stdout.strip())


def _get_scripts_dir():
    return os.path.realpath(
        os.path.dirname(
            os.path.realpath(__file__)) + '/../scripts')
