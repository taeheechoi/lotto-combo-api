release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py runscript tasks --no-input

web: gunicorn lottocomboapi.wsgi