#!/bin/bash

./waved &

wave run --no-reload --no-autostart UI.py &

wait -n

exit $?

