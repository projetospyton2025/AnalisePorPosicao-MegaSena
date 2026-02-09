"""
Service para cálculo de estatísticas da Quina
Análises: frequência, atrasos, pares/ímpares, por faixa, por dígito, por posição
"""
from typing import Dict, List
from collections import Counter, defaultdict
from models.resultado_model import ResultadoModel
from config import Config


class EstatisticaService:
    """Service para análises estatísticas da Quina"""
    
    def __init__(self):
        self.model = ResultadoModel()
    
    def calcular_estatisticas_completas(self) -> Dict:
        """
        Calcula todas as estatísticas disponíveis
        
        Returns:
            Dict com todas as estatísticas
        """
        resultados = self.model.buscar_todos()
        
        if not resultados:
            return self._estatisticas_vazias()
        
        return {
            'total_concursos': len(resultados),
            'frequencia': self.calcular_frequencia_numeros(resultados),
            'atrasos': self.calcular_atrasos(resultados),
            'pares_impares': self.calcular_pares_impares(resultados),
            'por_faixa': self.calcular_por_faixa(resultados),
            'por_digito': self.calcular_por_digito(resultados),
            'por_posicao_sorteio': self.calcular_por_posicao_sorteio(resultados)
        }
    
    def calcular_frequencia_numeros(self, resultados: List[Dict]) -> Dict:
        """
        Calcula frequência de cada número (01-80)
        
        Args:
            resultados: Lista de resultados
            
        Returns:
            Dict com frequência de cada número
        """
        frequencias = Counter()
        total_sorteios = len(resultados) * Config.NUMEROS_SORTEADOS
        
        for resultado in resultados:
            dezenas = [int(d) for d in resultado.get('listaDezenas', [])]
            frequencias.update(dezenas)
        
        # Monta lista completa de 1 a 80
        frequencia_completa = []
        for num in range(1, Config.MAX_NUMEROS + 1):
            count = frequencias.get(num, 0)
            percentual = (count / len(resultados) * 100) if len(resultados) > 0 else 0
            
            frequencia_completa.append({
                'numero': num,
                'frequencia': count,
                'percentual': round(percentual, 2)
            })
        
        # Ordena por frequência decrescente
        frequencia_ordenada = sorted(
            frequencia_completa,
            key=lambda x: x['frequencia'],
            reverse=True
        )
        
        return {
            'todos': frequencia_completa,
            'ordenado': frequencia_ordenada,
            'mais_frequentes': frequencia_ordenada[:20],
            'menos_frequentes': frequencia_ordenada[-20:]
        }
    
    def calcular_atrasos(self, resultados: List[Dict]) -> Dict:
        """
        Calcula atraso de cada número (concursos sem aparecer)
        
        Args:
            resultados: Lista de resultados
            
        Returns:
            Dict com atraso de cada número
        """
        # Inicializa atrasos com o número total de concursos
        atrasos = {num: len(resultados) for num in range(1, Config.MAX_NUMEROS + 1)}
        
        # Percorre resultados do mais recente ao mais antigo
        for idx, resultado in enumerate(resultados):
            dezenas = [int(d) for d in resultado.get('listaDezenas', [])]
            
            for dezena in dezenas:
                # Se ainda não atualizamos o atraso deste número
                if atrasos[dezena] == len(resultados):
                    atrasos[dezena] = idx
        
        # Converte para lista de dicts
        atrasos_lista = [
            {
                'numero': num,
                'atraso': atraso
            }
            for num, atraso in atrasos.items()
        ]
        
        # Ordena por atraso (mais atrasados primeiro)
        atrasos_ordenados = sorted(
            atrasos_lista,
            key=lambda x: x['atraso'],
            reverse=True
        )
        
        return {
            'todos': atrasos_lista,
            'mais_atrasados': atrasos_ordenados[:20]
        }
    
    def calcular_pares_impares(self, resultados: List[Dict]) -> Dict:
        """
        Calcula distribuição de números pares e ímpares
        
        Args:
            resultados: Lista de resultados
            
        Returns:
            Dict com estatísticas de pares/ímpares
        """
        distribuicao = Counter()
        
        for resultado in resultados:
            dezenas = [int(d) for d in resultado.get('listaDezenas', [])]
            pares = sum(1 for d in dezenas if d % 2 == 0)
            impares = len(dezenas) - pares
            
            # Formato: "3P-3I" (3 pares, 3 ímpares)
            chave = f"{pares}P-{impares}I"
            distribuicao[chave] += 1
        
        total = len(resultados)
        distribuicao_lista = []
        
        for padrao, count in distribuicao.most_common():
            distribuicao_lista.append({
                'padrao': padrao,
                'ocorrencias': count,
                'percentual': round((count / total * 100), 2) if total > 0 else 0
            })
        
        return {
            'distribuicao': distribuicao_lista,
            'mais_comum': distribuicao_lista[0] if distribuicao_lista else None
        }
    
    def calcular_por_faixa(self, resultados: List[Dict]) -> Dict:
        """
        Calcula distribuição por faixas de números
        Faixa 1: 01-16, Faixa 2: 17-32, Faixa 3: 33-48, Faixa 4: 49-64, Faixa 5: 65-80
        
        Args:
            resultados: Lista de resultados
            
        Returns:
            Dict com estatísticas por faixa
        """
        faixas = {
            1: {'range': '01-16', 'min': 1, 'max': 16, 'count': 0},
            2: {'range': '17-32', 'min': 17, 'max': 32, 'count': 0},
            3: {'range': '33-48', 'min': 33, 'max': 48, 'count': 0},
            4: {'range': '49-64', 'min': 49, 'max': 64, 'count': 0},
            5: {'range': '65-80', 'min': 65, 'max': 80, 'count': 0}
        }
        
        for resultado in resultados:
            dezenas = [int(d) for d in resultado.get('listaDezenas', [])]
            
            for dezena in dezenas:
                for faixa_num, faixa_info in faixas.items():
                    if faixa_info['min'] <= dezena <= faixa_info['max']:
                        faixa_info['count'] += 1
                        break
        
        total_numeros = len(resultados) * Config.NUMEROS_SORTEADOS
        
        # Converte para lista
        faixas_lista = []
        for faixa_num in sorted(faixas.keys()):
            faixa = faixas[faixa_num]
            percentual = (faixa['count'] / total_numeros * 100) if total_numeros > 0 else 0
            
            faixas_lista.append({
                'faixa': faixa_num,
                'range': faixa['range'],
                'ocorrencias': faixa['count'],
                'percentual': round(percentual, 2)
            })
        
        return {
            'faixas': faixas_lista
        }
    
    def calcular_por_digito(self, resultados: List[Dict]) -> Dict:
        """
        Calcula distribuição por primeiro dígito
        Dígito 0: 01-09, Dígito 1: 10-19, ..., Dígito 7: 70-80
        
        Args:
            resultados: Lista de resultados
            
        Returns:
            Dict com estatísticas por dígito
        """
        digitos = {
            0: {'range': '01-09', 'count': 0},
            1: {'range': '10-19', 'count': 0},
            2: {'range': '20-29', 'count': 0},
            3: {'range': '30-39', 'count': 0},
            4: {'range': '40-49', 'count': 0},
            5: {'range': '50-59', 'count': 0},
            6: {'range': '60-69', 'count': 0},
            7: {'range': '70-80', 'count': 0}
        }
        
        for resultado in resultados:
            dezenas = [int(d) for d in resultado.get('listaDezenas', [])]
            
            for dezena in dezenas:
                if dezena >= 70:
                    digitos[7]['count'] += 1
                else:
                    primeiro_digito = dezena // 10
                    digitos[primeiro_digito]['count'] += 1
        
        total_numeros = len(resultados) * Config.NUMEROS_SORTEADOS
        
        # Converte para lista
        digitos_lista = []
        for digito_num in sorted(digitos.keys()):
            digito = digitos[digito_num]
            percentual = (digito['count'] / total_numeros * 100) if total_numeros > 0 else 0
            
            digitos_lista.append({
                'digito': digito_num,
                'range': digito['range'],
                'ocorrencias': digito['count'],
                'percentual': round(percentual, 2)
            })
        
        return {
            'digitos': digitos_lista
        }
    
    def calcular_por_posicao_sorteio(self, resultados: List[Dict]) -> Dict:
        """
        Calcula estatísticas por posição do sorteio (1ª a 5ª bola)
        Usa dezenasSorteadasOrdemSorteio da API
        
        Args:
            resultados: Lista de resultados
            
        Returns:
            Dict com estatísticas por posição
        """
        posicoes = {i: Counter() for i in range(1, 6)}
        
        for resultado in resultados:
            dezenas_ordem = resultado.get('dezenasSorteadasOrdemSorteio', [])
            
            for idx, dezena in enumerate(dezenas_ordem, start=1):
                if idx <= 5:
                    posicoes[idx][int(dezena)] += 1
        
        # Monta estatísticas por posição
        posicoes_lista = []
        for pos in range(1, 6):
            top_numeros = []
            
            for numero, count in posicoes[pos].most_common(10):
                top_numeros.append({
                    'numero': numero,
                    'frequencia': count
                })
            
            posicoes_lista.append({
                'posicao': pos,
                'top_numeros': top_numeros
            })
        
        return {
            'posicoes': posicoes_lista
        }
    
    def _estatisticas_vazias(self) -> Dict:
        """
        Retorna estrutura vazia de estatísticas
        
        Returns:
            Dict com estrutura vazia
        """
        return {
            'total_concursos': 0,
            'frequencia': {'todos': [], 'ordenado': [], 'mais_frequentes': [], 'menos_frequentes': []},
            'atrasos': {'todos': [], 'mais_atrasados': []},
            'pares_impares': {'distribuicao': [], 'mais_comum': None},
            'por_faixa': {'faixas': []},
            'por_digito': {'digitos': []},
            'por_posicao_sorteio': {'posicoes': []}
        }
