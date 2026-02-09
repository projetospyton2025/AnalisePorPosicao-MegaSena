# 📥 Guia Completo de Download - Sistema Mega-Sena

Este guia explica **passo a passo** como baixar todos os arquivos do projeto, independente do seu nível de experiência.

---

## 🎯 Qual método escolher?

| Método | Dificuldade | Quando usar |
|--------|-------------|-------------|
| **Download ZIP** | ⭐ Fácil | Primeira vez, sem Git instalado |
| **Git Clone** | ⭐⭐ Médio | Quer receber atualizações facilmente |
| **GitHub Desktop** | ⭐ Fácil | Prefere interface gráfica |

---

## 📦 MÉTODO 1: Download ZIP (Recomendado para iniciantes)

### Passo a passo com imagens:

1. **Acesse a página do projeto:**
   ```
   https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena
   ```

2. **Localize o botão verde "Code"** no canto superior direito

3. **Clique em "Code"** e depois em **"Download ZIP"**

4. **Salve o arquivo** em uma pasta de sua escolha (ex: `C:\Projetos\` ou `~/Projetos/`)

5. **Extraia o arquivo ZIP:**
   - **Windows:** Clique com botão direito → "Extrair tudo..."
   - **Mac:** Clique duplo no arquivo .zip
   - **Linux:** `unzip AnalisePorPosicao-MegaSena-main.zip`

6. **Pronto!** Você agora tem todos os arquivos na pasta `AnalisePorPosicao-MegaSena-main`

### 📁 Arquivos que você terá:

```
AnalisePorPosicao-MegaSena-main/
├── app.py                    ← Arquivo principal
├── config.py                 ← Configurações
├── requirements.txt          ← Lista de dependências
├── README.md                 ← Documentação
├── models/                   ← Modelos de dados
├── services/                 ← Serviços e lógica
├── routes/                   ← Rotas da API
├── templates/                ← Páginas HTML
└── static/                   ← CSS e JavaScript
    ├── css/
    └── js/
```

---

## 💻 MÉTODO 2: Usando Git (Para desenvolvedores)

### Pré-requisitos:
- Git instalado ([Baixar Git](https://git-scm.com/downloads))

### Comandos:

```bash
# 1. Navegue até a pasta onde quer salvar o projeto
cd C:\Projetos                    # Windows
cd ~/Projetos                     # Mac/Linux

# 2. Clone o repositório
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena.git

# 3. Entre na pasta do projeto
cd AnalisePorPosicao-MegaSena

# 4. Verifique os arquivos
dir        # Windows
ls -la     # Mac/Linux
```

### Vantagens do Git:
- ✅ Receba atualizações facilmente com `git pull`
- ✅ Veja o histórico de mudanças
- ✅ Contribua com o projeto

### Para atualizar depois:
```bash
cd AnalisePorPosicao-MegaSena
git pull origin main
```

---

## 🖱️ MÉTODO 3: GitHub Desktop (Interface Gráfica)

### Passo a passo:

1. **Instale o GitHub Desktop:**
   - Acesse: https://desktop.github.com/
   - Baixe e instale para seu sistema operacional

2. **Clone o repositório:**
   - Opção A: Na página do GitHub, clique em "Code" → "Open with GitHub Desktop"
   - Opção B: No GitHub Desktop, vá em "File" → "Clone repository"
     - Cole a URL: `https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena`
     - Escolha onde salvar

3. **Pronto!** Os arquivos serão baixados automaticamente

### Vantagens:
- ✅ Interface visual amigável
- ✅ Fácil de ver mudanças
- ✅ Sincronização automática

---

## 🔧 Próximos Passos: Instalação

Depois de baixar os arquivos, siga estas etapas:

### 1️⃣ Instale o Python
- Versão necessária: **Python 3.10 ou superior**
- Download: https://www.python.org/downloads/
- ⚠️ **Importante:** Marque "Add Python to PATH" durante a instalação

### 2️⃣ Crie um Ambiente Virtual

```bash
# Entre na pasta do projeto
cd AnalisePorPosicao-MegaSena

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o Sistema

```bash
python app.py
```

### 5️⃣ Acesse no Navegador

Abra seu navegador e acesse:
```
http://localhost:5056
```

---

## ❓ Problemas Comuns e Soluções

### 🔴 "Python não é reconhecido como comando"
**Solução:** Python não está no PATH do sistema
- Reinstale o Python marcando "Add Python to PATH"
- Ou adicione manualmente: Painel de Controle → Sistema → Variáveis de Ambiente

### 🔴 "pip não encontrado"
**Solução:**
```bash
python -m pip install --upgrade pip
```

### 🔴 "Erro ao instalar dependências"
**Solução:** Atualize o pip primeiro
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 🔴 "Porta 5056 já está em uso"
**Solução:** Altere a porta no arquivo `.env` ou `config.py`
```python
PORT=5057  # ou outra porta disponível
```

### 🔴 "ModuleNotFoundError"
**Solução:** Certifique-se de que o ambiente virtual está ativado
```bash
# Você deve ver (venv) no início da linha de comando
# Se não estiver, ative novamente:
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
```

---

## 📞 Precisa de Ajuda?

### Opções de suporte:

1. **Issues no GitHub:**
   - Abra uma [nova issue](https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena/issues)
   - Descreva o problema com detalhes

2. **Verifique a documentação:**
   - [README.md](README.md) - Documentação completa
   - [LICENSE](LICENSE) - Informações de licença

3. **Comunidade:**
   - Verifique issues fechadas para soluções anteriores
   - Contribua com suas próprias soluções

---

## 📚 Recursos Adicionais

### Para aprender mais:

- **Python:** https://docs.python.org/pt-br/3/tutorial/
- **Flask:** https://flask.palletsprojects.com/
- **Git:** https://git-scm.com/book/pt-br/v2
- **GitHub:** https://docs.github.com/pt

### Vídeos úteis:

- Como usar o Git e GitHub (busque no YouTube)
- Tutorial de Python para iniciantes
- Como criar ambientes virtuais em Python

---

## ✅ Checklist de Verificação

Antes de começar, certifique-se de ter:

- [ ] Python 3.10+ instalado
- [ ] Todos os arquivos baixados
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Servidor rodando (`python app.py`)
- [ ] Navegador acessando http://localhost:5056

---

## 🎉 Tudo Pronto!

Se você seguiu todos os passos, agora você tem:
- ✅ Código fonte completo baixado
- ✅ Ambiente configurado corretamente
- ✅ Sistema rodando localmente
- ✅ Acesso à interface web

**Aproveite o Sistema Mega-Sena!** 🎲

---

## 📝 Notas de Versão

**Versão:** 1.0.0  
**Última atualização:** Fevereiro 2025  
**Compatibilidade:** Python 3.10+, Windows/Mac/Linux

---

**Desenvolvido com ❤️ para análise de dados da Mega-Sena**
