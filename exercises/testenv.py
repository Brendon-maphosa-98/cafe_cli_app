orders = [{'order1': {
    "customer_name": "Alice Smith",
    "customer_address": "High Road, MANCHESTER",
    "customer_phone": "07123456789",
    "status": "ready for pickup",
    "item(s)_ordered": ["Latte", "Blueberry Muffin"]
}},{'order2': {
    "customer_name": "James Carter",
    "customer_address": "Oak Street, LIVERPOOL",
    "customer_phone": "07234567890",
    "status": "preparing",
    "item(s)_ordered": ["Flat White", "Croissant"]
}},{'order3': {
    "customer_name": "Laura Green",
    "customer_address": "Maple Avenue, SHEFFIELD",
    "customer_phone": "07345678901",
    "status": "delivered",
    "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"]
    }}]

x = list(orders[1].keys())
print(x)