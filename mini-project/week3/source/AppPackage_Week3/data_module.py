products = [
    "Espresso",
    "Cappuccino",
    "Latte",
    "Americano",
    "Mocha",
    "Iced Coffee",
    "Flat White",
    "Cold Brew",
    "Croissant",
    "Blueberry Muffin",
]

orders = [
    {
        "order1": {
            "customer_name": "Alice Smith",
            "customer_address": "High Road, MANCHESTER",
            "customer_phone": "07123456789",
            "status": "ready for pickup",
            "courier": None,
            "item(s)_ordered": ["Latte", "Blueberry Muffin"],
        }
    },
    {
        "order2": {
            "customer_name": "James Carter",
            "customer_address": "Oak Street, LIVERPOOL",
            "customer_phone": "07234567890",
            "status": "preparing",
            "courier": None,
            "item(s)_ordered": ["Flat White", "Croissant"],
        }
    },
    {
        "order3": {
            "customer_name": "Laura Green",
            "customer_address": "Maple Avenue, SHEFFIELD",
            "customer_phone": "07345678901",
            "status": "delivered",
            "courier": None,
            "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"],
        }
    },
]

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]

couriers = [
    "John",
    "Alice",
    "Michael",
    "Sophie",
    "David",
    "Emma",
    "Liam",
    "Olivia",
    "Noah",
    "Chloe",
]
