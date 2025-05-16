from pydantic import BaseModel


class WeatherSchema(BaseModel): #Contrato de dados
    description: str
    temp: float
    capital_city: str

    class Config:
        from_attributes = True