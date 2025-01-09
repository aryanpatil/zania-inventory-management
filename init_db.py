from app.route import products, orders
from app.db import engine
from app.models import Base


# Initialise the database
Base.metadata.create_all(bind=engine)
print("DATABASE Initialised!!!!!")