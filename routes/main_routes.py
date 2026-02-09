"""
Rotas principais da aplicação (páginas HTML)
"""
from flask import Blueprint, render_template
from models.resultado_model import ResultadoModel

main_bp = Blueprint('main', __name__)
model = ResultadoModel()


@main_bp.route('/')
def index():
    """Página principal com resultados"""
    return render_template('index.html')


@main_bp.route('/palpites')
def palpites():
    """Página de geração e análise de palpites"""
    return render_template('palpites.html')
