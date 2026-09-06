# Passo a passo da execulção

## Setup do Ollama

```bash

#1. Instalar Ollama (ollama.com)
#2. Baixar o modelo
ollama pull gpt-oss

#3. Testar o funcionamento
ollama run gpt-oss "Olá mundo!"

```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
