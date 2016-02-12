## File to take data input from file

# Take file input and convert each item to ints and create list that holds each line a sepearte list.

file_name = "busy_day.in"

file = open(file_name, "r")

file_object = file.read()

file_split_line = file_object.splitlines()

# for line in file_split_line:
#     line.split()
#     [int(i) for i in line]

line_2 = file_split_line[2]
print(line_2[0])

## Take grid input

senario_layout = file_split_line[0]

## Number of products and weights

no_products = file_split_line[1]

product_weight = file_split_line[2]


## Number of warehouse, locations and stocks


no_warehouses = file_split_line[3]

# start_wharehouse_range = no_warehouses + 1
# end_wharehouse_range = start_wharehouse_range + (2 * no_warehouses)
#
# print(start_wharehouse_range,end_wharehouse_range)

##
