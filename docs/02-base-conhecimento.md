# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Fontes da Lara |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Melhorar a interação da Lara com o cliente |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |
| `Credit_Card_Dataset.csv` | CSV | Análise de gastos de cartão de crédito|

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Inclusão de um dataset de gastos em cartão de crédito para aumentar a quantidade de dados referentes a gastos, visto que a agente Lara será, primariamente, uma agente de auxílio para organização financeira. Também foi adicionado ao arquivo de produtos financeiro o Fundo Imobiliário.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados poderão ser injetados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos no código.

```python

import pandas as pd
import json

#CSV
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')
cartaocredito = pd.read_csv('data/Credit_Card_Dataset.csv')

#JSONs
with open('data/perfil_investidor.json', 'r', enconding='utf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', enconding='utf-8') as f:
  produtos = json.load(f)

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
Os dados serão injetados diretamente no prompt para que o contexto seja o melhor possível. Em contextos maiores deveremos utilizar informações carregadas dinamicamente para gerar uma flexibilidade no prompt.

```text
DADOS E PERFIL DO CLIENTE (data/perfil_investidor.json):

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

HISTÓRICO DE ATENDIMENTO DOS CLIENTES (data/historico_atendimento.csv):

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida


PRODUTOS DISPONIVEÍS PARA ENSINO (data/produtos_financeiros.json):

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Dividend Yeld (DY) costuma ficar entre 6% e 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado para diversificação e rende recorrente mensal"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "médio",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  },
  {
    "nome": "Poupança",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "0,5% ao mês + TR",
    "aporte_minimo": 0.01,
    "indicado_para": "Quem busca liquidez imediata e facilidade de movimentação"
},
{
    "nome": "CRI / CRA (Certificados de Recebíveis)",
    "categoria": "renda_fixa_credito_privado",
    "risco": "médio",
    "rentabilidade": "Isenta de IR (Geralmente atrelada ao CDI ou IPCA + bônus)",
    "aporte_minimo": 1000.00,
    "indicado_para": "Investidores moderados que buscam isenção de imposto e aceitam menor liquidez"
},
{
    "nome": "Tesouro IPCA+",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "IPCA (Inflação) + Taxa Prefixada (ex: ~7% a 8% a.a.)",
    "aporte_minimo": 30.00,
    "indicado_para": "Quem busca proteger o poder de compra contra a inflação no longo prazo"
},
{
    "nome": "Debêntures Incentivadas",
    "categoria": "renda_fixa_credito_privado",
    "risco": "médio a alto",
    "rentabilidade": "Isenta de IR (Geralmente IPCA + taxa fixa robusta)",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem deseja financiar grandes obras de infraestrutura em troca de altos retornos isentos"
},
{
    "nome": "Letra de Câmbio (LC)",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "Geralmente entre 100% e 120% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança do FGC com retornos potencialmente maiores que os de grandes bancos"
}
]

TRANSAÇÕES VIA CARTÃO DE CRÉDITO (data/Credit_Card-Dataset.csv):
*Linhas Exemplo (não compreendem a totalidade do arquivo)*
Customer_ID,Age,Gender,Marital_Status,Education_Level,Employment_Status,Annual_Income,Credit_Score,Number_of_Credit_Lines,Credit_Utilization_Ratio,Debt_To_Income_Ratio,Number_of_Late_Payments,Tenure_in_Years,Total_Transactions_Last_Year,Total_Spend_Last_Year,Defaulted,CLV,Total_Transactions,Avg_Transaction_Amount,Max_Transaction_Amount,Min_Transaction_Amount,Fraud_Transactions,Unique_Merchant_Categories,Unique_Transaction_Cities
CUST_00001,59,Male,Married,PhD,Unemployed,41442,642,4,0.44,0.4,2,22,166,13997,0,57310,22,454.3372727272727,1379.89,11.83,0,10,13
CUST_00002,49,Male,Divorced,High School,Unemployed,85992,665,7,0.52,0.29,0,25,10,27768,0,124494,22,378.365,1939.47,7.0,1,8,13
CUST_00003,35,Male,Married,Bachelor,Employed,58420,683,8,0.88,0.2,2,9,177,17979,1,46180,10,437.929,1712.14,1.92,0,7,9


```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Reserva Atual: R$ 5000,00
- Objetivo: R$ 10000,00

Resumo de gastos:
- Moradia: R$ 1500,00
- Alimentação: R$ 1000,00
- Transporte: R$ 600,00
- Saúde: R$ 250,00
- Lazer: R$ 150,00
- Total de Saídas: R$ 3500,00

Produtos Disponíveis:
- Tesouro Selic;
- CDB Liquidez Diária;
- LCI/LCA;
- Fundo Multimercado;
- Fundo de Ações;
- Fundo Imobiliário (FII).
```
