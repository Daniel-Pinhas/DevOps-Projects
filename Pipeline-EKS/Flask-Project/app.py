from flask import Flask, render_template
import os
import random
import mysql.connector

app = Flask(__name__)

def get_random_url() -> str:
    try:
        config = {
            'user': 'daniel2',
            'password': 'daniel2',
            'host': 'rds-gifs-db.cih3afqd7fge.us-east-2.rds.amazonaws.com',
            'port': '3306',
            'database': 'devopsroles'
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT url FROM dogs')
        urls = cursor.fetchall()
        cursor.close()
        connection.close()
        if urls:
            return random.choice(urls)[0]
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
    return None

@app.route("/")
def index():
    url = get_random_url()
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
