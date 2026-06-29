from fastapi import FastAPI
from services.job_service import get_all_jobs, create_job, delete_job, update_job
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 1. DEFINE API ROUTES FIRST
@app.get("/jobs")
def get_jobs():
    return get_all_jobs()

@app.post("/jobs")
def add_job(job: dict):
    return create_job(
        job.get("job_name"),
        job.get("owner"),
        job.get("description"),
        job.get("created_by"),
        job.get("last_modify"),
        job.get("schedule")
    )

@app.delete("/jobs/{job_id}")
def remove_job(job_id: int):
    return delete_job(job_id)

@app.put("/jobs/{job_id}")
def edit_job(job_id: int, job: dict):
    return update_job(
        job_id,
        job_name=job.get("job_name"),
        owner=job.get("owner"),
        description=job.get("description"),
        created_by=job.get("created_by"),
        last_modify=job.get("last_modify"),
        last_run=job.get("last_run"),
        schedule=job.get("schedule")
    )

# 2. MOUNT STATIC FILES AT THE VERY BOTTOM
app.mount("/", StaticFiles(directory="static", html=True), name="static")
