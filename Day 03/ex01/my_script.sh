#!/bin/sh

python3 -m pip -V 
if python3 -m pip install --target=local_lib git+https://github.com/jaraco/path.git --log pip_log_$(echo $(date +%s)).log --upgrade --disable-pip-version-check; then
	python3 my_program.py
else
	echo "Error In Install"
fi