all: default

clean: 
	rm -rf dist/
	
deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

check-format: dev_deps
	yapf -rd is_numeric/

format: dev_deps
	yapf -ri is_numeric/

lint: check-format
	pylint -r n is_numeric/

lint-no-error: 
	pylint --exit-zero -r n is_numeric/

test: init dev_deps
	python3 -m pytest -v

init: clean deps