import json
import psycopg2
import os

print('Loading function')


def lambda_handler(event, context):
    id = event['id']
    ip = event['ip']
    flag = event['flag']

    try:
        connection = psycopg2.connect(
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port="5432",
            database=os.environ['DB_NAME']
        )

        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS proactive (id TEXT, ip TEXT, flag boolean)")

        if flag == True:
            cursor.execute("UPDATE proactive SET ip = %s WHERE id = %s", (ip, id))
            return True

        elif flag == False:
            cursor.execute("INSERT INTO proactive (id, ip, flag) VALUES (%s, %s, %s)", (id, ip, flag))
            # cursor.execute("SELECT * FROM proactive")
            # results = cursor.fetchall()

            # print("Query results:", results)
            return True

    except (Exception, psycopg2.Error) as error:
        print("Error: ", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
    return False

