# ⚡ Guia de Início Rápido - Sistema Mega-Sena

Comece a usar o sistema em **5 minutos**!

---

## 🎯 Início Rápido

### Para quem tem pressa:

```bash
# 1. Baixe o projeto
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena.git
cd AnalisePorPosicao-MegaSena

# 2. Configure o ambiente
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OU
venv\Scripts\activate     # Windows

# 3. Instale e rode
pip install -r requirements.txt
python app.py

# 4. Acesse: http://localhost:5056
```

---

## 📋 Pré-requisitos Mínimos

- ✅ Python 3.10 ou superior
- ✅ Conexão com internet (para baixar dependências)
- ✅ 50 MB de espaço em disco
- ✅ Navegador web moderno

---

## 🚀 Primeiros Passos

### 1. Baixar o Projeto

**Sem Git?** [Baixe o ZIP aqui](https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena/archive/refs/heads/main.zip)

**Com Git:**
```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena.git
```

### 2. Instalar Dependências

```bash
cd AnalisePorPosicao-MegaSena
pip install -r requirements.txt
```

**Dependências instaladas:**
- Flask 3.0.0 (Framework web)
- requests 2.31.0 (Requisições HTTP)
- python-dotenv 1.0.0 (Variáveis de ambiente)

### 3. Executar o Sistema

```bash
python app.py
```

Você verá:
```
═══════════════════════════════════════════════════
🎲 Sistema Mega-Sena - Análise por Posição
═══════════════════════════════════════════════════

✓ Servidor rodando em: http://0.0.0.0:5056
✓ Modo Debug: True
✓ Banco de dados: /caminho/database.db

Acesse: http://localhost:5056
═══════════════════════════════════════════════════
```

### 4. Usar o Sistema

1. Abra o navegador em **http://localhost:5056**
2. Clique em **"Atualizar Base de Dados"** (primeira vez)
3. Explore os resultados da Mega-Sena
4. Acesse **"Palpites"** para gerar jogos inteligentes

---

## 🎮 Funcionalidades Principais

### Página de Resultados (`/`)
- 📊 Visualize todos os resultados oficiais
- 🔄 Atualize a base de dados da API da Caixa
- 💰 Veja prêmios e ganhadores por município

### Página de Palpites (`/palpites`)
- 🎲 Gere palpites com 8 estratégias diferentes
- 📈 Visualize estatísticas completas
- ✅ Confira seus jogos com resultados anteriores

---

## 💡 Dicas Úteis

### Primeira execução:
1. Clique em "Atualizar Base de Dados"
2. Aguarde o download dos concursos (pode demorar alguns minutos)
3. Explore as estatísticas e gere seus palpites

### Atualizações:
- Execute `git pull` regularmente para receber atualizações
- Ou baixe o ZIP novamente da página do GitHub

### Mudando a porta:
Se a porta 5056 estiver ocupada:
```bash
# Edite config.py e altere:
PORT = 5057  # ou outra porta
```

---

## ❌ Resolução Rápida de Problemas

| Problema | Solução Rápida |
|----------|----------------|
| Python não encontrado | Instale de [python.org](https://python.org) |
| pip não funciona | Execute `python -m pip` ao invés de `pip` |
| Porta ocupada | Mude a porta em `config.py` |
| Erro ao importar Flask | Execute `pip install -r requirements.txt` |
| Página não carrega | Verifique se o servidor está rodando |

---

## 📚 Documentação Completa

- 📖 [README.md](README.md) - Documentação detalhada
- 📥 [DOWNLOAD.md](DOWNLOAD.md) - Guia completo de download
- 🔧 [Estrutura do Projeto](README.md#-estrutura-do-projeto)
- 🔌 [Endpoints da API](README.md#-api-endpoints)

---

## 🎯 Próximos Passos

Depois de rodar o sistema:

1. **Explore as estatísticas:**
   - Números mais frequentes
   - Números atrasados
   - Distribuição por faixas

2. **Gere palpites:**
   - Teste diferentes estratégias
   - Escolha de 6 a 20 números
   - Gere múltiplos jogos

3. **Confira resultados:**
   - Compare seus números
   - Veja quantos acertos teve
   - Identifique premiações

---

## 💬 Comandos Úteis

```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Desativar ambiente virtual
deactivate

# Atualizar dependências
pip install --upgrade -r requirements.txt

# Verificar versão do Python
python --version

# Listar pacotes instalados
pip list

# Rodar em modo produção (sem debug)
# Edite config.py: DEBUG = False
python app.py
```

---

## 🆘 Precisa de Mais Ajuda?

1. **Leia o [DOWNLOAD.md](DOWNLOAD.md)** - Guia detalhado com soluções
2. **Abra uma [Issue](https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena/issues)**
3. **Verifique issues resolvidas** anteriormente

---

## ✅ Tudo Funcionando?

Se você conseguiu:
- ✅ Baixar os arquivos
- ✅ Instalar as dependências
- ✅ Rodar o servidor
- ✅ Acessar pelo navegador

**Parabéns! Você está pronto para usar o Sistema Mega-Sena!** 🎉

---

**Boa sorte com seus palpites!** 🍀🎲
