echo "waiting for postgres"
./wait-for db:5432

echo "migrating database"
python manage.py migrate

echo "starting server"
python manage.py runserver 0.0.0.0:8000