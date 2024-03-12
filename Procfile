worker: gunicorn hackathon_api.wsgi:application --log-file - --log-level debug
release: python manage.py makemigrations && python manage.py migrate