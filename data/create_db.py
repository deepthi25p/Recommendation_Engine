from data.database import engine
from data.models import Base

Base.metadata.create_all(bind=engine)

print("Database created successfully!")