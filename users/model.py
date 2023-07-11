from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()
engine =create_engine(os.environ.get("USER_DB"))
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(BigInteger)
    location = Column(String(200))
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_superuser = Column(Boolean, default=False)




