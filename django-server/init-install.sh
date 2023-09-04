
source ../.env # load the environment variables
poetry install
# desc: populate the database with the initial data
poetry run python manage.py makemigrations 
poetry run python manage.py migrate --fake-initial ## for the first time

