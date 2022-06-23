from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON


Base = declarative_base()


class MemberModel(Base):
    __tablename__ = "Members"

    beatle_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    custom_information = Column(JSON)
