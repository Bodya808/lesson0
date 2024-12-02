from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
def all_tasks():
    return []


@router.get("/{task_id}")
def task_by_id(task_id: int):
    return {}


@router.post("/create")
def create_task():
    return {}


@router.put("/update")
def update_task():
    return {}


@router.delete("/delete")
def delete_task():
    return {}
