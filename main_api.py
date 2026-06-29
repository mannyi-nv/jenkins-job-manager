from fastapi import FastAPI, Query
from services.job_service import get_all_jobs, create_job, delete_job, update_job
from fastapi.staticfiles import StaticFiles

# Map target keyword to filename used by data layer
TARGET_FILES = {
    "dev": "dummy_jobs.json",
    "production": None  # None means use default path (production DEFAULT_PATH)
}

app = FastAPI()

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

# 2. MOUNT STATIC FILES AT THE VERY BOTTOM
app.mount("/", StaticFiles(directory="static", html=True), name="static")
