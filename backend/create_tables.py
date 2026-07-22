from backend.models import Base
from backend.database import engine

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")