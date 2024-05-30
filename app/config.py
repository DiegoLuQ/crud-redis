from pathlib import Path
from dotenv import load_dotenv
from os import environ

"""
TENEMOS CONFIGURADO NUESTRAS VARIABLES DE ENTORNO
"""

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)


class Settings:
    HOST = environ.get('HOST')
    PORT = environ.get('PORT')
    


settings = Settings()