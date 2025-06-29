from contextlib import nullcontext

# app.py - Mock Flask backend (with bugs)
from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
@app.route("/feedback", methods=["GET"])
def get_feedback():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()

    rating = request.args.get("rating")
    sort = request.args.get("sort", "desc")
    query = "SELECT message, rating FROM feedback"

    print(rating)
    if rating != "null":
        query += f" WHERE rating = ? "  # <-- Prepared statement
    query += f" ORDER BY created_at {sort}"
    print(query)
    if rating != "null":
        feedback = cursor.execute(query, rating).fetchall()
    else:
        feedback = cursor.execute(query).fetchall()
    conn.close()
    return jsonify(feedback)

@app.route("/feedback", methods=["POST"])
def post_feedback():
    data = request.get_json()
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (message, rating) VALUES (?, ?)", (data["message"], data["rating"]))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(port=5000)