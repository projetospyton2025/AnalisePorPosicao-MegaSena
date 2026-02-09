"""
Configurações da aplicação Mega-Sena
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações gerais da aplicação"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # Server
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5056))
    
    # Database
    DATABASE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.getenv('DATABASE_PATH', 'database.db')
    )
    
    # API
    API_MEGASENA_URL = os.getenv(
        'API_MEGASENA_URL',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena'
    )
    
    # Mega-Sena Rules
    MIN_NUMEROS = 1
    MAX_NUMEROS = 60
    NUMEROS_SORTEADOS = 6
    MIN_JOGO = 6
    MAX_JOGO = 20
