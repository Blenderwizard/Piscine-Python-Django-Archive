#!/bin/sh

python3 -m venv django_venv
source django_venv/bin/activate
python3 -m pip install --log pip_log_$(echo $(date +%s)).log --upgrade --disable-pip-version-check --force-reinstall -r requirement.txt