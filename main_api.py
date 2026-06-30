from fastapi import FastAPI, Query
import shutil
from pathlib import Path
from services.job_service import get_all_jobs, create_job, delete_job, update_job, sync_jobs
from fastapi.staticfiles import StaticFiles

# Map target keyword to filename used by data layer
TARGET_FILES = {
    "dev": "dummy_jobs.json",
    "production": None  # None means use default path (production DEFAULT_PATH)
}

app = FastAPI()


@app.on_event("startup")
def copy_production_to_dev():
    """Ensure `dummy_jobs.json` exists and is copied from `jobs.json` at startup.

    This keeps the development view in sync with the repository production
    data each time the app starts (useful when running in a VM/container).
    """
    try:
        base = Path(__file__).parent
        src = base / "jobs.json"
        dest = base / "dummy_jobs.json"
        if src.exists():
            shutil.copyfile(src, dest)
            print(f"Copied {src} -> {dest} on startup")
    except Exception as e:
        print(f"Warning: failed to copy jobs.json to dummy_jobs.json on startup: {e}")

# 1. DEFINE API ROUTES FIRST
@app.get("/jobs")
def get_jobs(target: str | None = Query(None, description="Choose 'dev' or 'production' to select storage")):
    filename = TARGET_FILES.get(target) if target else None
    return get_all_jobs(filename)

@app.post("/jobs")
def add_job(job: dict, target: str | None = Query(None, description="Choose 'dev' or 'production' to select storage")):
    filename = TARGET_FILES.get(target) if target else None
    return create_job(
        job.get("job_name"),
        job.get("owner"),
        job.get("description"),
        job.get("created_by"),
        job.get("last_modify"),
        job.get("schedule"),
        filename=filename
    )

@app.delete("/jobs/{job_id}")
def remove_job(job_id: int, target: str | None = Query(None, description="Choose 'dev' or 'production' to select storage")):
    filename = TARGET_FILES.get(target) if target else None
    return delete_job(job_id, filename=filename)

@app.put("/jobs/{job_id}")
def edit_job(job_id: int, job: dict, target: str | None = Query(None, description="Choose 'dev' or 'production' to select storage")):
    filename = TARGET_FILES.get(target) if target else None
    return update_job(
        job_id,
        job_name=job.get("job_name"),
        owner=job.get("owner"),
        description=job.get("description"),
        created_by=job.get("created_by"),
        last_modify=job.get("last_modify"),
        last_run=job.get("last_run"),
        schedule=job.get("schedule"),
        filename=filename
    )

@app.post("/sync-dev-to-prod")
def sync_dev_to_prod():
    return sync_jobs(source_filename="dummy_jobs.json", target_filename=None)

# 2. MOUNT STATIC FILES AT THE VERY BOTTOM
app.mount("/", StaticFiles(directory="static", html=True), name="static")
