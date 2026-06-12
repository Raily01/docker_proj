from flask import Flask
import psycopg2
import time

app = Flask(__name__)

#просто базовое приложение
def connect_db():
    while True:
        try:
            connection = psycopg2.connect(
                host="postgres_db",
                database="shop_db",
                user="reylife",
                password="admin123"
            )
            return connection

        except Exception as e:
            print("Waiting database...", e)
            time.sleep(5)

@app.route("/products")
def get_products():

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    result = ""

    for item in data:
        result += f"{item}<br>"

    conn.close()

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)