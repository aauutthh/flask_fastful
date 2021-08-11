all:

dist/flask_fastful-0.1.tar.gz:
	python setup.py sdist

sdist: dist/flask_fastful-0.1.tar.gz

install: dist/flask_fastful-0.1.tar.gz
	pip install $<

clean:
	rm -Rf ./flask_fastful.egg-info dist build
	find . -type d -name '.mypy_cache'|xargs rm -rf
	find . -type d -name '__pycache__'|xargs rm -rf
	find . -type d -name '.pytest_cache'|xargs rm -rf
