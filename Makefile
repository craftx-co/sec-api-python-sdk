dev:
	pip3 install pipenv --upgrade
	pipenv install --dev
	pipenv shell

flake8:
	pipenv run flake8 sec_python_sdk

publish:
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	rm -rf build dist .egg sec_python_sdk.egg-info

clear-build:
	rm -rf build dist .egg sec_python_sdk.egg-info
