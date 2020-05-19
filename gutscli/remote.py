import click


@click.group('remote')
def cli():
    pass


@cli.command('merge-subtree')
@click.option('-r', '--remote',
              required=True,
              help='Absolute URL pointing to a project.')
@click.option('-b', '--branch',
              required=False,
              default='master',
              help='Default branch/trunk')
@click.option('-t', '--target',
              required=False,
              default='./',
              help='Target directory.')
def list_merged(remote, branch, target):
    print(remote, branch, target)
