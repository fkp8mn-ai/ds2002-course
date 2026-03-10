import requests
import mysql.connector
import os
from datetime import datetime

def connect_db():
    db = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSER"),
        password=os.getenv("DBPASS"),
        database="iss"
    )
    return db

def extract():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    return data


def register_reporter(table, reporter_id, reporter_name):

    db = connect_db()
    cursor = db.cursor()

    try:
        query = f"SELECT * FROM {table} WHERE reporter_id = %s"
        cursor.execute(query, (reporter_id,))
        result = cursor.fetchone()

        if result is None:
            insert_query = f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)"
            cursor.execute(insert_query, (reporter_id, reporter_name))
            db.commit()
            print("Reporter registered.")

        else:
            print("Reporter already exists.")

    except Exception as e:
        print("Database error:", e)

    finally:
        cursor.close()
        db.close()

def load(data, reporter_id):

    db = connect_db()
    cursor = db.cursor()

    try:
        message = data["message"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        timestamp = datetime.fromtimestamp(data["timestamp"])
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        insert_query = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (message, latitude, longitude, timestamp, reporter_id))
        db.commit()

        print("Location inserted.")

    except Exception as e:
        print("Insert error:", e)

    finally:
        cursor.close()
        db.close()

def main():

    reporter_id = "fkp8mn"
    reporter_name = "Giovanna Bonner"

    register_reporter("reporters", reporter_id, reporter_name)

    data = extract()

    load(data, reporter_id)


if __name__ == "__main__":
    main()
