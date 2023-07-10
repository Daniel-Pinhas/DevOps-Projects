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
        'host': '192.168.59.103',
        'port': '30300',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT url FROM alpacas')
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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    
