products = []


orders = [
    {
        "order1": {
            "customer_name": "Alice Smith",
            "customer_address": "High Road, MANCHESTER",
            "customer_phone": "07123456789",
            "status": "ready for pickup",
            "courier": "John",
            "item(s)_ordered": ["Latte", "Blueberry Muffin"],
        }
    },
    {
        "order2": {
            "customer_name": "James Carter",
            "customer_address": "Oak Street, LIVERPOOL",
            "customer_phone": "07234567890",
            "status": "preparing",
            "courier": "Alice",
            "item(s)_ordered": ["Flat White", "Croissant"],
        }
    },
    {
        "order3": {
            "customer_name": "Laura Green",
            "customer_address": "Maple Avenue, SHEFFIELD",
            "customer_phone": "07345678901",
            "status": "delivered",
            "courier": "Michael",
            "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"],
        }
    },
]

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]

couriers = []

## Persistence functions

# ingestion function
def ingest_function(prodlist,courlist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    with open("/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week3/data/products2.txt", 'r') as read_object:
        pass
    with open("/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week3/data/couriers2.txt", 'r') as read_object:
        pass
