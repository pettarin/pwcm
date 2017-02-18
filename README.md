# pwcm

A minimal working example of C++ function multiversioning in Python wheels.

* Date: 2017-02-18
* Version: 0.0.1
* Developer: [Alberto Pettarin](http://www.albertopettarin.it/)
* License: the MIT License (MIT)
* Contact: [click here](http://www.albertopettarin.it/contact.html)


## Overview

This repository contains a simple
Python 2.7/3.5+ package named ``pwcm``
that has a C++ extension (``pwcm.cext``) containing
[function multiversioning](https://gcc.gnu.org/wiki/FunctionMultiVersioning).
See also [this article](https://lwn.net/Articles/691932/).

The basic goal consists in testing the possibility of creating
a single Python wheel supporting CPUs with different features,
e.g. SSE3 vs SSE4.1/SSE4.1 vs AVX.
See this [PyTorch issue](https://github.com/pytorch/pytorch/issues/535).

So far, it seems to work as expected:

| Machine | CPU                                | Flags  | pwcm Output | Correct? | Compiler | Date       |
|---------|------------------------------------|--------|-------------|----------|----------|------------|
| laptop1 | Intel(R) Core(TM) i5-6200U         | SSE4.2 | SSE4.2      | Y        | GCC 6    | 2017-02-18 |
| vps1    | AMD Athlon(tm) II X2 240 Processor | SSE4a  | SSE4a       | Y        | GCC 6    | 2017-02-18 |


## Installation from source

```bash
$ virtualenv venv
$ cd venv
$ source bin/activate
$ git clone https://github.com/pettarin/pwcm
$ cd pwcm
$ make
$ make test
$ deactivate
```

The last line of the output should be something like:

```plain
[INFO] C++ extension returned the known value: SSE4.2
```


## Create a Python wheel

```bash
$ # in the pwcm root directory, the one containing README.md
$ make wheel
$ # look inside the dist/ directory
$ # the name of the .whl file depends on python version
$ ls dist/
pwcm-0.0.1-cp27-cp27mu-linux_x86_64.whl
```


## Installation from a wheel file

```bash
$ # create a new virtualenv
$ virtualenv venvtest
$ cd venvtest
$ source bin/activate
$ # download/copy the .whl file here
$ # adjust the name depending on your platform
$ pip install pwcm-0.0.1-cp27-cp27mu-linux_x86_64.whl
$ python -m pwcm
$ deactivate
```

Again, it should print something like:

```plain
[INFO] C++ extension returned the known value: SSE4.2
```


## Clean

```bash
$ # in the pwcm root directory, the one containing README.md
$ make clean
$ # in case you installed with pip
$ pip uninstall pwcm
```


## License

The contents of this repository are released
under the terms of the MIT License.
