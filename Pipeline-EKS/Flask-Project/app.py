from flask import Flask, render_template
import os
import random
import mysql.connector
import boto3
import json
import logging
from botocore.exceptions import ClientError

def get_secret():

    secret_name = "mysql-gifs-rds"
    region_name = "us-east-2"

    # Create a Secrets Manager client
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
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    return secret

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

def get_random_url() -> str:
    try:
        # Load the database credentials from the secret
        secret = get_secret()
        db_credentials = json.loads(secret)

        config = {
            'user': db_credentials['username'],
            'password': db_credentials['password'],
            'host': 'rds-gifs-db.cih3afqd7fge.us-east-2.rds.amazonaws.com',
            'port': '3306',
            'database': 'devopsroles'
        }

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Execute the query to retrieve URLs from the database
        cursor.execute('SELECT url FROM dogs')
        urls = cursor.fetchall()

        cursor.close()
        connection.close()

        # If URLs are found in the database, return a random URL
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