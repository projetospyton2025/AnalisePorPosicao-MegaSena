"""
Aplicação principal Flask - Sistema Quina
Servidor rodando na porta 5056
"""
from flask import Flask
from config import Config
from routes.main_routes import main_bp
from routes.api_routes import api_bp


def create_app():
    """Factory para criar a aplicação Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Registra blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    print(f"""
    ═══════════════════════════════════════════════════
    🎲 Sistema Quina - Análise por Posição
    ═══════════════════════════════════════════════════
    
    ✓ Servidor rodando em: http://{Config.HOST}:{Config.PORT}
    ✓ Modo Debug: {Config.DEBUG}
    ✓ Banco de dados: {Config.DATABASE_PATH}
    
    Acesse: http://localhost:{Config.PORT}
    ═══════════════════════════════════════════════════
    """)
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
