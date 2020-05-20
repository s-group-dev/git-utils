import click
from gutscli.utils.SubProcessRunner import SubProcessRunner


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
    process = SubProcessRunner()
    output = process.run('branch-list', [branch, p_type, 'true', filter])

    if output == '':
        return
    click.echo(output)

    if delete:
        for x in output.splitlines():
            if p_type == 'remote':
                params = [p_type, 'origin', x]
            else:
                params = [p_type, x]

            click.echo(process.run('branch-delete', params))


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
    process = SubProcessRunner()
    output = process.run('branch-list', [branch, p_type, 'false', filter])

    if output == '':
        return
    click.echo(output)

    if delete:
        for x in output.splitlines():
            if p_type == 'remote':
                params = [p_type, 'origin', x]
            else:
                params = [p_type, x]

            click.echo(process.run('branch-delete', params))
