
source .env # load the environment variables

# desc: populate the database with the initial data
python manage.py makemigrations
python manage.py makemigrations apiApp
# python manage.py migrate 
python manage.py migrate --run-syncdb ## for the first time

# # echo $DJANGO_SUPERUSER_USERNAME
# # echo $DJANGO_SUPERUSER_EMAIL
# # echo $DJANGO_SUPERUSER_PASSWORD
# # desc: create a superuser
# python manage.py createsuperuser --noinput \
#     --username $DJANGO_SUPERUSER_USERNAME \
#     --email $DJANGO_SUPERUSER_EMAIL
    

# # desc: populate the database with the initial data
# python manage.py makemigrations
# # python manage.py migrate 
# python manage.py migrate --run-syncdb ## for the first time