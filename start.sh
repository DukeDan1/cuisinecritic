#!/bin/bash
while true; do
    if [ $1 == "pythonanywhere" ]; then
        echo "Starting pythonanywhere server..."
        python3 CuisineCritic/manage.py runserver 0.0.0.0:8000
    else
        echo "Starting local server..."
        python3 CuisineCritic/manage.py runserver 12000
    fi
    echo "Server exited with code $?. Respawning.." >&2
    sleep 5
done