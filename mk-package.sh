#!/bin/bash

pip install setuptools wheel
rm -fr build dist src/python_sample.egg-info
python setup.py sdist bdist_wheel