"""
Service para geração de palpites da Mega-Sena
Implementa diferentes estratégias baseadas em estatísticas reais
"""
import random
from typing import Dict, List, Set
from config import Config
from services.estatistica_service import EstatisticaService
from models.resultado_model import ResultadoModel


class MegaSenaService:
    """Service para geração e conferência de palpites"""
    
    def __init__(self):
        self.estatistica_service = EstatisticaService()
        self.model = ResultadoModel()
    
    def gerar_palpite(
        self,
        estrategia: str = 'equilibrada',
        quantidade_numeros: int = 6,
        quantidade_jogos: int = 1
    ) -> Dict:
        """
        Gera palpites baseados na estratégia escolhida
        
        Args:
            estrategia: Tipo de estratégia (equilibrada, agressiva, conservadora, etc)
            quantidade_numeros: Quantidade de números por jogo (6-20)
            quantidade_jogos: Quantidade de jogos a gerar
            
        Returns:
            Dict com os jogos gerados e informações
        """
        # Valida parâmetros
        if quantidade_numeros < Config.MIN_JOGO or quantidade_numeros > Config.MAX_JOGO:
            return {
                'sucesso': False,
                'mensagem': f'Quantidade de números deve estar entre {Config.MIN_JOGO} e {Config.MAX_JOGO}'
            }
        
        if quantidade_jogos < 1 or quantidade_jogos > 100:
            return {
                'sucesso': False,
                'mensagem': 'Quantidade de jogos deve estar entre 1 e 100'
            }
        
        # Busca estatísticas
        stats = self.estatistica_service.calcular_estatisticas_completas()
        
        if stats['total_concursos'] == 0:
            return {
                'sucesso': False,
                'mensagem': 'Não há dados suficientes para gerar palpites. Atualize a base de dados.'
            }
        
        # Gera jogos
        jogos = []
        for _ in range(quantidade_jogos):
            numeros = self._gerar_por_estrategia(estrategia, quantidade_numeros, stats)
            jogos.append(sorted(numeros))
        
        return {
            'sucesso': True,
            'estrategia': estrategia,
            'quantidade_numeros': quantidade_numeros,
            'quantidade_jogos': quantidade_jogos,
            'jogos': jogos
        }
    
    def _gerar_por_estrategia(
        self,
        estrategia: str,
        quantidade: int,
        stats: Dict
    ) -> List[int]:
        """
        Gera números baseado na estratégia
        
        Args:
            estrategia: Nome da estratégia
            quantidade: Quantidade de números
            stats: Estatísticas calculadas
            
        Returns:
            Lista de números gerados
        """
        estrategias = {
            'equilibrada': self._estrategia_equilibrada,
            'agressiva': self._estrategia_agressiva,
            'conservadora': self._estrategia_conservadora,
            'mista': self._estrategia_mista,
            'atrasados': self._estrategia_atrasados,
            'por_faixa': self._estrategia_por_faixa,
            'por_digito': self._estrategia_por_digito,
            'aleatoria': self._estrategia_aleatoria
        }
        
        funcao = estrategias.get(estrategia, self._estrategia_equilibrada)
        return funcao(quantidade, stats)
    
    def _estrategia_equilibrada(self, quantidade: int, stats: Dict) -> List[int]:
        """60% quentes + 40% frios"""
        frequencia = stats['frequencia']
        
        quentes = [item['numero'] for item in frequencia['mais_frequentes'][:30]]
        frios = [item['numero'] for item in frequencia['menos_frequentes'][:30]]
        
        qtd_quentes = int(quantidade * 0.6)
        qtd_frios = quantidade - qtd_quentes
        
        numeros = set()
        numeros.update(random.sample(quentes, min(qtd_quentes, len(quentes))))
        numeros.update(random.sample(frios, min(qtd_frios, len(frios))))
        
        # Completa se necessário
        while len(numeros) < quantidade:
            numeros.add(random.randint(1, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _estrategia_agressiva(self, quantidade: int, stats: Dict) -> List[int]:
        """80% quentes + 20% frios"""
        frequencia = stats['frequencia']
        
        quentes = [item['numero'] for item in frequencia['mais_frequentes'][:30]]
        frios = [item['numero'] for item in frequencia['menos_frequentes'][:30]]
        
        qtd_quentes = int(quantidade * 0.8)
        qtd_frios = quantidade - qtd_quentes
        
        numeros = set()
        numeros.update(random.sample(quentes, min(qtd_quentes, len(quentes))))
        numeros.update(random.sample(frios, min(qtd_frios, len(frios))))
        
        while len(numeros) < quantidade:
            numeros.add(random.randint(1, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _estrategia_conservadora(self, quantidade: int, stats: Dict) -> List[int]:
        """40% quentes + 60% frios"""
        frequencia = stats['frequencia']
        
        quentes = [item['numero'] for item in frequencia['mais_frequentes'][:30]]
        frios = [item['numero'] for item in frequencia['menos_frequentes'][:30]]
        
        qtd_quentes = int(quantidade * 0.4)
        qtd_frios = quantidade - qtd_quentes
        
        numeros = set()
        numeros.update(random.sample(quentes, min(qtd_quentes, len(quentes))))
        numeros.update(random.sample(frios, min(qtd_frios, len(frios))))
        
        while len(numeros) < quantidade:
            numeros.add(random.randint(1, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _estrategia_mista(self, quantidade: int, stats: Dict) -> List[int]:
        """Distribui uniformemente por todas as faixas"""
        faixas = stats['por_faixa']['faixas']
        numeros = set()
        
        # Tenta pegar pelo menos 1 número de cada faixa
        for faixa in faixas:
            range_parts = faixa['range'].split('-')
            min_num = int(range_parts[0])
            max_num = int(range_parts[1]) if len(range_parts) > 1 else min_num
            
            if len(numeros) < quantidade:
                numeros.add(random.randint(min_num, max_num))
        
        # Completa aleatoriamente
        while len(numeros) < quantidade:
            numeros.add(random.randint(1, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _estrategia_atrasados(self, quantidade: int, stats: Dict) -> List[int]:
        """Foca em números com maior atraso"""
        atrasados = stats['atrasos']['mais_atrasados'][:40]
        numeros_atrasados = [item['numero'] for item in atrasados]
        
        numeros = set(random.sample(numeros_atrasados, min(quantidade, len(numeros_atrasados))))
        
        while len(numeros) < quantidade:
            numeros.add(random.randint(1, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _estrategia_por_faixa(self, quantidade: int, stats: Dict) -> List[int]:
        """Garante pelo menos um número de cada faixa"""
        faixas_ranges = [
            (1, 10), (11, 20), (21, 30),
            (31, 40), (41, 50), (51, 60)
        ]
        
        numeros = set()
        numeros_por_faixa = max(1, quantidade // 6)
        
        for min_num, max_num in faixas_ranges:
            for _ in range(numeros_por_faixa):
                if len(numeros) < quantidade:
                    numeros.add(random.randint(min_num, max_num))
        
        # Completa se necessário
        while len(numeros) < quantidade:
            numeros.add(random.randint(1, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _estrategia_por_digito(self, quantidade: int, stats: Dict) -> List[int]:
        """Distribui por primeiro dígito"""
        digitos_ranges = [
            (1, 9), (10, 19), (20, 29),
            (30, 39), (40, 49), (50, 60)
        ]
        
        numeros = set()
        numeros_por_digito = max(1, quantidade // 6)
        
        for min_num, max_num in digitos_ranges:
            for _ in range(numeros_por_digito):
                if len(numeros) < quantidade:
                    numeros.add(random.randint(min_num, max_num))
        
        while len(numeros) < quantidade:
            numeros.add(random.randint(1, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _estrategia_aleatoria(self, quantidade: int, stats: Dict) -> List[int]:
        """Seleção completamente aleatória"""
        return random.sample(range(1, Config.MAX_NUMEROS + 1), quantidade)
    
    def conferir_jogo(self, numeros: List[int], numero_concurso: int) -> Dict:
        """
        Confere um jogo com o resultado de um concurso
        
        Args:
            numeros: Lista de números do jogo
            numero_concurso: Número do concurso para conferir
            
        Returns:
            Dict com resultado da conferência
        """
        # Valida números
        if not numeros or len(numeros) < Config.MIN_JOGO or len(numeros) > Config.MAX_JOGO:
            return {
                'sucesso': False,
                'mensagem': f'Jogo deve ter entre {Config.MIN_JOGO} e {Config.MAX_JOGO} números'
            }
        
        # Valida números únicos e dentro do range
        numeros_set = set(numeros)
        if len(numeros_set) != len(numeros):
            return {
                'sucesso': False,
                'mensagem': 'Jogo contém números duplicados'
            }
        
        if any(n < 1 or n > Config.MAX_NUMEROS for n in numeros):
            return {
                'sucesso': False,
                'mensagem': f'Todos os números devem estar entre 1 e {Config.MAX_NUMEROS}'
            }
        
        # Busca resultado
        resultado = self.model.buscar_por_numero(numero_concurso)
        
        if not resultado:
            return {
                'sucesso': False,
                'mensagem': f'Concurso {numero_concurso} não encontrado'
            }
        
        # Confere acertos
        sorteados = [int(d) for d in resultado['listaDezenas']]
        acertos = [n for n in numeros if n in sorteados]
        qtd_acertos = len(acertos)
        
        # Define premiação
        premiacao = None
        if qtd_acertos == 6:
            premiacao = 'Sena (6 acertos)'
        elif qtd_acertos == 5:
            premiacao = 'Quina (5 acertos)'
        elif qtd_acertos == 4:
            premiacao = 'Quadra (4 acertos)'
        
        return {
            'sucesso': True,
            'concurso': numero_concurso,
            'data': resultado['dataApuracao'],
            'numeros_jogo': sorted(numeros),
            'numeros_sorteados': sorteados,
            'acertos': sorted(acertos),
            'quantidade_acertos': qtd_acertos,
            'premiacao': premiacao
        }
