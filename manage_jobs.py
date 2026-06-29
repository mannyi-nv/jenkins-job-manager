
def add_job(job_name, owner, description):
    #Docstring:
    """
    add_job dict items

    Parameters:
        job_name, owner,desciption

    returns:
        str dict type items saved to jobs.json
        
    """
    return {
        "job_name": job_name,
        "owner": owner,
        "description": description,
        "path": f"/jenkins_home/jobs/{job_name}"
    }

def delete_job(jobs, job_name):
    #Docstring:
    """
    delete_job list items

    use found = False as a place holder
        if job (found) will switch False to True
            delete jobs
        else
            no jobs, (found) is False, error will display to user

        returns:
            list type items removed from jobs.json
        
    """
    updated_jobs = []
    found = False 
    for job in jobs:
        if job["job_name"] != job_name:
            updated_jobs.append(job)
        else:
            found = True
    if not found:
        print(f"Job '{job_name}' not found.")
    return updated_jobs

def update_job(jobs, job_name, new_owner=None, new_description=None):
    #Docstring:
    """
    use found = False as a place holder
        if job (found) will switch False to True
            update jobs
        else
            no jobs, (found) is False, error will display to user

        returns:
            return updated jobs list  
    
    """
    found = False
    for job in jobs:
        if job["job_name"] == job_name:
            if new_owner:
                job["owner"] = new_owner
            if new_description:
                job["description"] = new_description
            found = True
            break  # job names are unique, no need to continue
    if not found:
        print(f"Job '{job_name}' not found.")
    return jobs