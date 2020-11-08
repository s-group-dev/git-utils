#!/usr/bin/env python3

import sys

import click

from gutscli.cli.branch import cli as branch_command
from gutscli.cli.remote import cli as remote_command
from gutscli.cli.repository import cli as repository_command
from gutscli.exceptions import GutsException


@click.group()
def cli():
    pass


cli.add_command(branch_command)
cli.add_command(repository_command)
cli.add_command(remote_command)


def main():
    try:
        cli()
    except GutsException as e:
        click.secho(str(e), fg="red")
        sys.exit(1)


if __name__ == "__main__":
    main()
