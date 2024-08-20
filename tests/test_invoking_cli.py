import sys


def test_invoking_cli_as_python_module(run_subprocess):
    result = run_subprocess(
        sys.executable,
        '-m',
        'action_commit_parser',
        '--help',
    )
    assert result.exit_code == 0
    assert result.stderr == ''
    assert result.stdout.split('\n')[0] == "Usage: action-commit-parser [OPTIONS]"
