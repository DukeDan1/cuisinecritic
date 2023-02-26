#!/bin/bash
while true; do
    echo "Starting server..."
    python3 CuisineCritic/manage.py runserver 12000
    echo "Server exited with code $?. Respawning.." >&2
    sleep 5
done