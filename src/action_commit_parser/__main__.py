"""Run `python -m action_commit_parser`.

Allow running Action Commit Parser, also by invoking
the python module:

`python -m action_commit_parser`

This is an alternative to directly invoking the cli that uses python as the
"entrypoint".
"""

from __future__ import absolute_import

from action_commit_parser.cli import main

if __name__ == "__main__":  # pragma: no cover
    main(prog_name="action-commit-parser")  # pylint: disable=unexpected-keyword-arg
