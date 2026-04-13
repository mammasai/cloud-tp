from flask import Flask, request, jsonify
import sqlite3
import os
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# SQL
conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# MongoDB
client = MongoClient(os.environ.get("MONGO_URI"))
#client = MongoClient("mongodb+srv://mammasai4_db_user:naYXo1MHkuLYUQTF@cluster0.omjynio.mongodb.net/testdb?retryWrites=true&w=majority")
db = client["testdb"]
collection = db["users"]

@app.route("/")
def home():
    return "Backend is running"

@app.route("/add_sql", methods=["POST"])
def add_sql():
    name = request.json["name"]
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    return jsonify({"msg": "Added to SQL"})

@app.route("/add_nosql", methods=["POST"])
def add_nosql():
    name = request.json["name"]
    collection.insert_one({"name": name})
    return jsonify({"msg": "Added to NoSQL"})

#app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)