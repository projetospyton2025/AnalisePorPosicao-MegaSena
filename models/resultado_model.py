"""
Model para armazenar resultados da Quina
Inclui TODOS os campos da API oficial da Caixa
"""
import sqlite3
import json
from typing import List, Dict, Optional
from config import Config


class ResultadoModel:
    """Model para gerenciar resultados da Quina no banco de dados"""
    
    def __init__(self):
        self.db_path = Config.DATABASE_PATH
        self._create_table()
    
    def _get_connection(self):
        """Cria conexão com o banco de dados"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _create_table(self):
        """Cria tabela de resultados se não existir"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resultados (
                numero INTEGER PRIMARY KEY,
                data_apuracao TEXT NOT NULL,
                acumulado BOOLEAN NOT NULL,
                data_proximo_concurso TEXT,
                dezenas_sorteadas_ordem_sorteio TEXT NOT NULL,
                lista_dezenas TEXT NOT NULL,
                valor_arrecadado REAL,
                valor_acumulado_proximo_concurso REAL,
                valor_estimado_proximo_concurso REAL,
                valor_acumulado_concurso_especial REAL,
                valor_acumulado_concurso_05 REAL,
                local_sorteio TEXT,
                nome_municipio_uf_sorteio TEXT,
                lista_rateio_premio TEXT,
                lista_municipio_uf_ganhadores TEXT,
                observacao TEXT,
                ultimo_concurso BOOLEAN,
                numero_jogo INTEGER,
                numero_concurso_final_05 INTEGER
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def inserir(self, resultado: Dict) -> bool:
        """
        Insere ou atualiza um resultado no banco de dados
        
        Args:
            resultado: Dicionário com dados do resultado da API
            
        Returns:
            bool: True se inserido/atualizado com sucesso
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO resultados (
                    numero, data_apuracao, acumulado, data_proximo_concurso,
                    dezenas_sorteadas_ordem_sorteio, lista_dezenas,
                    valor_arrecadado, valor_acumulado_proximo_concurso,
                    valor_estimado_proximo_concurso, valor_acumulado_concurso_especial,
                    valor_acumulado_concurso_05, local_sorteio,
                    nome_municipio_uf_sorteio, lista_rateio_premio,
                    lista_municipio_uf_ganhadores, observacao,
                    ultimo_concurso, numero_jogo, numero_concurso_final_05
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                resultado.get('numero'),
                resultado.get('dataApuracao', resultado.get('data_apuracao', '')),
                resultado.get('acumulado', False),
                resultado.get('dataProximoConcurso', resultado.get('data_proximo_concurso')),
                json.dumps(resultado.get('dezenasSorteadasOrdemSorteio', resultado.get('dezenas_sorteadas_ordem_sorteio', []))),
                json.dumps(resultado.get('listaDezenas', resultado.get('lista_dezenas', []))),
                resultado.get('valorArrecadado', resultado.get('valor_arrecadado', 0.0)),
                resultado.get('valorAcumuladoProximoConcurso', resultado.get('valor_acumulado_proximo_concurso', 0.0)),
                resultado.get('valorEstimadoProximoConcurso', resultado.get('valor_estimado_proximo_concurso', 0.0)),
                resultado.get('valorAcumuladoConcursoEspecial', resultado.get('valor_acumulado_concurso_especial', 0.0)),
                resultado.get('valorAcumuladoConcurso_0_5', resultado.get('valor_acumulado_concurso_05', 0.0)),
                resultado.get('localSorteio', resultado.get('local_sorteio')),
                resultado.get('nomeMunicipioUFSorteio', resultado.get('nome_municipio_uf_sorteio')),
                json.dumps(resultado.get('listaRateioPremio', resultado.get('lista_rateio_premio', []))),
                json.dumps(resultado.get('listaMunicipioUFGanhadores', resultado.get('lista_municipio_uf_ganhadores', []))),
                resultado.get('observacao'),
                resultado.get('ultimoConcurso', resultado.get('ultimo_concurso', False)),
                resultado.get('numeroJogo', resultado.get('numero_jogo')),
                resultado.get('numeroConcursoFinal_0_5', resultado.get('numero_concurso_final_05'))
            ))
            
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao inserir resultado: {e}")
            return False
        finally:
            conn.close()
    
    def buscar_por_numero(self, numero: int) -> Optional[Dict]:
        """
        Busca resultado por número do concurso
        
        Args:
            numero: Número do concurso
            
        Returns:
            Dict com dados do resultado ou None
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM resultados WHERE numero = ?', (numero,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return self._row_to_dict(row)
        return None
    
    def buscar_ultimo(self) -> Optional[Dict]:
        """
        Busca o último resultado cadastrado
        
        Returns:
            Dict com dados do último resultado ou None
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM resultados ORDER BY numero DESC LIMIT 1')
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return self._row_to_dict(row)
        return None
    
    def buscar_todos(self, limite: Optional[int] = None) -> List[Dict]:
        """
        Busca todos os resultados
        
        Args:
            limite: Limite de resultados (opcional)
            
        Returns:
            Lista de dicionários com resultados
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        if limite:
            cursor.execute('SELECT * FROM resultados ORDER BY numero DESC LIMIT ?', (limite,))
        else:
            cursor.execute('SELECT * FROM resultados ORDER BY numero DESC')
        
        rows = cursor.fetchall()
        conn.close()
        
        return [self._row_to_dict(row) for row in rows]
    
    def contar_resultados(self) -> int:
        """
        Conta quantos resultados existem no banco
        
        Returns:
            int: Número de resultados
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) as total FROM resultados')
        row = cursor.fetchone()
        conn.close()
        
        return row['total'] if row else 0
    
    def _row_to_dict(self, row: sqlite3.Row) -> Dict:
        """
        Converte uma row do SQLite para dicionário
        
        Args:
            row: Row do SQLite
            
        Returns:
            Dict com dados do resultado
        """
        return {
            'numero': row['numero'],
            'dataApuracao': row['data_apuracao'],
            'acumulado': bool(row['acumulado']),
            'dataProximoConcurso': row['data_proximo_concurso'],
            'dezenasSorteadasOrdemSorteio': json.loads(row['dezenas_sorteadas_ordem_sorteio']),
            'listaDezenas': json.loads(row['lista_dezenas']),
            'valorArrecadado': row['valor_arrecadado'],
            'valorAcumuladoProximoConcurso': row['valor_acumulado_proximo_concurso'],
            'valorEstimadoProximoConcurso': row['valor_estimado_proximo_concurso'],
            'valorAcumuladoConcursoEspecial': row['valor_acumulado_concurso_especial'],
            'valorAcumuladoConcurso_0_5': row['valor_acumulado_concurso_05'],
            'localSorteio': row['local_sorteio'],
            'nomeMunicipioUFSorteio': row['nome_municipio_uf_sorteio'],
            'listaRateioPremio': json.loads(row['lista_rateio_premio']) if row['lista_rateio_premio'] else [],
            'listaMunicipioUFGanhadores': json.loads(row['lista_municipio_uf_ganhadores']) if row['lista_municipio_uf_ganhadores'] else [],
            'observacao': row['observacao'],
            'ultimoConcurso': bool(row['ultimo_concurso']),
            'numeroJogo': row['numero_jogo'],
            'numeroConcursoFinal_0_5': row['numero_concurso_final_05']
        }
