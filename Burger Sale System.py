# Task site: https://www.programmingexpert.io/projects/async-point-of-sale-system

import asyncio
import random


# Basic functions

def number_teller(n):
    try:
        float(n)
        result = True
    except ValueError:
        result = False
    return result


# System-related functions

def alter_initial_order(stock,order_dic):
    for id, num in order_dic.itmes():
        deliver_status = stock.alter_stock(id,num)
        if deliver_status == -1:
            order_dic.pop(id)
        else:
            order_dic[id] = deliver_status
    return order_dic


def input_order(stock):
    order_list = []
    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
    while True:
        order = input("Enter an item number: ")
        if order == "q":
            print("Placing order...")
            break
        elif number_teller(order):
            order_num = int(order)
            current_available_stock = stock.get(order_num,"none")
            if current_available_stock == "none":
                print("[Failed to order] Your request is out of stock. Please go for another product.")
            else:
                ordered_num = order_list.count(order_num)
                if ordered_num + 1 <= current_available_stock:
                    order_list.append(order_num)
                else:
                    print("[Failed to order] Your request is out of stock. Please go for another product.")
        elif not number_teller(order):
            print("[Failed to order] Please enter a valid input.")
    return order_list

def order_list_generator(order_list):
    order_dic = {}
    for i in order_list:
        order_dic[i] = order_dic.get(i,0) + 1
    return order_dic

def combo_maker(lst):
    target = lst[0]
    product_name_default = target.get("feature","other")
    price = target.get("price")
    if product_name_default == "other":
        product_name_default = target.get("size")
    target["order_num"] = target.get("order_num") - 1
    return product_name_default, price

def combo_popper(lst):
    num_available = lst[0].get("order_num")
    if num_available == 0:
        del lst[0]
    return lst


