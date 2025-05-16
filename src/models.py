#Fazer o schema da minha tabela no db
from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.sql import func
from db import Base

class Weather(Base):
    __tablename__ = 'brazil_weather'
    id =Column(Integer, primary_key=True, index=True)
    capital_city=Column(String)
    description = Column(String)
    temp = Column(Float)
    created_at =Column(DateTime, default=func.now())