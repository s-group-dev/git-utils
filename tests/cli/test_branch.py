from unittest.mock import ANY, patch

import pytest
from click.testing import CliRunner

from gutscli.cli.branch import cli
from gutscli.services.branch_service import BranchService


@pytest.fixture
def runner():
    return CliRunner()


@patch.object(BranchService, "list")
def test_list_merged_is_called_with_branch_name(mock_method, runner):
    branch = "foo"
    result = runner.invoke(cli, ["list-merged", "--branch", branch])

    mock_method.assert_called_once_with(branch, ANY)
    assert result.exit_code == 0
