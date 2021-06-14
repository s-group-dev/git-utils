from unittest.mock import patch

from gtshcli.services.branch_service import BranchService


@patch.object(BranchService, "run")
def test_list(mock_method):
    assert "def" == _test_list(mock_method, "def")


@patch.object(BranchService, "run")
def test_list_empty(mock_method):
    assert _test_list(mock_method, "") is None


@patch.object(BranchService, "run")
def test_delete(mock_method):
    service = BranchService()

    params = ["a", "b", "c"]

    service.delete(params)

    mock_method.assert_called_once_with("branch-delete", params)


def _test_list(mock_method, return_value):
    service = BranchService()

    branch = "foo"
    params = ["a", "b", "c"]
    ret = return_value

    mock_method.return_value = ret
    result = service.list(branch, params)

    mock_method.assert_called_once_with("branch-list", [branch] + params)
    return result
