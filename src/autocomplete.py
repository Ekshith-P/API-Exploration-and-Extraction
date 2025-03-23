from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os

# Set up database connection (replace with your database URI)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://pakalaekshith:Bittu39@localhost:5432/apiexploration")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define SQL table model
class Name(Base):
    __tablename__ = "names"
    name = Column(String, primary_key=True, index=True)

# Create table if it doesn’t exist
Base.metadata.create_all(engine)

# Debugging: Print the database URL
print(f"🔍 Connecting to database: {engine.url}")

def load_names_into_db(file_path):
    session = SessionLocal()
    try:
        with open(file_path, "r") as file:
            for line in file:
                name = line.strip().lower()
                print(f"🔹 Trying to insert: {name}")  # DEBUG: Print each name
                
                # Check if the name already exists
                existing_name = session.query(Name).filter_by(name=name).first()
                if existing_name:
                    print(f"Skipping (already exists): {name}")
                else:
                    session.add(Name(name=name))

        session.commit()
        print("Names inserted successfully!")
    except Exception as e:
        print(f"Error inserting names: {str(e)}")
    finally:
        session.close()


def search_names(prefix, limit=10):
    """Search names by prefix from the database"""
    session = SessionLocal()
    results = session.query(Name).filter(Name.name.startswith(prefix.lower())).limit(limit).all()
    session.close()
    return [row.name for row in results]

# Example usage (if you want to test the functions)
# file_path = "names.txt"  # Replace with your file path
# load_names_into_db(file_path)

# Example search
# search_results = search_names("app")
# print(search_results)