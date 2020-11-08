import click

from gutscli.services.branch_service import BranchService


@click.group("branch")
def cli():
    pass


@cli.command("list-merged")
@click.option(
    "-b", "--branch", required=False, default="master", help="Default branch/trunk"
)
@click.option(
    "-r",
    "--remote",
    "remote",
    required=False,
    help="Remote to check against. If omited, checks against local",
)
@click.option(
    "-f",
    "--filter",
    required=False,
    default="",
    help="Filter output (case-insensitive)",
)
@click.option("--delete", is_flag=True, default=False, help="Delete merged branches")
def list_merged(branch, remote, filter, delete):
    """List all other branches that are merged to given branch."""
    service = BranchService()
    params = [remote if remote is not None else "", "true", filter]
    output = service.list(branch, params)

    if output is None:
        return

    click.echo(output)

    if delete:
        for x in output.splitlines():
            params = [remote if remote is not None else "", x]
            click.echo(service.delete(params))


@cli.command("list-wip")
@click.option(
    "-b", "--branch", required=False, default="master", help="Default branch/trunk"
)
@click.option(
    "-r",
    "--remote",
    "remote",
    required=False,
    help="Remote to check against. If omited, checks against local",
)
@click.option(
    "-f",
    "--filter",
    required=False,
    default="",
    help="Filter output (case-insensitive)",
)
@click.option("--delete", is_flag=True, default=False, help="Delete merged branches")
def list_wip(branch, remote, filter, delete):
    """List all other branches that are NOT merged to given branch."""
    service = BranchService()
    params = [remote if remote is not None else "", "false", filter]
    output = service.list(branch, params)

    if output is None:
        return

    click.echo(output)

    if delete:
        for x in output.splitlines():
            params = [remote if remote is not None else "", x]
            click.echo(service.delete(params))
