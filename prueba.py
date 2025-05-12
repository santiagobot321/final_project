inventory = [
    {"name": "earth", "price": 10.0, "quantity": 100},
    {"name": "saturn", "price": 15.0, "quantity": 50},
    {"name": "uranus", "price": 20.0, "quantity": 30},
    {"name": "mars", "price": 25.0, "quantity": 10},
    {"name": "neptune", "price": 30.0, "quantity": 5}
]

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

def add_products():
    name_product = input("type the name of the planet: ").lower()
    price_product = get_valid_float("type the price of the planet: ")
    quantity_product = get_valid_int("type the quantity of the planet: ")
    inventory.append({"name": name_product, "price": price_product, "quantity ":quantity_product})
    print("\n\033[32mProduct addded correctly\033[0m")

def search_products():
    name_product = input("Type the planet name to search: ").lower()
    for i in inventory:
        if name_product == i["name"]:
            print(f" The {i["name"]} has a \033[32m${i["price"]}\033[0m value and his quatity is {i["quantity"]}")
            break
    else:
        print("\n\033[031mPlanet not found\033[0m")
        
def update_product():
    name_product = input("Type the name of the planet to update: ").lower()
    for i in inventory:
        if name_product == i["name"]:
            new_price = get_valid_int("Type the new price of the planet: ")
            i["price"] = new_price
            print(f"The new price of {name_product} is ${i['price']}")

def delete_products():
    name_product = input("Type the name of the planet to delete: ").lower()
    for i in inventory:
        if name_product == i["name"]:
            inventory.remove(i)
            break
    else:
        print("\n\033[031mPlanet not found\033[0m")
            
print_table = lambda: print("\n".join(f"{i['name']} | {i['price']} | {i['quantity']}" for i in inventory) +
     f"\nTotal price inventory is \033[32m${sum(i['price'] * i['quantity'] for i in inventory):.2f}\033[0m")
                         
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