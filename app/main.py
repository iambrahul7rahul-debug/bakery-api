from fastapi import FastAPI
from app.database import Base, engine
from app.routes.product import router as product_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bakery API")

app.include_router(product_router)

@app.get("/")
def home():
    return {"message": "Bakery API is running"}
