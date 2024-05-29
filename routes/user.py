from fastapi import APIRouter
from config.database import user_collection
from schemas.user import single_serial, multi_serial
from models.user import User
from bson import ObjectId


user_router = APIRouter(prefix="/users", tags=["Users"])


# fetching all users
@user_router.get("/")
async def find_all_users():
    all_users = multi_serial(user_collection.find())
    return all_users


# find one user
@user_router.get("/{id}")
async def find_one_prodcut(id: str):
    return single_serial(user_collection.find_one({"_id": ObjectId(id)}))


# creating a user
@user_router.post("/")
async def create_user(new_user: User):
    created_user = user_collection.insert_one(dict(new_user))
    return single_serial(
        user_collection.find_one({"_id": ObjectId(created_user.inserted_id)})
    )


# update user
@user_router.put("/{id}")
async def update_user(id: str, user: User):
    user_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return single_serial(user_collection.find_one({"_id": ObjectId(id)}))


# delete user
@user_router.delete("/{id}")
async def delete_prodcut(id: str):
    deleted_user = user_collection.find_one_and_delete({"_id": ObjectId(id)})
    return single_serial(deleted_user)
