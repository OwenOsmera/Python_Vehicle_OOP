"""
Owen Osmera
HGM_TODO.py
created on 4/28/25
pupouse use the class to make workable motor bike mini game
"""

# TODO import the class and utils modules
import honda_grom_class as HG
import utils as U

# TODO create a constant for the admin speed increase
ADMIN_SPEED_INCREASE = 5

# TODO main file to create the Honda Grom
def main():
    # TODO make a cool title for the program
    U.title("Honda Grom Mini Game", "blue", "By Owen Osmera")

    # TODO make a user dictionary to hold the users bike data
    user_bike = {
        "color": input("What color do you want your bike to be? "),
        "max_speed": U.get_int("What is the max speed of your bike? "),
        "year": U.get_int("What year is your bike? "),
        "price": U.get_float("What is the price of your bike? "),
    }

    # TODO use those values to make a user bike class
    created_bike = HG.HondaGrom(
        user_bike["color"],
        user_bike["max_speed"],
        user_bike["year"],
        user_bike["price"],
        ADMIN_SPEED_INCREASE,
    )
    print()


    
    # TODO Game loop to run the game
    while True:

        # Create a menu of options for the user to choose from
        created_bike.menu()
        

        # Check the user choice and call the appropriate method
        choice = U.get_int("Please enter your choice: ")
        print("")

        if choice == 1:
            # Display the bike information menu
            while True:
                created_bike.bike_rider_menu()
                

                # Get the user choice
                bike_menu_choice = U.get_int("Please enter your choice: ")
                print("") 

                
                if bike_menu_choice == 1:
                    # accelerate the bike
                    created_bike.accelerate()
                elif bike_menu_choice == 2:
                    # brake the bike
                    created_bike.brake()
                elif bike_menu_choice == 3:
                    # bring the bike to a stop
                    created_bike.stop()
                else:
                    created_bike.stop()
                    print("Exiting the bike rider menu...")
                    print("")
                    # Slows down the bike and exits the bike menu
                    break

                print("")
        elif choice == 2:
            # Get a new Grom
            user_bike["color"] = input("What color do you want your new bike to be? ")
            user_bike["max_speed"] = U.get_int("What is the max speed of your new bike? ")
            user_bike["year"] = U.get_int("What year is your new bike? ")
            user_bike["price"] = U.get_float("What is the price of your new bike? ")
            # Call the get_new_grom method to get a new bike
            created_bike.get_new_grom(
            user_bike.get("color"),
            user_bike.get("max_speed"),
            user_bike.get("year"),
            user_bike.get("price")
            )

        elif choice == 3:
            # Display the bike information
            created_bike.display()

        else:
            # Exit the program
            print("Exiting the program...")
            break
        print()

# TODO code for running the program 
if __name__ == "__main__":
    main()





