#!/usr/bin/env bash

python3 -m venv venv

cd venv || exit

source bin/activate

pip install pandas
pip install matplotlib
pip install scipy
pip install scikit-learn