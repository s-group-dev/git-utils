from unittest.mock import patch

from gtshcli.services.subprocess_runner import SubprocessRunner


def test_run():
    runner = SubprocessRunner()
    script_name = "foo"
    params = ["a", "b"]
    with patch("subprocess.run") as mock_run:
        runner.run(script_name, params)

    mock_run.assert_called_once()

    args = mock_run.call_args.args[0]
    assert script_name in args[0]
    assert params[0] == args[1]
    assert params[1] == args[2]
