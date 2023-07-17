from flask import Flask, render_template
import os
import random
import mysql.connector
import boto3
from botocore.exceptions import ClientError
import json

app = Flask(__name__)

def get_secret():
    secret_name = "MySQL-Gifs-Secret"
    region_name = "us-east-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return secret

def get_random_url() -> str:
    try:
        secret = get_secret()
        secret_dict = json.loads(secret)
        db_username = secret_dict["username"]
        db_password = secret_dict["password"]
        db_host = 'rds-gifs-db.cih3afqd7fge.us-east-2.rds.amazonaws.com'
        db_port = 3306
        db_name = 'devopsroles'

        config = {
            'user': db_username,
            'password': db_password,
            'host': db_host,
            'port': db_port,
            'database': db_name
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
