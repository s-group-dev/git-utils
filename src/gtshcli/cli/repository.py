import click

from gtshcli.services.repository_service import RepositoryService


@click.group("repository")
def cli():
    pass


@cli.command("clean-up")
def clean_up():
    """Clean up repository and reduce its disk size."""
    service = RepositoryService()
    click.echo(service.clean_up())
