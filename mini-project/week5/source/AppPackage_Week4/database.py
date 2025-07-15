from dotenv import load_dotenv
import os
import psycopg2 as psycopg

# load enviroments variable from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")


def database_fetch_function(table):
    try:
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password,
        ) as connection:

            cursor = connection.cursor()

        if table == "products":
            column_0 = 'product_id'
            column_1 = 'product_name'
            column_2 = 'product_price'
            table_name = 'products'
        elif table == "couriers":
            column_0 = 'courier_id'
            column_1 = 'courier_name'
            column_2 = 'courier_phone_number'   
            table_name = 'couriers'         

        cursor.execute(f'SELECT {column_0},{column_1}, {column_2} from {table_name}')
        rows = cursor.fetchall()
    except Exception as ex:
        print("Failed to:", ex)
    return rows    

def database_send_function(table,input1,input2):
    try:
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password,
        ) as connection:

            cursor = connection.cursor()

        if table == "products":
            column_1 = 'product_name'
            column_2 = 'product_price'
            table_name = 'products'
        elif table == "couriers":
            column_1 = 'courier_name'
            column_2 = 'courier_phone_number'   
            table_name = 'couriers'     

        values = f'{input1},{input2}'

        cursor.execute(f'INSERT INTO {table_name} ({column_1}, {column_2}) Values ({values})',({column_1},{column_2}))
        rows = cursor.fetchall()
    except Exception as ex:
        print("Failed to:", ex)
    return rows 

