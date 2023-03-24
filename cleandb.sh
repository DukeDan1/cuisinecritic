if [ -f CuisineCritic/db.sqlite3 ]; then
    rm CuisineCritic/db.sqlite3
fi

python CuisineCritic/manage.py makemigrations
python CuisineCritic/manage.py migrate
python CuisineCritic/manage.py migrate --run-syncdb
python CuisineCritic/population_script.py