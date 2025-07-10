import csv

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
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/products3.csv",
        "r",
    ) as read_object:
        for row in csv.DictReader(read_object):
            temp_prod_list.append({"name": row["name"], "price": row["price"]})
    prodlist = temp_prod_list
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/couriers3.csv",
        "r",
    ) as read_object:
        for row in csv.DictReader(read_object):
            temp_cour_list.append({"name": row["name"], "phone_number": row["phone_number"]})
    prodlist = temp_cour_list
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/orders3.csv",
        "r",
    ) as read_object:
        for row in csv.DictReader(read_object):
            temp_orders_list.append(
                {
                    f"order{row["order_num"]}": {
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
def persistence_function(prodlist,courlist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/products3.csv",
        "w",
    ) as write_object:
        fieldnames = ["name", "price"]
        csv.DictWriter(write_object,fieldnames=fieldnames).writeheader()
        for product in temp_prod_list:
            csv.DictWriter(write_object,fieldnames=fieldnames).writerow(product)
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/couriers3.csv",
        "w",
    ) as write_object:
        fieldnames = ["name", "phone_number"]
        csv.DictWriter(write_object,fieldnames=fieldnames).writeheader()
        for courier in temp_cour_list:
            csv.DictWriter(write_object,fieldnames=fieldnames).writerow(courier)
    # with open(
    #     "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/orders3.csv",
    #     "r",
    # ) as write_object:
    #     fieldnames = [
    #         "order_num",
    #         "customer_name",
    #         "customer_address",
    #         "customer_phone",
    #         "courier",
    #         "status",
    #         "items",
    #     ]
    #     pass


ingest_function(products,couriers,orders)

persistence_function(products,couriers)
print('')
print(couriers)