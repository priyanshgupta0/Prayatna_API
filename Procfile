web: gunicorn hackathon_api.wsgi:application --log-file - --log-level debug
release: python ./hackathon_api/manage.py makemigrations hackathon && python ./hackathon_api/manage.py migrate hackathon