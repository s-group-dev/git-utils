from unittest.mock import call, patch

import pytest
from click.testing import CliRunner

from gtshcli.cli.branch import cli
from gtshcli.services.branch_service import BranchService


@pytest.fixture
def runner():
    return CliRunner()


@patch.object(BranchService, "list")
def test_list_merged_is_called_with_params(mock_method, runner):
    _test_list_with_params(mock_method, "list-merged", "true", runner)


@patch.object(BranchService, "list")
def test_list_wip_is_called_with_params(mock_method, runner):
    _test_list_with_params(mock_method, "list-wip", "false", runner)


def _test_list_with_params(mock_method, method, is_merged, runner):
    mock_method.return_value = None

    branch = "foo"
    filter = "filter123"
    remote = "remote456"
    params = [method, "--branch", branch, "--remote", remote, "--filter", filter]
    result = runner.invoke(cli, params)

    mock_method.assert_called_once_with(branch, [remote, is_merged, filter])

    assert result.exit_code == 0
    assert result.output.strip() == ""


@patch.object(BranchService, "list")
@patch.object(BranchService, "delete")
def test_list_merged_and_delete(mock_method_delete, mock_method_list, runner):
    _test_list_with_delete(
        mock_method_delete, mock_method_list, "list-merged", "true", runner
    )


@patch.object(BranchService, "list")
@patch.object(BranchService, "delete")
def test_list_wip_and_delete(mock_method_delete, mock_method_list, runner):
    _test_list_with_delete(
        mock_method_delete, mock_method_list, "list-wip", "false", runner
    )


def _test_list_with_delete(
    mock_method_delete, mock_method_list, method, is_merged, runner
):
    output1 = "foo\nbar"
    output2 = ["abc", "def"]
    mock_method_list.return_value = output1
    mock_method_delete.side_effect = output2

    branch = "branch123"
    filter = "filter456"
    remote = "remote789"
    params = [
        method,
        "--branch",
        branch,
        "--remote",
        remote,
        "--filter",
        filter,
        "--delete",
    ]
    result = runner.invoke(cli, params)

    mock_method_list.assert_called_with(branch, [remote, is_merged, filter])

    assert mock_method_delete.call_count == 2
    mock_method_delete.assert_has_calls(
        [call([remote, x]) for x in output1.splitlines()], any_order=True
    )

    assert result.exit_code == 0
    assert result.output.strip() == output1 + "\n" + "\n".join(output2)
