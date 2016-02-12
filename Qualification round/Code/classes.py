# File containing all hte python class and function required for the challange

# Classes

import math

class Drone:

    def __init__(self,position,current_load,items_weight,max_weight):
        self.position_x = position[0]
        self.position_y = position[1]
        self.current_load = current_load
        self.items_weight = items_weight
        self.max_weight = max_weight
        self.current_weight = 0

    def give_position(self):
        return self.position

    def change_position(self, new_position):
        old_positon = self.position
        new_position = new_position

        change_in_x = (old_positon[0] - new_position[0])
        change_in_y = (old_positon[1] - new_position[1])

        distance_travelled = math.sqrt( (change_in_x**2) + (change_in_y**2) )

        # round up

        self.position = new_position

        return distance_travelled

    def load_item(self,item_id,quantity):

        # Load new item into drone
        current_load = self.current_load
        current_item_stock = current_load[item_id]

        new_item_stock = current_item_stock + quantity

        # Set current item stock
        self.current_load[item_id] = new_item_stock

        self.current_weight = self.return_weight()

        # If overweight unload items one by one until under max capacity

        while (self.current_weight > self.max_weight):

            # Remove items one by one
            self.unload_item(item_id,1)
            self.current_weight = self.return_weight()
            quantity -= 1

        print("Was able to load %i items" % (quantity))
        return quantity, self.current_weight

    def unload_item(self,item_id,quantity):

        # unload item
        current_item_stock = self.current_load[item_id]

        # While loop to ensure that drone stock can not go negative
        while current_item_stock < quantity:
            quantity -= 1


        new_item_stock = current_item_stock - quantity


        self.current_load[item_id] = new_item_stock

        print("Was able to unload %i items" % quantity)
        return quantity


    def return_weight(self):
        length_weight_array = (len(self.items_weight)- 1)

        total_weight = 0

        for i in range(0,length_weight_array):
            item_weight = self.current_load[i] * self.items_weight[i]
            total_weight += item_weight

        self.current_weight = total_weight

        return self.current_weight

    def check_item_stock(self,item_id):
        current_item_stock = self.current_load[item_id]
        return current_item_stock

    def print_value(self):
        print("The current load is ", self.current_load)
        print("The current weight is ", self.current_weight)
        print("The current position is ", self.position)

# class wharehouse:
#
# class customer_order:
#
# class item:
#
# position,current_load,number_of_items,items_weight,max_weight

drone_1 = Drone([0,1],[0,0,0,0,0,0],[1,1,1,2,2,2],400)

drone_1.print_value()
drone_1.load_item(2,200)
drone_1.print_value()

print(drone_1.check_item_stock(2))

# Functions

def total_score():
    return
