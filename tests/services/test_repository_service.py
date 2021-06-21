from unittest.mock import patch

from gtshcli.services.repository_service import RepositoryService


@patch.object(RepositoryService, "run")
def test_clean_up(mock_method):
    service = RepositoryService()

    service.clean_up()

    mock_method.assert_called_once_with("repository-clean-up", [])
