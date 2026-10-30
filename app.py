"""Task 1: a beginner-friendly language translation web application."""
import os

import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# MyMemory is a public translation API suitable for a small academic demo.
# You can set MYMEMORY_EMAIL to your email to use its larger daily quota.
API_URL = "https://api.mymemory.translated.net/get"


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/translate")
def translate():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    source = str(data.get("source", "en")).strip()
    target = str(data.get("target", "hi")).strip()

    if not text:
        return jsonify(error="Please enter text to translate."), 400
    if source == target:
        return jsonify(translated_text=text)

    params = {"q": text, "langpair": f"{source}|{target}"}
    email = os.getenv("MYMEMORY_EMAIL")
    if email:
        params["de"] = email

    try:
        response = requests.get(API_URL, params=params, timeout=15)
        response.raise_for_status()
        result = response.json()
        translated = result.get("responseData", {}).get("translatedText")
        if not translated:
            raise ValueError("The translation service returned no text.")
        return jsonify(translated_text=translated)
    except (requests.RequestException, ValueError) as error:
        return jsonify(error=f"Translation could not be completed: {error}"), 502


if __name__ == "__main__":
    app.run(debug=True)
