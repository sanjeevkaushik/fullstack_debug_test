import sqlite3

conn = sqlite3.connect('feedback.db')
with open('feedbackSchema.sql', 'r') as f:
    cursor = conn.cursor()
    cursor.executescript(f.read())
    conn.commit()
    cursor.close()