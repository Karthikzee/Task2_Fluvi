from fastapi import APIRouter, HTTPException, status
from server.models.user import UpdateUser, User
from server.utils import pydantic_encoder
from typing import List
from uuid import UUID

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: User):
    await user.insert()
    return user


@router.get("/", response_model=List[User])
async def get_users():
    users = await User.find_all().to_list()
    return users


@router.get("/{id}", response_model=User)
async def get_user(id: UUID):
    user = await User.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )

    return user


@router.put("/{id}", response_model=User)
async def update_user(id: UUID, user_data: UpdateUser):
    user = await User.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    user_data = pydantic_encoder.encode_input(user_data)
    _ = await user.update({"$set": user_data})
    updated_user = await User.get(id)
    return updated_user


@router.delete("/{id}")
async def delete_user(id: UUID):
    user = await User.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    await user.delete()
    return {"message": "User deleted successfully"}
