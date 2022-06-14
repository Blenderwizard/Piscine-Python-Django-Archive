#!/bin/sh

curl -s $1 | grep -oE --color=never "<a href=\"[^\"]*" | cut -c 10-