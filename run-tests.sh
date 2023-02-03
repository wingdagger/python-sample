#!/bin/bash

pip install -r requirements.txt
pip install pytest
pip install ./dist/python_sample-0.0.1-py3-none-any.whl
pytest 