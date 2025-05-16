# Projeto_One_Weather
ClimaBR: Monitoramento Climático das Capitais Brasileiras

Objetivo:
Este projeto foi desenvolvido como parte dos meus estudos, de forma prática, os conceitos fundamentais de engenharia de dados e construção de sistemas bem estruturados. Ele simula um sistema de coleta climática contínua e automatizada, com foco em qualidade, organização e boas práticas.

Tecnologias Utilizadas
Categoria	Ferramentas/Tecnologias
Coleta de Dados	requests, API OpenWeather
Validação	Pydantic
Armazenamento	SQLAlchemy, SQLite
Estrutura	Padrão MVC
Documentação	README.md

Funcionalidades
Coleta automática e periódica de dados climáticos das 27 capitais do Brasil.

Informações coletadas:

Nome da cidade

Temperatura atual

Descrição do clima

Data e hora da coleta

Dados persistidos localmente via SQLite.

Agendamento de coleta 

Arquitetura MVC
Model: Banco de dados com SQLAlchemy.

View: Validação com Pydantic.

Controller: Orquestra lógica, coleta e persistência.

🛡️ Qualidade e Segurança
Uso de variáveis de ambiente (.env) para proteger chaves de API.

Validação dos dados recebidos.

Estrutura modular para facilitar manutenção e escalabilidade.

🔄 Expansões Futuras
Visualização com dashboards (ex: Power BI, Streamlit)

Notificações por e-mail ou SMS em caso de extremos climáticos

Suporte a múltiplas cidades e países

# -weather_monitoring_brazilian_capitals
# -weather_monitoring_brazilian_capitals
