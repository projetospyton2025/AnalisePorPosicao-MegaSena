# 🎲 Adaptação Mega-Sena → Quina - Resumo Completo

## 📋 Visão Geral

Adaptação bem-sucedida do sistema de análise de loteria **Mega-Sena** para **Quina**, mantendo todas as funcionalidades e atualizando para as regras específicas da Quina.

## 🔄 Mudanças Principais

### Regras do Jogo
| Aspecto | Mega-Sena | Quina |
|---------|-----------|-------|
| **Números disponíveis** | 01-60 (60 números) | 01-80 (80 números) |
| **Números sorteados** | 6 números | 5 números |
| **Tamanho do jogo** | 6-20 números | 5-15 números |
| **Posições analisadas** | 1ª a 6ª bola | 1ª a 5ª bola |

### Faixas de Premiação
| Mega-Sena | Quina |
|-----------|-------|
| Sena (6 acertos) | Quina (5 acertos) |
| Quina (5 acertos) | Quadra (4 acertos) |
| Quadra (4 acertos) | Terno (3 acertos) |
| - | Duque (2 acertos) |

### Análises Estatísticas

#### Distribuição por Faixa
**Mega-Sena (6 faixas de 10 números):**
- Faixa 1: 01-10
- Faixa 2: 11-20
- Faixa 3: 21-30
- Faixa 4: 31-40
- Faixa 5: 41-50
- Faixa 6: 51-60

**Quina (5 faixas de 16 números):**
- Faixa 1: 01-16
- Faixa 2: 17-32
- Faixa 3: 33-48
- Faixa 4: 49-64
- Faixa 5: 65-80

#### Distribuição por Primeiro Dígito
**Mega-Sena (7 grupos):**
- 01-09, 10-19, 20-29, 30-39, 40-49, 50-59, 60

**Quina (8 grupos):**
- 01-09, 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-80

### Identidade Visual

#### Cores
| Mega-Sena | Quina |
|-----------|-------|
| **Verde #1B9A67** | **Roxo #260184** |
| Gradiente verde | Gradiente roxo |

#### Logo
| Mega-Sena | Quina |
|-----------|-------|
| ![Mega-Sena](https://i.postimg.cc/VkSZr7z6/megasena.png) | ![Quina](https://i.postimg.cc/G3PvK6cN/quina.png) |

## 📁 Arquivos Modificados

### Backend (Python)
- ✅ `config.py` - Parâmetros e API URL
- ✅ `app.py` - Mensagens e títulos
- ✅ `models/resultado_model.py` - Validação de 5 números
- ✅ `services/api_caixa_service.py` - API Quina
- ✅ `services/estatistica_service.py` - Estatísticas 1-80, 5 posições
- ✅ `services/quina_service.py` - Nova lógica (era megasena_service.py)
- ✅ `routes/api_routes.py` - Importação QuinaService

### Frontend (HTML/CSS/JS)
- ✅ `templates/base.html` - Logo e título
- ✅ `templates/index.html` - Referências Quina
- ✅ `templates/palpites.html` - Inputs 5-15
- ✅ `static/css/styles.css` - Esquema de cores roxo
- ✅ `static/js/scripts.js` - Validação 1-80, 5-15

### Documentação
- ✅ `README.md` - Documentação completa Quina

## 🧪 Testes Realizados

### ✅ Funcionalidades Testadas
1. **Configuração**
   - Range de números: 1-80 ✓
   - Números sorteados: 5 ✓
   - Tamanho do jogo: 5-15 ✓

2. **Estatísticas**
   - Total de concursos: 50 ✓
   - Faixas: 5 grupos ✓
   - Posições: 5 bolas ✓
   - Números mais frequentes ✓
   - Números mais atrasados ✓
   - Pares x Ímpares ✓

3. **Geração de Palpites**
   - 8 estratégias funcionando ✓
   - Números no range 1-80 ✓
   - Tamanho correto (5 números) ✓

4. **Conferência de Jogos**
   - 5 acertos = Quina ✓
   - 4 acertos = Quadra ✓
   - 3 acertos = Terno ✓
   - 2 acertos = Duque ✓

5. **Interface Web**
   - Cores roxas aplicadas ✓
   - Logo Quina exibido ✓
   - Validação de inputs ✓
   - Estatísticas renderizadas ✓

## 🔌 API

**Endpoint:** `https://servicebus2.caixa.gov.br/portaldeloterias/api/quina`

**Estrutura de Resposta:**
```json
{
  "numero": 6792,
  "dataApuracao": "05/08/2025",
  "listaDezenas": ["16", "42", "43", "62", "68"],
  "dezenasSorteadasOrdemSorteio": ["16", "62", "68", "43", "42"],
  "listaRateioPremio": [
    {
      "descricaoFaixa": "5 acertos",
      "numeroDeGanhadores": 0,
      "valorPremio": 0.0
    },
    {
      "descricaoFaixa": "4 acertos",
      "numeroDeGanhadores": 22,
      "valorPremio": 14600.08
    },
    {
      "descricaoFaixa": "3 acertos",
      "numeroDeGanhadores": 2035,
      "valorPremio": 150.32
    },
    {
      "descricaoFaixa": "2 acertos",
      "numeroDeGanhadores": 54300,
      "valorPremio": 5.63
    }
  ]
}
```

## 🚀 Como Executar

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py

# Acessar
http://localhost:5056
```

## 📊 Estratégias de Palpites

1. **Equilibrada** - 60% números quentes + 40% frios
2. **Agressiva** - 80% números quentes + 20% frios
3. **Conservadora** - 40% números quentes + 60% frios
4. **Mista** - Distribuição uniforme por faixas
5. **Atrasados** - Foca em números com maior atraso
6. **Por Faixa** - Garante números de todas as faixas
7. **Por Dígito** - Distribui por primeiro dígito
8. **Aleatória** - Seleção completamente aleatória

## ✨ Resultado Final

✅ **Aplicação 100% funcional** para análise da Quina  
✅ **Todas as funcionalidades** adaptadas corretamente  
✅ **Interface visual** atualizada com identidade Quina  
✅ **Documentação** completa e atualizada  
✅ **Testes** confirmam funcionamento correto  

---

**Desenvolvido com ❤️ para análise de dados da Quina**
