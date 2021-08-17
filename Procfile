release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py runscript tasks

web: gunicorn lottocomboapi.wsgi