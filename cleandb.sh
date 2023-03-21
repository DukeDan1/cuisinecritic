rm CuisineCritic/db.sqlite3
python CuisineCritic/manage.py makemigrations
python CuisineCritic/manage.py migrate
python CuisineCritic/manage.py migrate --run-syncdb
python CuisineCritic/populate.py