import subprocess
from services.subprocess_runner import SubprocessRunner

def test_truthy():
    """
    Test that will succeed
    """
    assert True == True

def test_with_mock(mocker):
    """
    Example of mock test
    """
    mocker.patch('subprocess.run')
    runner = SubprocessRunner()
    runner.run('script', [])
    subprocess.run.assert_called()
