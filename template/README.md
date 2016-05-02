# <PACKAGE_NAME>
<PACKAGE_ONELINER>

Source at [GitHub](<GIT_REPO>).

Docs at [PythonHosted.org](http://pythonhosted.org/<PACKAGE_NAME_LOWER>/).

## Install

Install <PACKAGE_NAME> via pip:

```python
pip install <PACKAGE_NAME_LOWER>
```

## How to use

TBD

## Build & upload

To build and upload to pypi (more info here http://peterdowns.com/posts/first-time-with-pypi.html):

```
# first to test repo:
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest

# now actually upload to pypi:
python setup.py register -r pypi
python setup.py sdist upload -r pypi
```

To create docs (will be generated into 'site' folder):

```
mkdocs build --clean
```

## Run Tests

From <PACKAGE_NAME> root dir:

```shell
cd tests
python run_tests.py
```

Note: tests are not included in the pypi package ("pip insall" won't fetch them). 
To run tests please clone from git.

## Changes

## Contact

For bugs use the issue report, for other stuff feel free to contact me at <AUTHOR_EMAIL>.


__Project structure generated via [PypiProjectGenerator](https://github.com/RonenNess/PypiProjectGenerator).__

