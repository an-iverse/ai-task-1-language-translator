# Task 1 — Language Translation Tool

This Flask web application lets a user choose a source and target language, send text to the MyMemory Translation API, and see/copy the translated result.

## Run it

1. Install Python 3.11 or newer from https://www.python.org/downloads/ (tick **Add Python to PATH**).
2. In this folder, open PowerShell and run:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   flask --app app run
   ```
3. Open `http://127.0.0.1:5000` in a browser.

## Demonstration checklist

- Select English → Hindi, type `Good morning`, and click Translate.
- Show the returned result and Copy button.
- Explain that the browser sends JSON to Flask, and Flask calls the API securely on the server side.

## Notes

The MyMemory endpoint is a public API intended for modest demos. Internet access is required. Set the optional `MYMEMORY_EMAIL` environment variable to your own email for a higher public quota.
