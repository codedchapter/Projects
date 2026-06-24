# URL Shortener Project

A beginner-friendly URL shortening service built with Flask and SQLite.

## What this project does

- Provides a web endpoint to shorten long URLs into short codes.
- Redirects short codes back to the original URL.
- Stores links in a local SQLite database.

## Files in this project

- `app.py` — the Flask application and API routes.
- `database.py` — database setup and helper functions.
- `requirements.txt` — Python dependencies for the project.

## How to use it

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

3. Open the app in your browser or use an API tool like Postman.

## Available routes

- `GET /` — confirms the server is running.
- `POST /shorten` — accepts JSON with a `url` field and returns a short code.
- `GET /<code>` — redirects the browser to the original URL.
- `GET /links` — returns all saved short links.

## Example

Request:

```bash
curl -X POST http://127.0.0.1:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

Response:

```json
{ "code": "a1B2c3" }
```

Then open:

```bash
http://127.0.0.1:5000/a1B2c3
```

## 

- `requirements.txt` has the libraries need.
- `app.py` starts the web server and handles requests.
- `database.py` keeps the data safe in `links.db`.