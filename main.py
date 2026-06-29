import main_menu
import add_jobs
import delete_jobs
import update_jobs
import display_jobs

while True:
    try:

        ##### Show menu ######

        # Displaying the main menu list user choice

        choice = main_menu.menu()

        ################################ Add jobs ################################

        if choice == "1":
            add_jobs.add_jobs()
            
        ################################ Delete jobs ##############################

        elif choice == "2":
            delete_jobs.del_jobs()
        
        ################################ Update jobs ##############################

        elif choice == "3":
             update_jobs.up_jobs()
            
        ################################ load demi data ###########################
        ################################ Coming soon ##############################

        # elif choice == "4":  # load demi data

        ################################ Display jobs #############################

        elif choice == "5":  # Job display
            display_jobs.list_jobs()              

        ################################## EXIT ####################################

        elif choice == "6":
            print("Exiting...")
            break

        ################################ Invalid choice #############################
        
        else:
            print("\nInvalid menu option. Please choose a number between 1-6.")

    except Exception as e:
        print(f" Unexpected error:------------ {e}")