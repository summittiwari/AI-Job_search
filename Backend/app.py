# Entry point for backend API
from flask import Flask
import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

@app.route('/')
def home():
    return "AI Job Platform Backend Running"

@app.route('/test-db')
def test_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Database connected: {db_version[0]}"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
