import time
from controller import collect_climate_data, add_weather_to_db, api_key, BRAZILIAN_CAPITALS


N = 6  # vezes por dia
INTERVALO = 86400 // N  # segundos

def main():
    while True:
        print("[INFO] Iniciando nova coleta de dados...")
        dados = collect_climate_data(api_key, BRAZILIAN_CAPITALS)

        for capital, weather in dados.items():
            if weather is None:
                print(f"[WARNING] Dados não disponíveis para {capital}, pulando.")
                continue
            add_weather_to_db(weather)

        print(f"[INFO] Aguardando {INTERVALO} segundos até a próxima coleta...\n")
        time.sleep(INTERVALO)

if __name__ == '__main__':
    main()
