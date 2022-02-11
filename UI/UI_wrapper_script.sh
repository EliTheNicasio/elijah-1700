#!/bin/bash

set -m

./wave/waved -web-dir "/wave/www"&

python3 /usr/src/app/UI.py&

fg %1
