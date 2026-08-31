from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=5432
    )

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "message": "Connected to PostgreSQL!",
        "postgres_version": result[0]
    }

@app.route("/health")
def health():
    return "OK", 200

app.run(host="0.0.0.0", port=5000)
