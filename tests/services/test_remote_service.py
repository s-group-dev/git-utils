from unittest.mock import patch

from gtshcli.services.remote_service import RemoteService


@patch.object(RemoteService, "run")
def test_subtree_merge(mock_method):
    assert "def" == _test_subtree_merge(mock_method, "def")


@patch.object(RemoteService, "run")
def test_sybtree_merge_empty(mock_method):
    assert _test_subtree_merge(mock_method, "") is None


def _test_subtree_merge(mock_method, return_value):
    service = RemoteService()

    params = ["a", "b", "c"]
    mock_method.return_value = return_value

    result = service.subtree_merge(params[0], params[1], params[2])

    mock_method.assert_called_once_with("remote-merge-subtree", params)
    return result
