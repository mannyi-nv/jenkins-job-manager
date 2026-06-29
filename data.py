import json
import os

# Enforce a strict absolute path to your production deployment directory
DEFAULT_PATH = "/var/www/jenkins-job-manager/jobs.json"
FALLBACK_PATH = os.path.join(os.path.dirname(__file__), "jobs.json")


def _get_production_path():
    if os.path.exists(DEFAULT_PATH):
        return DEFAULT_PATH

    directory = os.path.dirname(DEFAULT_PATH)
    try:
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        return DEFAULT_PATH
    except OSError as exc:
        print(f"Warning: unable to use production path {DEFAULT_PATH} ({exc}). Falling back to {FALLBACK_PATH}.")
        return FALLBACK_PATH


def _resolve_filename(filename: str | None):
    """Return the filename to use. If `filename` is provided, return it.
    Otherwise default to production storage or a fallback path."""
    return filename or _get_production_path()


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
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(path, "w") as f:
            json.dump(jobs, f, indent=4)
        print(f"Jobs saved successfully to {path}.")
    except Exception as e:
        print(f"Error saving jobs to {path}: {e}")
        raise

