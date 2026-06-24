# app.py

# Flask — the web framework that handles HTTP requests and responses
# request — lets us read data sent by the client (e.g. JSON body)
# jsonify — converts Python dicts/lists into proper JSON responses
# redirect — tells the browser to go to a different URL (302 response)
from flask import Flask, request, jsonify, redirect

# Importing all the database functions we need from database.py
# Keeping database logic separate from route logic is intentional —
# each file has one responsibility
from database import init_db, save_link, generate_code, get_link, get_all_links, code_exists

# Creates the Flask application instance
# __name__ tells Flask where to find the project files
app = Flask(__name__)

# Runs once when the server starts — creates the database table if it doesn't exist yet
init_db()


# The root route — just confirms the server is running
# Useful for health checks (making sure the API is alive)
@app.route("/")
def hello_world():
    return "URL Shortener is running"


# POST /shorten — takes a long URL and returns a unique short code
# Steps:
#   1. Read the JSON body from the request
#   2. Validate that a URL was actually provided
#   3. Generate a code, keep regenerating if it already exists (collision safety)
#   4. Save the code + URL to the database
#   5. Return the code — 201 means "Created", something new was successfully saved
@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")  # .get() returns None safely if "url" key is missing
    if not original_url:
        return jsonify({"error": "URL is required"}), 400  # 400 = Bad Request

    code = generate_code()
    while code_exists(code):       # keep trying until we find a code nobody else has
        code = generate_code()

    save_link(code, original_url)
    return jsonify({"code": code}), 201


# GET /<code> — redirects the user to the original URL
# <code> is a dynamic URL parameter — Flask extracts it and passes it into the function
# If the code exists: redirect (302) sends the browser to the original URL
# If not: return 404 (Not Found) with a clear error message
@app.route("/<code>")
def redirect_url(code):
    original_url = get_link(code)
    if not original_url:
        return jsonify({"error": "Link not found"}), 404
    return redirect(original_url)


# GET /links — returns every saved link as a JSON array
# Useful for building an admin dashboard or debugging
# Each item is a dict with "code" and "url" keys for clarity
@app.route("/links")
def links():
    link = get_all_links()
    return jsonify(link)


# Only starts the development server if this file is run directly
# debug=True means the server restarts automatically when you save changes
# and shows detailed error messages — never use debug=True in production
if __name__ == "__main__":
    app.run(debug=True)