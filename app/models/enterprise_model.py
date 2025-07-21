from sqlalchemy import Column, Float, Integer, String

from app.database.connection import Base


class Enterprise(Base):
    __tablename__ = 'enterprises'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    year_of_foundation = Column(Integer, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    telephone = Column(String, nullable=False)
    social_value = Column(Float, nullable=False)
