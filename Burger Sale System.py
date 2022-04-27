# Task site: https://www.programmingexpert.io/projects/async-point-of-sale-system

import asyncio
import random



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
        for i in range(20):
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




# Initiate store and menu
Store = Inventory()
Store.build_initial_stock()


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