import data
import manage_jobs

def up_jobs():
    while True:
    
        jobs_data = data.load_jobs()

        if not jobs_data:
            print("\nERROR!!! No jobs to update, going back to main menu")
            break
                
        print("\nExisting Jobs list:")
        define = f"Existing Jobs list:"
        print("=" * len(define))
        print()
        for idx, job in enumerate(jobs_data, start=1): # making sure enumerate count will start at 1
            print(f"{idx}. {job['job_name']} (Owner: {job['owner']}, Description: {job['description']})")

        print("0. Cancel and return to main menu") # will be used to go back to the main menu   

        try:
            user_input = int(input("\nEnter the number of the job you would like to update: "))
            job_choice = int(user_input)

            if job_choice == 0:
                print("\nUpdate has been cancelled by the user.")
                print(f"Returning back to the main menu.")
                break  # Exit the retry loop and go back to the main menu
            
            if 1 <= job_choice <= len(jobs_data):
        
                job_to_update = jobs_data[job_choice - 1]["job_name"]

                # Using .strip() below to make sure user will not press backspace and enter which result in an empty owner, description value
                new_owner = input("Please enter new owner (leave blank if no change is needed): ").strip()
                new_description = input("Please enter new description (leave blank if no change is needed): ").strip()

                jobs_data = manage_jobs.update_job(
                    jobs_data, job_to_update,
                    new_owner if new_owner else None,
                    new_description if new_description else None
                )

                data.save_jobs(jobs_data)
                print(f"Job '{job_to_update}' updated successfully.")
                input("\nPress Enter to return to the main menu...")
                break
                
            else:
                print(f"\nPlease enter a number between 1 and {len(jobs_data)}.")             
        

        except Exception:
            print(f"\nError: Invalid input. Please enter a valid number")