"""
Rotas da API REST
Endpoints para integração e funcionalidades
"""
from flask import Blueprint, jsonify, request
from services.api_caixa_service import ApiCaixaService
from services.estatistica_service import EstatisticaService
from services.megasena_service import MegaSenaService
from models.resultado_model import ResultadoModel

api_bp = Blueprint('api', __name__, url_prefix='/api')

# Inicializa services
api_caixa_service = ApiCaixaService()
estatistica_service = EstatisticaService()
megasena_service = MegaSenaService()
model = ResultadoModel()


@api_bp.route('/atualizar', methods=['POST'])
def atualizar():
    """Atualiza base de dados com concursos da API"""
    resultado = api_caixa_service.atualizar_base_completa()
    return jsonify(resultado)


@api_bp.route('/ultimo-resultado', methods=['GET'])
def ultimo_resultado():
    """Retorna último resultado cadastrado"""
    resultado = model.buscar_ultimo()
    
    if resultado:
        return jsonify({
            'sucesso': True,
            'resultado': resultado
        })
    
    return jsonify({
        'sucesso': False,
        'mensagem': 'Nenhum resultado encontrado'
    }), 404


@api_bp.route('/resultados', methods=['GET'])
def resultados():
    """Lista todos os resultados"""
    limite = request.args.get('limite', type=int)
    resultados = model.buscar_todos(limite)
    
    return jsonify({
        'sucesso': True,
        'total': len(resultados),
        'resultados': resultados
    })


@api_bp.route('/resultado/<int:numero>', methods=['GET'])
def resultado_especifico(numero):
    """Busca resultado de concurso específico"""
    resultado = model.buscar_por_numero(numero)
    
    if resultado:
        return jsonify({
            'sucesso': True,
            'resultado': resultado
        })
    
    return jsonify({
        'sucesso': False,
        'mensagem': f'Concurso {numero} não encontrado'
    }), 404


@api_bp.route('/estatisticas', methods=['GET'])
def estatisticas():
    """Retorna estatísticas completas"""
    stats = estatistica_service.calcular_estatisticas_completas()
    
    return jsonify({
        'sucesso': True,
        'estatisticas': stats
    })


@api_bp.route('/gerar-palpite', methods=['POST'])
def gerar_palpite():
    """Gera palpites baseados em estratégia"""
    data = request.get_json()
    
    estrategia = data.get('estrategia', 'equilibrada')
    quantidade_numeros = data.get('quantidade_numeros', 6)
    quantidade_jogos = data.get('quantidade_jogos', 1)
    
    resultado = megasena_service.gerar_palpite(
        estrategia=estrategia,
        quantidade_numeros=quantidade_numeros,
        quantidade_jogos=quantidade_jogos
    )
    
    return jsonify(resultado)


@api_bp.route('/conferir', methods=['POST'])
def conferir():
    """Confere palpite com resultado de concurso"""
    data = request.get_json()
    
    numeros = data.get('numeros', [])
    concurso = data.get('concurso')
    
    if not numeros or not concurso:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Parâmetros inválidos. Informe numeros e concurso.'
        }), 400
    
    resultado = megasena_service.conferir_jogo(numeros, concurso)
    
    return jsonify(resultado)


@api_bp.route('/status', methods=['GET'])
def status():
    """Status da aplicação"""
    total_concursos = model.contar_resultados()
    ultimo = model.buscar_ultimo()
    
    return jsonify({
        'sucesso': True,
        'status': 'online',
        'total_concursos': total_concursos,
        'ultimo_concurso': ultimo['numero'] if ultimo else None
    })
