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
