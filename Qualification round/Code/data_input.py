## File to take data input from file

# Take file input and convert each item to ints and create list that holds each line a sepearte list.



def main(file_name):
    file = open(file_name, "r")

    file_object = file.read()

    file_split_line = file_object.splitlines()

    # Split variable in lines

    list_file_inputs_lists_lines = []


    for line in file_split_line:
        new_line = []
        line = line.split()
        for i in line:
            new_line.append(int(i))
        list_file_inputs_lists_lines.append(new_line)

    # print(list_file_inputs_lists_lines)


    ## Take grid input

    senario_layout = list_file_inputs_lists_lines[0]
    # print(senario_layout)

    ## Number of products and weights

    no_products = list_file_inputs_lists_lines[1][0]

    product_weights = list_file_inputs_lists_lines[2]


    ## Number of warehouse, locations and stocks


    no_warehouses = list_file_inputs_lists_lines[3][0] # Take first time from list at position 3
    # print(no_warehouses)

    start_wharehouse_range = 3 + 1
    end_wharehouse_range = (start_wharehouse_range - 1) + (2 * no_warehouses)


    position_of_warehouses = generate_range(start_wharehouse_range,end_wharehouse_range)

    warehouses_loc_and_stock = []
    # print(position_of_warehouses)

    for i in position_of_warehouses:
        new_item = []
        location = list_file_inputs_lists_lines[i]
        stock = list_file_inputs_lists_lines[i + 1]
        new_item.append(location)
        new_item.append(stock)

        warehouses_loc_and_stock.append(new_item)

    # print(list_file_inputs_lists_lines[0])


    ## Customer orders

    location_cus_order_no = end_wharehouse_range + 1
    no_customter_orders = list_file_inputs_lists_lines[location_cus_order_no][0]

    start_customer_orders = location_cus_order_no + 1
    end_customer_order = location_cus_order_no + (no_customter_orders *2)

    range_orders = generate_range(start_customer_orders,end_customer_order)

    customer_order_loc_request = []

    for i in range_orders:
        new_item = []
        location = list_file_inputs_lists_lines[i]
        item_requested = list_file_inputs_lists_lines[i + 1]
        new_item.append(location)
        new_item.append(item_requested)

        customer_order_loc_request.append(new_item)



    Current_senario = Senario(senario_layout,no_products,product_weights,no_warehouses,warehouses_loc_and_stock,no_customter_orders,customer_order_loc_request)

    return Current_senario

def generate_range(start,finish):
    range_list = []
    for i in range(start,finish,2):
        range_list.append(i)
    return range_list


class Senario:

    def __init__(self,senario_layout,no_products,product_weights,no_warehouse,warehouse_info,no_cusotmer_orders, customer_orders):
        self.senario_layout = senario_layout
        self.no_products = no_products
        self.product_weights = product_weights
        self.no_warehouse = no_warehouse
        self.warehouse_info = warehouse_info
        self.no_customer_orders = no_cusotmer_orders
        self.customer_orders = customer_orders


    def print_information(self):
        print("The senario layout is", self.senario_layout)
        print("There are %i products their weight are %s" % (self.no_products,self.product_weights))
        print("There are %i warehouses" % (self.no_warehouse))
        print("The warehouse location and stock levels are %s" % (self.warehouse_info))
        print("There are %i customer order" % (self.no_customer_orders))
        print("The order location and requests are %s " % (self.customer_orders))


if __name__ == '__main__':
    file_name = "busy_day.in"
    current_senario = main(file_name)

