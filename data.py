import json

# Enforce a strict absolute path to your production deployment directory
DEFAULT_PATH = "/var/www/jenkins-job-manager/jobs.json"

# Workspace-local development path (checked first when filename is not provided)
DEV_PATH = "./jobs.json"


def _resolve_filename(filename: str | None):
    """Return the filename to use. If `filename` is provided, return it.
    Else prefer the workspace-local `DEV_PATH` if it exists, otherwise fall back
    to the production `DEFAULT_PATH`.
    """
    if filename:
        return filename
    try:
        # Prefer workspace-local sample file for local development
        with open(DEV_PATH, "r"):
            return DEV_PATH
    except Exception:
        return DEFAULT_PATH


def load_jobs(filename: str | None = None):
    path = _resolve_filename(filename)
    try:
        with open(path, "r") as f:
            jobs = json.load(f)
            if not isinstance(jobs, list):
                return []
            return jobs
    except FileNotFoundError:
        print(f"Warning: {path} not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print(f"Warning: {path} contains invalid JSON.")
        return []


def save_jobs(jobs, filename: str | None = None):
    path = _resolve_filename(filename)
    try:
        with open(path, "w") as f:
            json.dump(jobs, f, indent=4)
        print(f"Jobs saved successfully to {path}.")
    except Exception as e:
        print(f"Error saving jobs to {path}: {e}")

