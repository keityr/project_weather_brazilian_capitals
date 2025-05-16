import requests 
from schema import WeatherSchema
from models import Weather
from db import SessionLocal, Base, engine
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

Base.metadata.create_all(bind=engine)

#Lista de capitais do Brazil
BRAZILIAN_CAPITALS = [
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília",
    "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte",
    "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro",
    "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis",
    "São Paulo", "Aracaju", "Palmas"
]

# Itera para pegar todas as capitais 
def collect_climate_data(api_key, BRAZILIAN_CAPITALS) -> WeatherSchema:

    resultado ={}
    for capital in BRAZILIAN_CAPITALS:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={capital}&appid={api_key}"
        
        #Conecta e traz a API
        response = requests.get(url)
        response_json = response.json()

        #Confirma se a conexao foi bem sucedida, se sim retorna as informações
        if response.status_code == 200:
            description = response_json["weather"][0]["description"]
            temperature = response_json["main"]["temp"]
            temp_celsius =temperature - 273.15
            #Transforma em celsius
            resultado[capital] = WeatherSchema(
                capital_city=capital,
                temp=round(temp_celsius, 2),
                description=description
            )
            
        else:
            None
        
    return resultado


def add_weather_to_db(weather_schema: WeatherSchema) -> Weather:  
    with SessionLocal()  as db:
        db_weather = Weather(capital_city=weather_schema.capital_city,description=weather_schema.description, temp=weather_schema.temp )
        db.add(db_weather)
        db.commit()
        db.refresh(db_weather)
    return  db_weather

 


