# database.py

# Three built-in Python libraries:
# sqlite3 — lets us create and query a local database stored as a single file
# random — lets us pick random characters for generating short codes
# string — gives us ready-made collections of characters (letters, digits)
import sqlite3
import random
import string


# Opens a connection to the database file "links.db"
# If links.db doesn't exist yet, SQLite creates it automatically
# Returns the connection object so other functions can use it
def get_connection():
    conn = sqlite3.connect("links.db")
    return conn


# Creates the "links" table when the app first starts up
# IF NOT EXISTS means it runs silently on every startup —
# only actually creates the table the very first time
# The table has two columns:
#   code — the short random string (e.g. "aB3dE9"), must be unique (PRIMARY KEY)
#   original_url — the full long URL, cannot be empty (NOT NULL)
def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS links (
            code TEXT PRIMARY KEY,
            original_url TEXT NOT NULL
        )
    """)
    conn.commit()   # saves the table creation permanently to the file
    conn.close()    # closes the connection, we're done here


# Generates a random 6-character short code like "xK9mP2"
# string.ascii_letters gives us all letters a-z and A-Z (52 characters)
# string.digits gives us 0-9 (10 characters)
# Combined pool = 62 possible characters per position
# random.choices picks 6 characters randomly from that pool (with repetition allowed)
# ''.join() glues the list ['x','K','9','m','P','2'] into one string "xK9mP2"
def generate_code():
    pool = string.ascii_letters + string.digits
    return ''.join(random.choices(pool, k=6))


# Saves a new code + original_url pair into the links table
# The ? placeholders are intentional — never put variables directly in SQL strings
# because that opens a security hole called SQL injection
# We pass the actual values separately as a tuple: (code, original_url)
# commit() saves the new row permanently, close() frees the connection
def save_link(code, original_url):
    conn = get_connection()
    conn.execute(
        "INSERT INTO links (code, original_url) VALUES (?, ?)",
        (code, original_url)
    )
    conn.commit()
    conn.close()


# Looks up a code in the database and returns the original URL
# fetchone() returns one row as a tuple e.g. ("https://google.com",)
# or None if no row matches that code
# We return result[0] to get just the URL string, not the whole tuple
# We close BEFORE returning — anything after return never executes
def get_link(code):
    conn = get_connection()
    result = conn.execute(
        "SELECT original_url FROM links WHERE code = ?",
        (code,)
    ).fetchone()
    conn.close()
    if result:
        return result[0]
    return None


# Returns every saved link as a list of dicts — e.g.:
# [{"code": "aB3dE9", "url": "https://google.com"}, ...]
# fetchall() returns all rows as a list of tuples
# The list comprehension loops through each tuple and builds a named dict
# This shape is better than raw tuples because API consumers know what each field means
def get_all_links():
    conn = get_connection()
    result = conn.execute("SELECT code, original_url FROM links").fetchall()
    conn.close()
    return [{"code": row[0], "url": row[1]} for row in result]


# Checks whether a code already exists in the database
# Returns True if found, False if not
# Used before saving a new link to avoid collisions —
# two different links must never share the same code
def code_exists(code):
    conn = get_connection()
    result = conn.execute(
        "SELECT original_url FROM links WHERE code = ?",
        (code,)
    ).fetchone()
    conn.close()
    if result:
        return True
    return False