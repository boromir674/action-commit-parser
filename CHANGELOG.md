# Changelog

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
