'''The algorithm has as its main element a list of dictionaries
in which 5 initial planets are stored.'''
inventory = [

    {"name": "earth", "price": 10.0, "quantity": 100},
    {"name": "saturn", "price": 15.0, "quantity": 50},
    {"name": "uranus", "price": 20.0, "quantity": 30},
    {"name": "mars", "price": 25.0, "quantity": 10},
    {"name": "neptune", "price": 30.0, "quantity": 5}
]


'''In this section, we have two functions that help us validate data inputs.'''

'''In both options we verify that the user enters
a number and that it is positive.'''
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("\033[31mError: Type a positive number.\033[0m")
        except ValueError:
            print("\033[31mError: Type a valid character.\033[0m")

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("\033[31mError: Type a positive number.\033[0m")
        except ValueError:
            print("\033[31mError: Type a valid character.\033[0m")   


'''We request the different inputs such as name, price 
and quantity and add them to the list like another dictionary.'''
def add_products():
    name_product = input("type the name of the planet: ").lower()
    price_product = get_valid_float("type the price of the planet: ")
    quantity_product = get_valid_int("type the quantity of the planet: ")
    inventory.append({"name": name_product, "price": price_product, "quantity ":quantity_product})
    print("\n\033[32mProduct addded correctly\033[0m")


'''
We request the name of the product we want to search for and check if it's in stock.
If the answer is yes, we proceed to display the results.
'''
def search_products():
    name_product = input("Type the planet name to search: ").lower()
    for i in inventory:
        if name_product == i["name"]:
            print(f" The planet {i["name"]} has a \033[32m${i["price"]}\033[0m value and his quantity is {i["quantity"]}")
            break
    else:
        print("\n\033[031mPlanet not found\033[0m")


'''
We ask the user for the name of the product to update.
We verify that it exists and proceed to update its price, 
replacing it with the new one requested.
'''       
def update_product():
    name_product = input("Type the name of the planet to update: ").lower()
    for i in inventory:
        if name_product == i["name"]:
            new_price = get_valid_int("Type the new price of the planet: ")
            i["price"] = new_price
            print(f"The new price of {name_product} is ${i['price']}")

'''
We again request the name of the product to be deleted. Next, we check if it exists in the inventory 
and finally delete it with the remove() method.
'''

def delete_products():
    name_product = input("Type the name of the planet to delete: ").lower()
    for i in inventory:
        if name_product == i["name"]:
            inventory.remove(i)
            break
    else:
        print("\n\033[031mPlanet not found\033[0m")


'''
We created a lambda function to print a table with the prices 
and then the total sum of all the planet prices by their respective quantities.
'''
           
print_table = lambda: print("\n".join(f"{i['name']} | {i['price']} | {i['quantity']}" for i in inventory) +
     f"\nTotal price inventory is \033[32m${sum(i['price'] * i['quantity'] for i in inventory):.2f}\033[0m")


'''
We show the menu of available options with a while, we test the options with a try and
with a match we access the different functions created previously
'''                        
while True:
    print('''
          \033[33mWelcome! Traveler
          Here you can manage your planet store\033[0m\n
          1) Add planets
          2) Search planets
          3) Update planets
          4) Delete planets
          5) Calculate total 
          6) Exit
          ''')
    try: 
        option = get_valid_int("Type a number: ")
        match option:
            case 1:
                add_products()
            case 2:
                search_products()
            case 3:
                update_product()
            case 4:
                delete_products()
            case 5:
                print_table()
            case 6:
                print("\033[34mSee you later! Space traveler\033[0m")
                break
    except ValueError:
        print("Type a correct number ")
        
