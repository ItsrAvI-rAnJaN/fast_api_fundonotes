from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/fundoo_notes_fastapi")
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


