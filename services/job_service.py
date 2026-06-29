from data import load_jobs, save_jobs

###############
# Create Jobs #
###############

from data import load_jobs, save_jobs

###############
# Create Jobs #
###############

def create_job(job_name: str, owner: str, description: str, created_by: str = "admin", last_modify: str = "", schedule: str = "Manual"):
    if not job_name or not owner:
        raise ValueError("job_name and owner are required")

    try:
        jobs = load_jobs()
    except Exception:
        jobs = []

    new_job = {
        "job_name": job_name,
        "owner": owner,
        "description": description,
        "created_by": created_by or "admin",
        "last_modify": last_modify,
        "last_run": "",
        "schedule": schedule or "Manual",
        "status": "PENDING"
    }

    jobs.append(new_job)
    save_jobs(jobs)

    return new_job

################
# Display Jobs #
################

def get_all_jobs():
    try:
        jobs = load_jobs()
    except Exception:
        jobs = []

    return jobs

################
# Delete Jobs  #
################

def delete_job(index: int):
    jobs = load_jobs()

    if index < 0 or index >= len(jobs):
        raise IndexError("Invalid job index")

    removed_job = jobs.pop(index)
    save_jobs(jobs)

    return removed_job


################
# Update Jobs  #
################

def update_job(index: int, job_name: str = None, owner: str = None, description: str = None, created_by: str = None, last_modify: str = None, last_run: str = None, schedule: str = None):
    jobs = load_jobs()

    if index < 0 or index >= len(jobs):
        raise IndexError("Invalid job index")

    job = jobs[index]

    # --- Core Properties Mapping Updates ---
    if job_name is not None and job_name.strip() != "":
        job["job_name"] = job_name
    if owner is not None and owner.strip() != "":
        job["owner"] = owner
    if description is not None and description.strip() != "":
        job["description"] = description
    if created_by is not None and created_by.strip() != "":
        job["created_by"] = created_by
    if last_modify is not None:
        job["last_modify"] = last_modify
    if last_run is not None:
        job["last_run"] = last_run

    # --- Safe Dropdown Mapping Update Fix ---
    # This forces Python to accept the schedule value even if the original json row entry lacked the 'schedule' key!
    if schedule is not None and schedule.strip() != "":
        job["schedule"] = schedule
    elif "schedule" not in job:
        job["schedule"] = "Manual" # Default fallback placeholder value

    save_jobs(jobs)
    return job

