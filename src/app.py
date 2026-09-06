import json
import pandas as pd
import requests
import streamlit as st

#======== Configuração Ollama ========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

#======== Carregar Dados ========
historico = pd.read_csv('./LaraIA/data/historico_atendimento.csv')
transacoes = pd.read_csv('./LaraIA/data/transacoes.csv')
cartao = pd.read_csv('./LaraIA/data/transacoes_cartao.csv')
perfil = json.load(open('./LaraIA/data/perfil_investidor.json'))
base_perfil = json.load(open('./LaraIA/data/base_conhecimento_investimentos.json'))
produtos = json.load(open('./LaraIA/data/produtos_financeiros.json'))

#======== Montar Contexto ========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil de investimento {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

TRANSAÇÕES CARTAO:
{cartao.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

BASE PERFIL:
{json.dumps(base_perfil, indent=2, ensure_ascii=False)}
"""

#======== Montar Contexto ========
SYSTEM_PROMPT = """
Você é a Lara, uma agente financeira que auxília as pessoas a organizarem seus gastos, utilizando exemplos do dia a dia e que são compatíveis com a realidade do cliente.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos.
2. Nunca inventar informações financeiras.
3. Se não souber algo, admita e ofereça alternativas.
4. JAMAIS induza o cliente a contratação de um investimento específico, apenas explique.
5. Ser simples e prática, mas mantendo um tom técnico nas explicações.
6. Sempre perguntar para o cliente se ele entendeu a explicação.
7. Respostas sucintas e coesas. No máximo 3 parágrafos.
8. Nunca fugir do tema organização financeira e finanças pessoais
"""

#======== Chamando Ollama ========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json = {"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

#======== INTERFACE STREAMLIT ========

st.title("Lara, sua organizadora financeira")

if pergunta := st.chat_input("Como posso te ajudar a organizar suas finanças?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistent").write(perguntar(pergunta))