class Inventory:
    def __init__(self):
        self.menu = None
        self.catalogue = {
            "Burgers": [
                {"id": 1, "name": "Python Burger", "price": 5.99},
                {"id": 2, "name": "C Burger", "price": 4.99},
                {"id": 3, "name": "Ruby Burger", "price": 6.49},
                {"id": 4, "name": "Go Burger", "price": 5.99},
                {"id": 5, "name": "Java Burger", "price": 7.99},
                {"id": 6, "name": "C++ Burger", "price": 7.99}
            ],
            "Sides": {
                "Fries": [
                    {"id": 7, "size": "Small", "price": 2.49},
                    {"id": 8, "size": "Medium", "price": 3.49},
                    {"id": 9, "size": "Large", "price": 4.29}
                ],
                "Caesar Salad": [
                    {"id": 10, "size": "Small", "price": 3.49},
                    {"id": 11, "size": "Large", "price": 4.49}
                ]
            },
            "Drinks": {
                "Coke": [
                    {"id": 12, "size": "Small", "price": 1.99},
                    {"id": 13, "size": "Medium", "price": 2.49},
                    {"id": 14, "size": "Large", "price": 2.99}
                ],
                "Ginger Ale": [
                    {"id": 15, "size": "Small", "price": 1.99},
                    {"id": 16, "size": "Medium", "price": 2.49},
                    {"id": 17, "size": "Large", "price": 2.99}
                ],
                "Chocolate Milk Shake": [
                    {"id": 18, "size": "Small", "price": 3.99},
                    {"id": 19, "size": "Medium", "price": 4.49},
                    {"id": 20, "size": "Large", "price": 4.99}
                ]
            }
        }

    def get_catalogue(self, category):
        self.menu = {}
        if category.lower() not in ["burgers", "sides", "drinks"]:
            print("this category doesn't exist in stock.")
        else:
            self.menu = self.catalogue.get(category, "null")
            return self.menu

    def build_initial_stock(self):
        self.stock = {}
        for i in range(1,21):
            stock = random.randint(1, 10)
            self.stock.update({i: stock})
        return self.stock

    def build_menu(self,lst):
        for i in range(len(lst)):
            product = lst[i]
            product_id = product.get("id","null")
            product_price = product.get("price", "null")
            # print(product.keys())
            if self.stock.get(product_id) == 0:
                pass
            else:
                if "name" not in product.keys():
                    product_name = product.get("size", "null")
                else:
                    product_name = product.get("name", "null")
                print(f"{product_id}. {product_name} {product_price}")

    def alter_stock(self,id,num):
        current_stock = self.stock.get(id,"none")
        deliver_status = -1
        if current_stock != "none":
            if num >= current_stock:
                deliver_status = current_stock
                self.stock[id] = 0
            else:
                deliver_status = num
                self.stock[id] = current_stock - num
        return deliver_status




    def combo_calculator(self, order_dic):
        self.Burger_order = []
        self.Side_order = []
        self.Drink_order = []
        for id, num in order_dic.items():
            if int(id) in range(1,7):
                product = {}
                product_info = self.catalogue.get("Burgers")[int(id) - 1]
                product.update({"id":id, "feature":product_info.get("name"), "price":product_info.get("price"), "order_num": num})
                self.Burger_order.append(product)
            elif int(id) in range(7,10):
                product = {}
                product_info = self.catalogue.get("Sides").get("Fries")[int(id) - 7]
                size = product_info.get("size")
                product.update({"id": id, "feature": f"{size} Fries", "price": product_info.get("price"), "order_num": num})
                self.Side_order.append(product)
            elif int(id) in range(10,12):
                product = {}
                product_info = self.catalogue.get("Sides").get("Caesar Salad")[int(id) - 10]
                size = product_info.get("size")
                product.update({"id": id, "feature": f"{size} Caesar Salad", "price": product_info.get("price"), "order_num": num})
                self.Side_order.append(product)
            elif int(id) in range(12,15):
                product = {}
                product_info = self.catalogue.get("Drinks").get("Coke")[int(id)-12]
                size = product_info.get("size")
                product.update({"id": id, "feature": f"{size} Coke", "price": product_info.get("price"), "order_num": num})
                self.Drink_order.append(product)
            elif int(id) in range(15,18):
                product = {}
                product_info = self.catalogue.get("Drinks").get("Ginger Ale")[int(id) - 15]
                size = product_info.get("size")
                product.update({"id": id, "feature": f"{size} Ginger Ale", "price": product_info.get("price"), "order_num": num})
                self.Drink_order.append(product)
            elif int(id) in range(18,21):
                product = {}
                product_info = self.catalogue.get("Drinks").get("Chocolate Milk Shake")[int(id) - 18]
                size = product_info.get("size")
                product.update({"id": id, "feature": f"{size} Chocolate Milk Shake", "price": product_info.get("price"), "order_num": num})
                self.Drink_order.append(product)
        self.Burger_order = sorted(self.Burger_order,key = lambda x: x.get("price"), reverse=True)
        self.Side_order = sorted(self.Side_order, key=lambda x: x.get("price"), reverse=True)
        self.Drink_order = sorted(self.Drink_order, key=lambda x: x.get("price"), reverse=True)

        # return self.Side_order
        # print(f"Burger order list: {self.Burger_order}")
        # print(f"Side order list: {self.Side_order}")
        # print(f"Drink order list: {self.Drink_order}")

        combo_list = []
        single_purchase_list = []

        while True:
            if self.Burger_order == [] or self.Side_order == [] or self.Drink_order == []:
                break

            if self.Burger_order != [] and self.Side_order != [] and self.Drink_order != []:

                combo_burger = combo_maker(self.Burger_order) #("Python Burger", 5.99)
                combo_side = combo_maker(self.Side_order)
                combo_drink = combo_maker(self.Drink_order)


                price = combo_burger[1] + combo_side[1] + combo_drink[1]

                product_compile = []

                product_compile.append(combo_burger[0])
                product_compile.append(combo_side[0])
                product_compile.append(combo_drink[0])

                single_combo = {}
                single_combo.update({"product":product_compile,"price":price})
                combo_list.append(single_combo)


                self.Burger_order = combo_popper(self.Burger_order)
                self.Side_order = combo_popper(self.Side_order)
                self.Drink_order = combo_popper(self.Drink_order)

                # print(f"Burger order list: {self.Burger_order}")
                # print(f"Side order list: {self.Side_order}")
                # print(f"Drink order list: {self.Drink_order}")


        return combo_list








# Initiate store and menu
Store = Inventory()
stock = Store.build_initial_stock()
print(stock)


Burgers_menu = Store.get_catalogue("Burgers")
Sides_menu = Store.get_catalogue("Sides")
Drinks_menu = Store.get_catalogue("Drinks")


# Display menu
print("")
print("-" * 10, "Menu for Today", "-" * 10)
print("*" * 10, "Burger", "*" * 10)
Store.build_menu(Burgers_menu)
print("")

print("*" * 10, "Sides", "*" * 10)
print("Fries")
Store.build_menu(Sides_menu.get("Fries"))
print("\nCaesar Salad")
Store.build_menu(Sides_menu.get("Caesar Salad"))
print("")

print("*" * 10, "Drinks", "*" * 10)
print("Coke")
Store.build_menu(Drinks_menu.get("Coke"))
print("\nGinger Ale")
Store.build_menu(Drinks_menu.get("Ginger Ale"))
print("\nChocolate Milk Shake")
Store.build_menu(Drinks_menu.get("Chocolate Milk Shake"))
print("")
print("-" * 10, "End of Menu", "-" * 10)

# Input order
order_list = input_order(stock)
# print(order_list)
order_dic = order_list_generator(order_list)
# print(order_dic)
test = Store.combo_calculator(order_dic)
print(test)
# print(test)
# print(combo_maker(test)[1])
# print(test)
# print(combo_popper(test))
