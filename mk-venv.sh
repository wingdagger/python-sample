#!/bin/bash

VENV=venv
rm -fr $VENV
python -m venv $VENV
pip install -r requirements.txt
