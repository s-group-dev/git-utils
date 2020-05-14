import click


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
    print("ok")
