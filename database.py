from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://root:bruh123!@database-1.c7sc0i4407ns.us-east-1.rds.amazonaws.com:5432/postgres"
# So, this databse info should be in an env file and should be loaded, but for the sake of quickness, I did not do it, but
# obvi, normally I would!
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
