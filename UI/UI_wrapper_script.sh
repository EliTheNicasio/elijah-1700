#!/bin/bash

# run waved host
./waved &

# run python UI
wave run --no-reload --no-autostart UI.py &

wait -n

exit $?

