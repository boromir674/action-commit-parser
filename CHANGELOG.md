# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/).

## 1.0.0 (2024-08-24)

Major Release since **Public API** has been stable.

### Changes

#### Fix
- be invariant of possible branch X updates when TO Ref is X branch & FROM is branched off of TO

#### Test
- add Test Case that expects 2 commits to be generated
- verify that client code can parse and embed commits Array with special characters in subjects
- assert action JSON output can be stored in GITHUB_ENV
- verify action can parse commit message subjects that include single-quotes

#### Docs
- add `Commits Range Topic Page`
- clean up white-space in README.md

#### CI
- fix docs-live tox environment
- automatically spawn CI Test Cases, by calling Test Worklfow, with dynamic input Matrix
- fix Automated Github Release logic for making a Prod or Draft Release
- use corresponding Action Project Name in message of merge-to-main commit

#### Other
- update gitignore to exclude development artifacts


## 0.3.0 (2024-08-22)

### Changes

#### Feature
- implement Composite Action, leveraging 'git log --pretty=format:'{"message": "%s"},' command

#### CI
- switch from local action reference to 'dev' git ref
- disable CI Jobs designed for testing Python client Code, since offer Composite Action
- add Reusable Workflow with E2E Test Case Scenario, that calls action and asserts result


## 0.2.0 (2024-08-21)

### Build
- pin griffe to 0.40.1, to prevent just released broken built creash our CI Docs Build
- start tracking poetry.lock

### CI
- disable automatic PyPI publish
- set Test Matrix 'python version' factor to [3.10, 3.11, 3.12]
- change trigger of CI/CD Pipeline to `branch` and `tag` pushes, such as:
  - any `branch push` **except** for 'dev' and 'release' branches
  - `tag push` of **run-ci** tag
  - `tag push` of **Semantic Version** Tags with pattern **v*.*.*** 
- trigger CI/CD for any branch push except 'dev' and 'release' branches
- setup 'Release Me' Git Ops Process
- reproduce docs build env using statically compiled pinned requirements
- pin Reusable Workflow to v1.10.0 for making Github Release
- use v1.11.0 of Docker Reusable Workflow

### Docs
- update cicd_mermaid diagram with up-to-date information from parsing workflow yaml
- fix automatic CLI API Ref Page generation, using correct module name

### Other
- update gitignore with generated files during development


## 0.1.0 (2024-08-20)

This is the **first** ever release of the **Action Commit Parser** Open-Source Project.
- The project is hosted in a public repository on GitHub at [https://github.com/boromir674/action-commit-parser](https://github.com/boromir674/action-commit-parser)
- The project was scaffolded using the [Cookiecutter Python Package](https://python-package-generator.readthedocs.io/en/master/) (cookiecutter) Template at [https://github.com/boromir674/cookiecutter-python-package/tree/master/src/cookiecutter_python](https://github.com/boromir674/cookiecutter-python-package/tree/master/src/cookiecutter_python)

Scaffolding included:

- **Python package** `action_commit_parser`, which is **PyPI ready**
  - Build Process with `poetry`
- **Documentation Website**, writen in `markdown`
  - Build Process with `mkdocs`

- **CI/CD Pipeline** running on GitHub Actions at [https://github.com/boromir674/action-commit-parser/actions](https://github.com/boromir674/action-commit-parser/actions)
  - **CI**
    - `Test Python` **Workflow**, running a multi-factor **Build Matrix** spanning different `python version`s
      - Python Interpreters: `3.10`, `3.11`
    - `Code Lint` **Workflow**
    - `Test Docs` **Workflow**
    - `Python Code Visualization` **Workflow**
  - **CD**
    - `Docker Build n Publish` **Workflow**
    - `PyPI Publish` **Workflow**
    - `Github Release` **Workflow**

- Automated **Test Suite**, written in `pytest`
  - Code Coverage and hosting on **codecov.io**
- Various **Automations**, for development/CI, using **tox**
  - 1-command `Lint`, `Type Check`, `Build` and `Deploy` *operations*
