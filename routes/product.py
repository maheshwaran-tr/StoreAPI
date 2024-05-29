from fastapi import APIRouter
from config.database import product_collection
from schemas.product import single_serial, multi_serial
from models.product import Product
from bson import ObjectId


prodcut_router = APIRouter(prefix="/products", tags=["Products"])


# fetching all products
@prodcut_router.get("/")
async def find_all_products():
    all_products = multi_serial(product_collection.find())
    return all_products


# find one product
@prodcut_router.get("/{id}")
async def find_one_prodcut(id: str):
    deleted_product = product_collection.find_one({"_id": ObjectId(id)})
    return single_serial(deleted_product)


# creating a product
@prodcut_router.post("/")
async def create_product(new_product: Product):
    created_product = product_collection.insert_one(dict(new_product))
    return single_serial(
        product_collection.find_one({"_id": ObjectId(created_product.inserted_id)})
    )


# update product
@prodcut_router.put("/{id}")
async def update_product(id: str, product: Product):
    updated_product = product_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(product)}
    )
    return single_serial(updated_product)


# delete product
@prodcut_router.delete("/{id}")
async def delete_prodcut(id: str):
    deleted_product = product_collection.find_one_and_delete({"_id": ObjectId(id)})
    return single_serial(deleted_product)