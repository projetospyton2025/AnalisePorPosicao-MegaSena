"""
Service para integração com a API oficial da Caixa Econômica Federal
Endpoint: https://servicebus2.caixa.gov.br/portaldeloterias/api/quina
"""
import requests
from typing import Dict, List, Optional
from config import Config
from models.resultado_model import ResultadoModel


class ApiCaixaService:
    """Service para consumir a API da Caixa"""
    
    def __init__(self):
        self.base_url = Config.API_QUINA_URL
        self.model = ResultadoModel()
    
    def buscar_ultimo_concurso(self) -> Optional[Dict]:
        """
        Busca o último concurso da Quina
        
        Returns:
            Dict com dados do último concurso ou None em caso de erro
        """
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar último concurso: {e}")
            return None
        except ValueError as e:
            print(f"Erro ao decodificar JSON: {e}")
            return None
    
    def buscar_concurso_especifico(self, numero: int) -> Optional[Dict]:
        """
        Busca um concurso específico pelo número
        
        Args:
            numero: Número do concurso
            
        Returns:
            Dict com dados do concurso ou None em caso de erro
        """
        try:
            url = f"{self.base_url}/{numero}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar concurso {numero}: {e}")
            return None
        except ValueError as e:
            print(f"Erro ao decodificar JSON do concurso {numero}: {e}")
            return None
    
    def atualizar_base_completa(self) -> Dict[str, any]:
        """
        Atualiza a base de dados com todos os concursos disponíveis
        Faz atualização incremental a partir do último concurso no banco
        
        Returns:
            Dict com estatísticas da atualização
        """
        resultado = {
            'sucesso': False,
            'total_inseridos': 0,
            'total_erros': 0,
            'ultimo_concurso': None,
            'mensagem': ''
        }
        
        try:
            # Busca último concurso da API
            ultimo_api = self.buscar_ultimo_concurso()
            
            if not ultimo_api:
                resultado['mensagem'] = 'Erro ao buscar último concurso da API'
                return resultado
            
            numero_ultimo_api = ultimo_api.get('numero', 0)
            
            if numero_ultimo_api == 0:
                resultado['mensagem'] = 'Número do último concurso inválido'
                return resultado
            
            # Verifica último concurso no banco
            ultimo_banco = self.model.buscar_ultimo()
            numero_inicio = 1
            
            if ultimo_banco:
                numero_inicio = ultimo_banco['numero'] + 1
            
            # Se já está atualizado
            if numero_inicio > numero_ultimo_api:
                resultado['sucesso'] = True
                resultado['mensagem'] = 'Base de dados já está atualizada'
                resultado['ultimo_concurso'] = numero_ultimo_api
                return resultado
            
            # Atualiza concursos faltantes
            for numero in range(numero_inicio, numero_ultimo_api + 1):
                concurso = self.buscar_concurso_especifico(numero)
                
                if concurso:
                    if self.model.inserir(concurso):
                        resultado['total_inseridos'] += 1
                    else:
                        resultado['total_erros'] += 1
                        print(f"Erro ao inserir concurso {numero}")
                else:
                    resultado['total_erros'] += 1
                    print(f"Erro ao buscar concurso {numero}")
            
            resultado['sucesso'] = True
            resultado['ultimo_concurso'] = numero_ultimo_api
            resultado['mensagem'] = f"Base atualizada com sucesso! {resultado['total_inseridos']} novos concursos."
            
        except Exception as e:
            resultado['mensagem'] = f"Erro ao atualizar base: {str(e)}"
            print(f"Erro ao atualizar base completa: {e}")
        
        return resultado
    
    def sincronizar_ultimo_concurso(self) -> Dict[str, any]:
        """
        Sincroniza apenas o último concurso disponível
        
        Returns:
            Dict com resultado da sincronização
        """
        resultado = {
            'sucesso': False,
            'concurso': None,
            'mensagem': ''
        }
        
        try:
            ultimo = self.buscar_ultimo_concurso()
            
            if not ultimo:
                resultado['mensagem'] = 'Erro ao buscar último concurso da API'
                return resultado
            
            if self.model.inserir(ultimo):
                resultado['sucesso'] = True
                resultado['concurso'] = ultimo
                resultado['mensagem'] = f"Concurso {ultimo.get('numero')} sincronizado com sucesso"
            else:
                resultado['mensagem'] = 'Erro ao salvar concurso no banco'
                
        except Exception as e:
            resultado['mensagem'] = f"Erro ao sincronizar: {str(e)}"
            print(f"Erro ao sincronizar último concurso: {e}")
        
        return resultado
    
    def validar_dados_concurso(self, concurso: Dict) -> bool:
        """
        Valida se os dados do concurso estão completos
        
        Args:
            concurso: Dicionário com dados do concurso
            
        Returns:
            bool: True se dados são válidos
        """
        campos_obrigatorios = ['numero', 'dataApuracao', 'listaDezenas']
        
        for campo in campos_obrigatorios:
            if campo not in concurso or not concurso[campo]:
                return False
        
        # Valida lista de dezenas
        dezenas = concurso.get('listaDezenas', [])
        if len(dezenas) != 5:
            return False
        
        return True
