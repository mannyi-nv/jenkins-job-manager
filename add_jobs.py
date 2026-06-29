import data
import manage_jobs

def add_jobs():
    while True:
        
        jobs_data = data.load_jobs()
        
        try:
            jobs_counter = int(input("\nPlease enter how many jobs to create: "))
            print("you can type 0 to cancel and return to the main menu at any time")
            if jobs_counter == 0:
                print("Operation canceled. Returning to main menu.")
                break # going back to the main menu
            
        except ValueError:  
            print("\nError: Invalid input. Please enter a valid number")
            continue

        for i in range(jobs_counter):
            job_name = input(f"Please enter job name for job number {i + 1}: ")
            owner = input(f"Enter owner for: {job_name} ")
            description = input(f"Enter description for: {job_name} ")

            new_job = manage_jobs.add_job(job_name, owner, description)
            jobs_data.append(new_job)

        # Save all jobs
        data.save_jobs(jobs_data)
        print(f"\n{jobs_counter} job(s) added successfully.")
        input("\nPress Enter to return to the main menu...")
        break