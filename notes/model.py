from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


Base = declarative_base()
engine =create_engine(os.environ.get("NOTE_DB"))
Base.metadata.create_all(engine)
note_session = sessionmaker(bind=engine, autoflushcr=False, autocommit=False)



def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()



class Note(Base):
    __tablename__="notes"

    id =Column(Integer,primary_key=True,index=True)
    tittle=Column(String(100))
    description=Column(String(200))
    color=Column(String(50))
    user_id = Column(BigInteger, nullable=False)