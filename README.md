# final_project
Inventory management system for a planet store

The program consists of an interactive menu where we can add, search for, and remove planets from our space store.

When the program is running, it shows us the menu as follows:

          Welcome! Traveler
          Here you can manage your planet store
          
          1) Add planets
          2) Search planets
          3) Update planets
          4) Delete planets
          5) Calculate total 
          6) Exit

We must choose a valid option between 1 and 6 to continue execution. Otherwise, we will see an error message like the following:


          Type a correct number

If we choose option 1, we will be asked for the name, price and quantity of the planet to add.

          type the name of the planet: Planet X
          type the price of the planet: 35
          type the quantity of the planet: 1

If the user entered the data correctly, the following message will be displayed:

          Product addded correctly

If we choose option 2, we can search for a planet by its name

          Type the planet name to search: Neptuno

And we can obtain all the information from it:

          The planet Neptuno has a $30.0 value and his quantity is 5

If we choose option 3, we can update the price of a planet by searching for its name

          Type the name of the planet to update: Earth

Then it will ask us to enter the new price:

          Type the new price of the planet: 98

Finally it shows us the updated price:

          The new price of earth is $98

If we choose option 4, we can remove a planet from the inventory by searching for it by name.

          Type the name of the planet to delete: Neptuno

If we type a planet that is not in the inventory, it will show us a message:

          Type the name of the planet to delete: Saturne
          Planet not found

Finally, we can calculate the total inventory with option 5:

          earth  | 10.0 | 100
          saturn | 15.0 | 50
          uranus | 20.0 | 30
          mars   | 25.0 | 10
          neptune| 30.0 | 5
          
          Total price inventory is $2750.00


          
