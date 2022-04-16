# mangapy
Manga translation tool

# Usage google_vision

Create a credentials json file and export the following environment variable:

```
export GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

The current google_vision script expects to have a local file called "18.png"
which will upload to Google vision API to recognize:

```
python google_vision.py
```


# Django
## Start && Stop:
For starting the project:
```
make start
```

For stopping containers or `ctrl+C`:
```
make stop
```

For further useful commands check the `Makefile`

## Creating a superuser to login inside the Django Admin:
1. `make bash c=web` -> It will open a shell inside the `web` container
2. Then run normally the `createsuperuser` command like this:
   - `python manage.py createsuperuser`