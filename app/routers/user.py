from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
def all_users():
    return []


@router.get("/{user_id}")
def user_by_id(user_id: int):
    return {}


@router.post("/create")
def create_user():
    return {}


@router.put("/update")
def update_user():
    return {}


@router.delete("/delete")
def delete_user():
    return {}
