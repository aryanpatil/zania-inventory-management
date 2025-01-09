from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.route import products, orders
from app.db import engine
from app.models import Base


# Initialise the database
Base.metadata.create_all(bind=engine)
print("DATABASE Initialised!!!!!")

app = FastAPI(title="Product Management API")

# Intialising routes
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# Redirect hoempage to Swagger UI
@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')