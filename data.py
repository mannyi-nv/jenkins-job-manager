import json

# Enforce a strict absolute path to your production deployment directory
DEFAULT_PATH = "/var/www/jenkins-job-manager/jobs.json"

def load_jobs(filename=DEFAULT_PATH):
    try:
        with open(filename, "r") as f:
            jobs = json.load(f)
            if not isinstance(jobs, list):
                return []
            return jobs
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print(f"Warning: {filename} contains invalid JSON.")
        return []

def save_jobs(jobs, filename=DEFAULT_PATH):
    try:
        with open(filename, "w") as f:
            json.dump(jobs, f, indent=4)
        print("Jobs saved successfully.")
    except Exception as e:
        print(f"Error saving jobs: {e}")

