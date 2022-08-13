.PHONY: all test coverage dist upload clean doc deps

all:
	@echo "Usage: make [deps|deps-dev|test|dist|upload|release|clean]"
	@exit 1

deps:
	pip install -e .

deps-dev: deps
	pip install -r requirements-dev.txt

test:
	cd tests ; python -m pytest .

version-test:

#
##

## Formatting
#  ==========

format:
	yapf -vv -i --style=.style.yapf --recursive termscraper/

format-test:
	yapf -vv --style=.style.yapf --diff --recursive termscraper/
#
##

## Packaging and clean up
#  ======================

dist:
	rm -Rf dist/ build/ *.egg-info
	python setup.py sdist bdist_wheel
	rm -Rf build/ *.egg-info

upload: dist version-test
	twine upload dist/*.tar.gz dist/*.whl

# Describe the HEAD and if it is not a tag, fail; othewise get
# the annotation of the tag and ensure that the indentation is removed
# from it (tail + sed) and then create a Github release with that.
release:
	gh auth status
	@X=`git describe --exact-match HEAD` && ( git tag -n1000 "$$X" | tail -n +3 | sed 's/^[[:blank:]]\{,4\}\(.*\)$$/\1/' | tee .release-notes | gh release create --generate-notes "$$X" --notes-file - )
	@cat .release-notes

clean:
	rm -f .coverage .coverage.work.* .release-notes .workflow-log
	rm -Rf dist/ build/ *.egg-info
	rm -Rf build/ *.egg-info
	find . -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -f README.rst prof-traces

#
##
