[![tests](https://github.com/KKashpovski/pythonProject_Testing_REST_API_Store/actions/workflows/tests.yml/badge.svg?branch=branch_1)](https://github.com/KKashpovski/pythonProject_Testing_REST_API_Store/actions/workflows/tests.yml)

# Python api tests

This is a tutorial project that shows how to implement api tests in Python

The project uses:
1. Python
2. Requests
3. Allure for reports
4. CI (GitHub actions)


Testing application (write with Flask):

git: https://github.com/KKashpovski/pythonProject_Testing_REST_API_Store

url: https://stores-tests-api.herokuapp.com


### How to start

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

or install poetry https://python-poetry.org/, then

```
poetry install
```

and add pre-commit
```
pre-commit install
```

### Run all tests

```python
pytest
```
"# pythonProject_REST_API_Store_Testing" 
