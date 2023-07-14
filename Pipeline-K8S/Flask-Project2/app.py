from typing import List, Dict
from flask import Flask, render_template
import os
import random
import mysql.connector

app = Flask(__name__)

def get_random_url() -> str:
    config = {
        'user': 'root',
        'password': 'daniel',
        'host': os.environ.get("MYSQL_HOST"),
        'port': os.environ.get("MYSQL_PORT"),
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT url FROM classmate')
    urls = cursor.fetchall()
    cursor.close()
    connection.close()
    if urls:
        return random.choice(urls)[0]
    return None


@app.route("/")
def index():
    url = get_random_url()
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("FLASK_PORT", 5000)))
