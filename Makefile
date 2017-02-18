SETUP=setup.py
PACKAGE=pwcm
README=README.md

all: build_ext

clean:
	rm -rf build dist pwcm.egg-info __pycache__ *.pyc pwcm/*.pyc pwcm/*.so pwcm/__pycache__

build_ext: clean
	python $(SETUP) build_ext --inplace

test: build_ext
	python -m $(PACKAGE)

readme: $(README)
	pandoc -f markdown README.md -t rst > README.rst

wheel: build_ext
	python $(SETUP) bdist_wheel
