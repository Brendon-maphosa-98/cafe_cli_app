from dotenv import load_dotenv
import os
import psycopg2 as psycopg

# load enviroments variable from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

try:
    with psycopg.connect(
        host=host_name,
        dbname=database_name,
        user=user_name,
        password=user_password,
    ) as connection:

        curser = connection.cursor()

        Sql = """INSERT INTO products (product_name, product_price)
VALUES 
    ('Espresso', 3.99),
    ('Cappuccino', 4.5),
    ('Latte', 3.75),
    ('Americano', 4.3),
    ('Mocha', 2.0),
    ('Iced Coffee', 3.45),
    ('Flat White', 4.25),
    ('Cold Brew', 2.5),
    ('Croissant', 1.99),
    ('French Toast', 3.0)
RETURNING product_id, product_name, product_price;

"""
        data_values = ("product_name", "product_price")

        curser.execute(Sql,data_values)
except Exception as ex:
    print("Failed to:", ex)
