"""
Owen Osmera
HGM_Class_TODO.py
created on 4/28/25
pupouse use the class to make workable motor bike mini game
"""

# TODO import the time module so there is some loding for effect
import time

import utils as U

from rich.console import Console
from rich.panel import Panel



# TODO make class for honda Grom
""" I could make some set methods but I will rely on the inicialization of the class """

class HondaGrom:
    """ Makes a honda Grom object (color, max_speed, year, price) """
    # TODO make init method for honda Grom
    def __init__(self, color, max_speed, year, price, admin_speed_increase =5):
        self.color = color 
        self.max_speed = max_speed
        self.year = year
        self.price = price
        self._admin_speed_increase = admin_speed_increase
        self._speed = 0
        self.console = Console()

        # Just the fake loading screen for the Grom
        print("Creating a new Grom...")
        time.sleep(2)
        print("Grom created!")

        # This just creates space in the out put
        print("")


        # Display the Grom information
        self.display()

        

    # TODO make a change speed method for the Grom
    def accelerate(self):
        """ Increase the speed of the Grom """
        if self._speed + self._admin_speed_increase > self.max_speed:
            print("You have reached the max speed of the Grom")
        else:
            self._speed += self._admin_speed_increase
            print(f"The speed of the Grom is now {self._speed}")

        time.sleep(1)

    # TODO make a brake method for the Grom
    def brake(self):
        """ Decrease the speed of the Grom """
        if self._speed - self._admin_speed_increase < 0:
            print("The Grom is already stopped")
        else:
            self._speed -= self._admin_speed_increase
            print(f"The speed of the Grom is now {self._speed}")

        time.sleep(1)

    # TODO bring the Grom to a stop method
    def stop(self):
        """ Bring the Grom to a stop """
        # This is a fancy way of making the Grom stop intresting
        print("Grom is stopping...")
        time.sleep(2)

        self._speed = 0
        print("The Grom is now stopped")

    # TODO make a change color method for the Grom
    def change_color(self, color):
        """ Change the color of the Grom """
        self.color = color
        return self.color

    # TODO make a change year method for the Grom
    def change_year(self, year):
        """ Change the year of the Grom """
        self.year = year
        return self.year

    # TODO make a change price method for the Grom
    def change_price(self, price):
        """ Change the price of the Grom """
        self.price = price
        return self.price
    
    # TODO Make a max speed change method for the Grom
    def change_max_speed(self, max_speed):
        """ Change the max speed of the Grom """
        self.max_speed = max_speed
        return self.max_speed

    # TODO Get a new Grom
    def get_new_grom(self, color, max_speed, year, price):
        """ Sell old Grom before getting a new one """
        print("Selling old Grom...")
        time.sleep(1)
        print("Old Grom sold!")
        print(f"You made {self.price} from the sale!")
        time.sleep(1)
        print("Preparing the new Grom...")
        time.sleep(1)
        print("New Grom is ready!")
        

        """ Get a new Grom """
        self.color = self.change_color(color)
        self.max_speed = self.change_max_speed(max_speed)
        self.year = self.change_year(year)
        self.price = self.change_price(price)

        # Display the new Grom information
        print("")
        self.display()
        print("New Grom is ready to ride!")

    # TODO Make a display method for the Grom
    def display(self):
        """ Display the Grom """
        U.title("Your Current Grom", "white", "")
        print(f"The color of the Grom is:     {self.color}")
        print(f"The max speed of the Grom is: {self.max_speed} MPH")
        print(f"The year of the Grom is:      {self.year}")
        print(f"The price of the Grom is:    ${self.price}")
        time.sleep(3)

    # TODO Make a menu method for the Grom
    def menu(self):
        """ Display the menu for the Grom """
        U.title("Honda Grom Menu", "green", "")
        print(" 1. Go for a ride")
        print(" 2. Get a new Grom")
        print(" 3. Display Grom")
        print(" 4. Exit")
    
    # TODO Make a bike rider menu method for the Grom
    def bike_rider_menu(self):
        """ Display the menu for the Grom Rider """
        U.title("Honda Grom Rider Menu", "purple", "")
        self.console.print(f"[green] 1. Accelerate by {self._admin_speed_increase} MPH [/green]")
        self.console.print(f"[yellow] 2. Brake (slow down) down {self._admin_speed_increase} MPH [/yellow]")
        self.console.print("[red] 3. Stop (bring to a stop) [/red]")
        print(" 4. Exit")
        

