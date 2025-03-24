from sqlalchemy import create_engine, Column, String, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set! Check your environment variables.")

# Set up database connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define SQL table model
class Name(Base):
    __tablename__ = "names"
    name = Column(String, primary_key=True, index=True)

# Create table if it doesn’t exist
Base.metadata.create_all(engine)
print(f"Connected to database: {engine.url}")

def load_names_into_db(file_path="data/results.txt"):
    """Load names from results.txt into PostgreSQL only if the table is empty."""
    session = SessionLocal()
    try:
        # Check if the table already has data
        if session.query(Name).count() > 0:
            print("Database already has names. Skipping loading.")
            return

        with open(file_path, "r") as file:
            names = [line.strip().lower() for line in file]

        insert_query = text("""
        INSERT INTO names (name) VALUES (:name)
        ON CONFLICT (name) DO NOTHING;
        """)
        session.execute(insert_query, [{"name": name} for name in names])
        session.commit()
        print("Names inserted successfully into PostgreSQL!")
    except Exception as e:
        print(f"Error inserting names: {str(e)}")
    finally:
        session.close()

def search_names(prefix, limit=10):
    """Search names by prefix from the database."""
    session = SessionLocal()
    try:
        results = session.query(Name).filter(Name.name.startswith(prefix.lower())).limit(limit).all()
        return [row.name for row in results]
    finally:
        session.close()
