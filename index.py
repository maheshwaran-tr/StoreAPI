from fastapi import FastAPI
from routes.product import prodcut_router
from routes.user import user_router
app = FastAPI(title="StoreAPI")

app.include_router(user_router)
app.include_router(prodcut_router)