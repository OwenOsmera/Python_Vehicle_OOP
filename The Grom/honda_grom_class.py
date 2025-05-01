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

# This import will be used for the easter egg menu
import random


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
        self._admin_menu_title_color = "green"
        self._admin_menu_Rider_title_text = "purple"

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
        print(f"You made ${self.price} from the sale!")
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
        U.title("Honda Grom Menu", self._admin_menu_title_color, "")
        print(" 1. Go for a ride")
        print(" 2. Get a new Grom")
        print(" 3. Display Grom")
        print(" 4. Exit")
    
    # TODO Make a bike rider menu method for the Grom
    def bike_rider_menu(self):
        """ Display the menu for the Grom Rider """
        U.title("Honda Grom Rider Menu", self._admin_menu_Rider_title_text, "")
        self.console.print(f"[green] 1. Accelerate by {self._admin_speed_increase} MPH [/green]")
        self.console.print(f"[yellow] 2. Brake (slow down) down {self._admin_speed_increase} MPH [/yellow]")
        self.console.print("[red] 3. Stop (bring to a stop) [/red]")
        print(" 4. Exit")

    # TODO output the speed of the Grom
    def get_speed(self):
        """ Get the speed of the Grom """
        # This functions sole purpose is to output the speed to make the diving menu better
        return self._speed
        

    # TODO make a easter egg menu for the Grom
    def easter_egg_menu(self):
        """ Display the easter egg menu for the Grom """
        U.title("Easter Egg Menu (ADMIN CHANGES)", "yellow", "")
        print("1. Chenge Admin Speed")
        print("2. Change Grom Menu Title Color")
        print("3. Change Grom Rider Menu Title Text")
        print("4. To quit: ")
        
    # TODO make a easter hint randomizer for the Grom
    def easter_egg_hint(self):
        """ Display a random easter egg hint """
        # Change this to make it easier to find the easter egg
        test = random.randint(1,5)

        # Checks in the random number is what it needs to be to show the hint
        if test == 5:
            print("")
            print("PSSST! if you are seeing this you are fairly lucky!")
            print("You have found a secret!")
            print("You can now go to the easter egg menu!")
            print("Put in the code 115 on the main menu to access the easter egg menu!")
            print("")

    # Changes the admin speed of the Grom
    def change_admin_speed(self, admin_speed_increase):
        """ Change the admin speed of the Grom """
        self._admin_speed_increase = admin_speed_increase

    # Changes the color of the Grom menu title
    def change_menu_title_color(self, color):
        """ Change the color of the Grom menu title """
        self._admin_menu_title_color = color

        # will display what the title will look like if does not work will repeat code to try again
        try:
            print("Menu title will look like this:")
            U.title("Honda Grom Menu", self._admin_menu_title_color, "")
            print("")
        except:
            print("Error: Menu title color not valid")
            print("Try again:")
            self.change_menu_title_color(input("Enter a color for the title: "))

    # Changes the color of the Grom menu title
    def change_menu_rider_title_color(self, color):
        """ Change the color of the Grom menu title """
        self._admin_menu_Rider_title_text = color

        # will display what the title will look like if does not work will repeat code to try again
        try:
            print("Menu title will look like this:")
            U.title("Honda Grom Rider Menu", self._admin_menu_Rider_title_text, "")
            print("")
        except:
            print("Error: Menu title color not valid")
            print("Try again:")
            self.change_menu_rider_title_color(input("Enter a color for the title: "))
    
        



