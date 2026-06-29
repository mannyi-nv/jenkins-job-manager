import data
import manage_jobs

def del_jobs():        
    while True:
        
        jobs_data = data.load_jobs()
        
        if not jobs_data:
            print("\nERROR!!! No jobs to delete, going back to main menu")
            break

        print("\nExisting Jobs list:")
        define = f"Existing Jobs list:"
        print("=" * len(define))
        print()
        for idx, job in enumerate(jobs_data, start=1): # making sure enumerate count will start at 1
            print(f"{idx}. {job['job_name']}")
        
        print("0. Cancel and return to main menu") # will be used to go back to the main menu

        try:
            user_input = input("\nEnter the number of the job to delete: ")
            job_choice = int(user_input)

            if job_choice == 0:
                print(f"\nDelete has been canceled by the user.")
                print(f"Returning back to the main menu.")
                break  # Exit the retry loop and go back to the main menu

            if 1 <= job_choice <= len(jobs_data):
                job_to_delete = jobs_data[job_choice - 1]["job_name"]
                user_conf = input(f"\nPlease type 'YES / NO' to confirm: ").lower()

                if user_conf == "yes": # Perform the actual deletion

                    jobs_data = manage_jobs.delete_job(jobs_data, job_to_delete)
                    data.save_jobs(jobs_data)
                    print(f"Job '{job_to_delete}' deleted successfully, returning back to the main menu")
                    return
                else:
                    print(f"\nDelete has been canceled by the user.")
                    print(f"Returning back to the main menu.")
                    break
                
            else:
                print(f"\nPlease enter a number between 1 and {len(jobs_data)}.")

        except ValueError:
            print("\nError: Invalid input. Please enter a valid number") # will catch if user type str job name and not int