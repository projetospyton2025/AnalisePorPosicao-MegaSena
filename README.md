# 🎲 Sistema Quina - Análise por Posição

Sistema completo em Python para geração e conferência de jogos da **Quina**, com análises estatísticas baseadas em dados reais da API oficial da Caixa Econômica Federal.

## 📥 COMO BAIXAR O PROJETO

### 💡 3 Formas de Baixar os Arquivos:

#### **Opção 1: Download ZIP (Mais Fácil)** ⭐
1. Clique no botão verde **"Code"** no topo desta página
2. Selecione **"Download ZIP"**
3. Extraia o arquivo ZIP em seu computador
4. Pronto! Todos os arquivos estão na pasta extraída

#### **Opção 2: Usando Git (Recomendado)**
```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena.git
cd AnalisePorPosicao-MegaSena
```

#### **Opção 3: GitHub Desktop**
1. Instale o [GitHub Desktop](https://desktop.github.com/)
2. Clique em **"Code"** → **"Open with GitHub Desktop"**
3. Escolha onde salvar o projeto

### 📂 O que você receberá:
- ✅ Código fonte completo (Python, HTML, CSS, JS)
- ✅ Banco de dados SQLite configurado
- ✅ Templates e estilos prontos
- ✅ Documentação completa
- ✅ Arquivo de dependências (requirements.txt)

### 📚 Precisa de ajuda para baixar?
- 📍 **[ONDE ESTÃO OS ARQUIVOS?](ONDE-ESTAO-ARQUIVOS.md)** - Guia visual de localização
- ⚡ **[GUIA DE INÍCIO RÁPIDO](QUICKSTART.md)** - Comece em 5 minutos!
- 📖 **[GUIA COMPLETO DE DOWNLOAD](DOWNLOAD.md)** - Passo a passo com imagens e soluções de problemas
- 🚀 **[Instruções de Instalação →](#-instalação-e-execução)**

---

## 🌟 Características

- ✅ Integração com API oficial da Caixa
- ✅ Geração inteligente de palpites com 8 estratégias diferentes
- ✅ Análises estatísticas completas (frequência, atrasos, pares/ímpares)
- ✅ Análise por faixa de posição (01-10, 11-20, etc.)
- ✅ Análise por primeiro dígito
- ✅ Análise por posição do sorteio (1ª a 5ª bola)
- ✅ Interface web responsiva com cores oficiais
- ✅ Conferência de jogos com resultados
- ✅ Arquitetura modular com Flask Blueprints
- ✅ Banco de dados SQLite com todos os campos da API

## 🔧 Tecnologias

- **Backend:** Python 3.10+, Flask 3.0
- **Banco de Dados:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **API:** Caixa Econômica Federal (oficial)

## 📊 Estrutura do Projeto

```
/
├── app.py                          # Aplicação principal Flask
├── config.py                       # Configurações
├── requirements.txt                # Dependências Python
├── .gitignore                      # Arquivos ignorados
├── .env.example                    # Exemplo de variáveis de ambiente
├── README.md                       # Documentação
├── database.db                     # Banco SQLite (criado automaticamente)
├── models/
│   └── resultado_model.py         # Model de resultados
├── services/
│   ├── api_caixa_service.py       # Integração com API
│   ├── estatistica_service.py     # Cálculos estatísticos
│   └── quina_service.py        # Geração de palpites
├── routes/
│   ├── main_routes.py             # Rotas HTML
│   └── api_routes.py              # Rotas API REST
├── templates/
│   ├── base.html                  # Template base
│   ├── index.html                 # Página de resultados
│   └── palpites.html              # Página de palpites
└── static/
    ├── css/
    │   └── styles.css             # Estilos CSS
    └── js/
        └── scripts.js             # Scripts JavaScript
```

## 🚀 Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena.git
cd AnalisePorPosicao-MegaSena
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente (opcional)

```bash
cp .env.example .env
# Edite o arquivo .env se necessário
```

### 5. Execute a aplicação

```bash
python app.py
```

A aplicação estará disponível em: **http://localhost:5056**

## 📖 Uso

### Interface Web

#### Página de Resultados (`/`)
- Visualize todos os resultados da Quina
- Atualize a base de dados com a API oficial
- Veja números sorteados em ordem crescente e ordem do sorteio
- Consulte ganhadores e valores de premiação

#### Página de Palpites (`/palpites`)
- Gere palpites inteligentes com diferentes estratégias
- Visualize estatísticas completas dos números
- Confira seus jogos com resultados anteriores
- Análise detalhada por faixas, dígitos e posições

### Estratégias de Palpites

1. **Equilibrada:** 60% números quentes + 40% frios
2. **Agressiva:** 80% números quentes + 20% frios
3. **Conservadora:** 40% números quentes + 60% frios
4. **Mista:** Distribuição uniforme por todas as faixas
5. **Atrasados:** Foca em números com maior atraso
6. **Por Faixa:** Garante números de todas as faixas (01-10, 11-20, etc.)
7. **Por Dígito:** Distribui por primeiro dígito
8. **Aleatória:** Seleção completamente aleatória

## 🔌 API Endpoints

### POST `/api/atualizar`
Atualiza a base de dados com todos os concursos da API da Caixa.

**Resposta:**
```json
{
  "sucesso": true,
  "mensagem": "Base atualizada com sucesso! 10 novos concursos.",
  "total_inseridos": 10,
  "total_erros": 0,
  "ultimo_concurso": 2897
}
```

### GET `/api/ultimo-resultado`
Retorna o último resultado cadastrado.

**Resposta:**
```json
{
  "sucesso": true,
  "resultado": {
    "numero": 2897,
    "dataApuracao": "05/08/2025",
    "listaDezenas": ["01", "06", "24", "27", "28", "57"],
    ...
  }
}
```

### GET `/api/resultados?limite=20`
Lista todos os resultados (opcional: limitar quantidade).

### GET `/api/resultado/<numero>`
Busca resultado de um concurso específico.

### GET `/api/estatisticas`
Retorna estatísticas completas:
- Frequência de números
- Números mais atrasados
- Distribuição pares/ímpares
- Análise por faixa de posição
- Análise por primeiro dígito
- Análise por posição do sorteio

### POST `/api/gerar-palpite`
Gera palpites baseados em estratégia.

**Corpo da requisição:**
```json
{
  "estrategia": "equilibrada",
  "quantidade_numeros": 6,
  "quantidade_jogos": 5
}
```

**Resposta:**
```json
{
  "sucesso": true,
  "estrategia": "equilibrada",
  "jogos": [
    [1, 6, 24, 27, 28, 57],
    [5, 12, 33, 41, 52, 60],
    ...
  ]
}
```

### POST `/api/conferir`
Confere um jogo com resultado de um concurso.

**Corpo da requisição:**
```json
{
  "numeros": [1, 6, 24, 27, 28, 57],
  "concurso": 2897
}
```

**Resposta:**
```json
{
  "sucesso": true,
  "concurso": 2897,
  "data": "05/08/2025",
  "numeros_jogo": [1, 6, 24, 27, 28, 57],
  "numeros_sorteados": [1, 6, 24, 27, 28, 57],
  "acertos": [1, 6, 24, 27, 28, 57],
  "quantidade_acertos": 6,
  "premiacao": "Quina (5 acertos)"
}
```

### GET `/api/status`
Retorna o status da aplicação e quantidade de concursos cadastrados.

## 📊 Análises Estatísticas

### 1. Frequência de Números
- Quantidade de vezes que cada número foi sorteado
- Percentual de aparição
- Top 20 mais frequentes (quentes)
- Top 20 menos frequentes (frios)

### 2. Análise de Atrasos
- Quantidade de concursos que cada número não aparece
- Números mais atrasados

### 3. Pares x Ímpares
- Distribuição de números pares e ímpares nos sorteios
- Padrões mais comuns (ex: 3P-3I, 4P-2I)

### 4. Análise por Faixa de Posição
```
Faixa 1: 01-10
Faixa 2: 11-20
Faixa 3: 21-30
Faixa 4: 31-40
Faixa 5: 41-50
Faixa 6: 51-60
```

### 5. Análise por Primeiro Dígito
```
Dígito 0: 01-09
Dígito 1: 10-19
Dígito 2: 20-29
Dígito 3: 30-39
Dígito 4: 40-49
Dígito 5: 50-59
Número 60
```

### 6. Análise por Posição do Sorteio
- Estatísticas de cada bola (1ª a 5ª)
- Quais números saem mais em cada posição
- Usa `dezenasSorteadasOrdemSorteio` da API

## 🎨 Identidade Visual

### Cor Principal
**#260184** - Verde oficial da Quina

### Paleta Completa
A aplicação utiliza uma escala completa de tons de verde, do mais claro ao mais escuro, seguindo a identidade visual oficial da Quina.

### Logo Oficial
![Quina](https://i.postimg.cc/VkSZr7z6/quina.png)

## 🎯 Regras da Quina

- **60 números disponíveis:** 01 a 60
- **5 números sorteados** por concurso
- Jogador escolhe de **5 a 15 números**
- Jogos mais comuns: 5, 6, 7, 8, 9 números

### Faixas de Premiação
1. **Quina (5 acertos)** - Prêmio principal
2. **Quina (5 acertos)** - Prêmio secundário
3. **Quadra (4 acertos)** - Prêmio terciário

## 💾 Banco de Dados

O sistema utiliza SQLite com uma tabela `resultados` que armazena **todos** os campos retornados pela API oficial da Caixa:

- Número do concurso (PK)
- Data da apuração
- Dezenas sorteadas (ordem do sorteio e ordem crescente)
- Valores arrecadados e prêmios
- Local do sorteio
- Lista de ganhadores por município
- Rateio de prêmios (Sena, Quina, Quadra)
- E muito mais...

## 🔐 Segurança

- Validação de entrada em todos os endpoints
- Tratamento de erros adequado
- Sem exposição de dados sensíveis
- Queries SQL parametrizadas (proteção contra SQL Injection)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

Para dúvidas ou sugestões:
- Abra uma [issue](https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena/issues)
- Entre em contato com os mantenedores

## 🎲 Aviso Legal

Este sistema é apenas para fins educacionais e de entretenimento. Os palpites gerados são baseados em análises estatísticas históricas, mas **não garantem** ganhos em apostas reais. A Quina é um jogo de azar e todos os resultados são completamente aleatórios.

**Jogue com responsabilidade!**

---

**Desenvolvido com ❤️ para análise de dados da Quina**
