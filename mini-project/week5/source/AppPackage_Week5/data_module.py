import csv
from dotenv import load_dotenv
import os
import psycopg2 as psycopg

products = []

orders = []

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]

couriers = []

## Persistence functions


# ingestion function
def ingest_function(prodlist, courlist, orderslist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    temp_orders_list = orderslist
    with open(
        "mini-project/week5/data/products3.csv",
        "r",
    ) as read_object:
        for row in csv.DictReader(read_object):
            temp_prod_list.append({"name": row["name"], "price": float(row["price"])})
    prodlist = temp_prod_list
    with open(
        "mini-project/week5/data/couriers3.csv",
        "r",
    ) as read_object:
        for row in csv.DictReader(read_object):
            temp_cour_list.append(
                {"name": row["name"], "phone_number": row["phone_number"]}
            )
    courlist = temp_cour_list
    with open(
        "mini-project/week5/data/orders3.csv",
        "r",
    ) as read_object:
        for row in csv.DictReader(read_object):
            temp_orders_list.append(
                {
                    int(row["order_num"]): {
                        "customer_name": row["customer_name"],
                        "customer_address": row["customer_address"],
                        "customer_phone": row["customer_phone"],
                        "courier": row["courier"],
                        "status": row["status"],
                        "items": row["items"],
                    }
                }
            )
    orderslist = temp_orders_list


# persistence function
def persistence_function(prodlist, courlist, orderslist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    temp_orders_list = orderslist
    with open(
        "mini-project/week5/data/products3.csv",
        "w",
    ) as write_object:
        fieldnames = ["name", "price"]
        csv.DictWriter(write_object, fieldnames=fieldnames).writeheader()
        for product in temp_prod_list:
            csv.DictWriter(write_object, fieldnames=fieldnames).writerow(product)
    with open(
        "mini-project/week5/data/couriers3.csv",
        "w",
    ) as write_object:
        fieldnames = ["name", "phone_number"]
        csv.DictWriter(write_object, fieldnames=fieldnames).writeheader()
        for courier in temp_cour_list:
            csv.DictWriter(write_object, fieldnames=fieldnames).writerow(courier)
    with open(
        "mini-project/week5/data/orders3.csv",
        "w",
    ) as write_object:
        fieldnames = [
            "order_num",
            "customer_name",
            "customer_address",
            "customer_phone",
            "courier",
            "status",
            "items",
        ]
        csv.DictWriter(write_object, fieldnames=fieldnames).writeheader()
        for dictionary in temp_orders_list:
            for key, value in dictionary.items():
                new_row = {
                    "order_num": key,
                    "customer_name": value["customer_name"],
                    "customer_address": value["customer_address"],
                    "customer_phone": value["customer_phone"],
                    "courier": value["courier"],
                    "status": value["status"],
                    "items": value["items"],
                }
                csv.DictWriter(write_object, fieldnames=fieldnames).writerow(new_row)


## Database functions and code so that the app can move from local data files to working with databases

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
            column_0 = "product_id"
            column_1 = "product_name"
            column_2 = "product_price"
            table_name = "products"
        elif table == "couriers":
            column_0 = "courier_id"
            column_1 = "courier_name"
            column_2 = "courier_phone_number"
            table_name = "couriers"

        cursor.execute(f"SELECT {column_0},{column_1}, {column_2} from {table_name}")
        rows = cursor.fetchall()
    except Exception as ex:
        print("Failed to:", ex)
    return rows


def database_send_function(table, input1, input2):
    try:
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password,
        ) as connection:

            cursor = connection.cursor()

        if table == "products":
            column_0 = "product_id"
            column_1 = "product_name"
            column_2 = "product_price"
            table_name = "products"
        elif table == "couriers":
            column_0 = "courier_id"
            column_1 = "courier_name"
            column_2 = "courier_phone_number"
            table_name = "couriers"

        values = f"'{input1}','{input2}'"

        cursor.execute(
            f"INSERT INTO {table_name} ({column_1}, {column_2}) Values ({values}) RETURNING {column_0},{column_1},{column_2}",
            ({column_1}, {column_2}),
        )
        connection.commit()
    except Exception as ex:
        print("Failed to:", ex)
