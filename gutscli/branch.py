import click
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
    process = subprocess.run(['scripts/branch-list-merged.sh', branch, p_type],
                             stdout=subprocess.PIPE, universal_newlines=True)
    output = process.stdout.strip()
    click.secho(output)


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
    process = subprocess.run(['scripts/branch-list-wip.sh', branch, p_type],
                             stdout=subprocess.PIPE, universal_newlines=True)
    click.secho(process.stdout.strip())
