
# Sistema Backend SAC IA 🤖💬

Este projeto consiste numa API backend desenvolvida em **FastAPI** para classificar automaticamente mensagens de Atendimento ao Cliente (SAC). Utiliza a inteligência artificial do **Google Gemini (modelo gemini-2.5-flash)** para analisar o teor das mensagens e categorizá-las por nível de urgência e tipo de solicitação.

## 🚀 Funcionalidades

* **Classificação Inteligente:** Analisa o texto e define a categoria automaticamente.
* **Categorias Suportadas:**
* Problema urgente
* Problema comum
* Pergunta nova/diferente
* Dúvida comum
* Elogio
* Reclamação leve


* **API Rápida:** Construída sobre FastAPI com validação de dados via Pydantic.

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

* [Python 3.9+](https://www.python.org/)
* Uma chave de API do Google AI Studio (Gemini API).

## 📦 Instalação e Configuração

Siga os passos abaixo para colocar o ambiente a funcionar:

### 1. Clonar o repositório

```bash
git clone https://github.com/pedroh-santana/sistema-backend-sac-ia.git
cd sistema-backend-sac-ia

```

### 2. Criar um ambiente virtual (Recomendado)

Para isolar as dependências do projeto:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

```

### 3. Instalar as dependências

Crie um ficheiro `requirements.txt` com o conteúdo abaixo ou instale manualmente:

```bash
pip install fastapi uvicorn python-dotenv google-genai pydantic

```

### 4. Configurar Variáveis de Ambiente

O sistema necessita de uma chave de API do Google para funcionar.

1. Crie um ficheiro chamado `.env` na raiz do projeto.
2. Adicione a sua chave de API (conforme esperado pela biblioteca `google-genai`):

```env
GOOGLE_API_KEY="A_SUA_CHAVE_API_AQUI"
# Ou se estiver a usar a variável padrão do sistema
GEMINI_API_KEY="A_SUA_CHAVE_API_AQUI"

```

> **Nota:** O código em `services.py` carrega estas variáveis via `load_dotenv`. Sem isso, o serviço retornará "Erro ao conectar ao serviço de IA".

## ▶️ Como Executar

Para iniciar o servidor de desenvolvimento, execute o seguinte comando no terminal:

```bash
uvicorn main:app --reload

```

O servidor iniciará, geralmente, em `http://127.0.0.1:8000`.

## 📖 Como Usar a API

### Documentação Interativa (Swagger UI)

A forma mais fácil de testar é através da documentação automática gerada pelo FastAPI.

1. Abra o navegador em: **`http://127.0.0.1:8000/docs`**
2. Vá até ao endpoint `POST /classificar`.
3. Clique em "Try it out" e envie uma mensagem.

### Exemplo de Requisição (JSON)

O endpoint espera um corpo JSON. Apenas o campo `texto` é obrigatório (o ID e o horário são gerados automaticamente se omitidos).

**Endpoint:** `POST /classificar`

**Corpo da Requisição:**

```json
{
  "texto": "O meu produto chegou completamente partido e preciso de uma troca urgente!"
}

```

**Resposta Esperada:**

```json
{
  "categoria": "Problema urgente"
}

```

## 📂 Estrutura do Projeto

* `main.py`: Ponto de entrada da aplicação. Define as rotas e inicializa o FastAPI.
* `services.py`: Contém a lógica de conexão com o Google Gemini e o prompt de classificação.
* `moldes.py`: Define os modelos de dados (Schemas) usando Pydantic para entrada e saída.
* `.env`: (Não incluído no repositório) Armazena as credenciais sensíveis.

## ⚠️ Tratamento de Erros

O sistema possui tratamentos básicos em `services.py`:

* Se a chave de API não for encontrada ou o cliente não iniciar, retorna: *"Erro ao conectar ao serviço de IA."*
* Se o modelo falhar ao gerar resposta, retorna: *"Erro ao processar a mensagem."*

