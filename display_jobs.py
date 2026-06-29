import data

def list_jobs():
    while True:
        jobs_data = data.load_jobs()

        if not jobs_data:
            print("\nERROR!!!No jobs to display, going back to main menu")
            break
                    
        try:
            print("\nJobs Summery:")
            define = f"Jobs Summery:"
            print("=" * len(define))
            print()
            for idx, job in enumerate(jobs_data, start=1):
                print(f"{idx}. Job name: {job['job_name']}, Owner: {job['owner']}, Description: {job['description']}")
            input("\nPress Enter to return back to the main menu...")
            break
        
        except Exception as e:
            print(e)