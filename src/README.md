# Passo a passo da execulção

## Setup do Ollama

```bash

#1. Instalar Ollama (ollama.com)
#2. Baixar o modelo
ollama pull gpt-oss

#3. Testar o funcionamento
ollama run gpt-oss "Olá mundo!"

```

## Código Completo

Todo o código fonte está no arquivo `app.py`

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

#2. Verificar se o Ollama está rodando
ollama serve

#3. Rodar o app
streamlit run app.py
```
