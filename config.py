"""
Configurações da aplicação Quina
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
    API_QUINA_URL = os.getenv(
        'API_QUINA_URL',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/quina'
    )
    
    # Quina Rules
    MIN_NUMEROS = 1
    MAX_NUMEROS = 80
    NUMEROS_SORTEADOS = 5
    MIN_JOGO = 5
    MAX_JOGO = 15
