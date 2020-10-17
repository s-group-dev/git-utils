#!/usr/bin/env python3

from cli.branch import cli as branch_command
from cli.remote import cli as remote_command
from cli.repository import cli as repository_command
from exceptions import GutsException
import click
import sys


@click.group()
def cli():
    pass


cli.add_command(branch_command)
cli.add_command(repository_command)
cli.add_command(remote_command)

if __name__ == '__main__':
    try:
        cli()
    except GutsException as e:
        click.secho(str(e), fg='red')
        sys.exit(1)
