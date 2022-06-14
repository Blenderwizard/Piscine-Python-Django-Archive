#!/bin/sh

python3 -m venv .
pg_ctl restart
source ./bin/activate
python3 -m pip install --log pip_log_$(echo $(date +%s)).log --upgrade --disable-pip-version-check --force-reinstall -r requirements.txt