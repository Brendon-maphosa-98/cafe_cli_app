import data_module as data
import input_output_module as io

# Add new order function


def add_order(orderlist, cust_fname, cust_sname, cust_street, cust_city, cust_num):
    customer_name1 = input(cust_fname)
    customer_name2 = input(cust_sname)
    customer_address1 = input(cust_street)
    customer_address2 = input(cust_city)
    customer_number = input(cust_num)
    temp_order_list = orderlist
    order = {
        f"{len(data.orders) + 1}": {
            "customer_name": f"{customer_name1.capitalize()} {customer_name2.capitalize()}",
            "customer_address": f"{customer_address1.title()} {customer_address2.upper()}",
            "customer_phone": customer_number,
            "status": f"{data.order_status[0]}",
        }
    }
    temp_order_list.append(order)
    return temp_order_list


# function for updating an existing order


def update_existing_order():
    io.list_output(data.orders)


update_existing_order()
