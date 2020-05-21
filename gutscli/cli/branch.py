import click
from gutscli.services.branch_service import BranchService


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
    service = BranchService()
    params = [p_type, 'true', filter]
    output = service.list(branch, params)

    if output:
        click.echo(output)

    if delete:
        for x in output.splitlines():
            params = [p_type, 'origin',
                      x] if p_type == 'remote' else [p_type, x]
            click.echo(service.delete(params))


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
    service = BranchService()
    params = [p_type, 'false', filter]
    output = service.list(branch, params)

    if output:
        click.echo(output)

    if delete:
        for x in output.splitlines():
            params = [p_type, 'origin',
                      x] if p_type == 'remote' else [p_type, x]
            click.echo(service.delete(params))
