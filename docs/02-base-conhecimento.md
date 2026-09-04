# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Fontes da Lara |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Melhorar a interação da Lara com o cliente |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |
| `transacoes_cartao.csv` | CSV | Análise de gastos de cartão de crédito|
| `base_conhecimento_investimentos.json`|JSON| Tipos de investimentos e explicações|

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

INVESTIMENTOS EXPLICADOS (data/base_conhecimento_investimento.json)

[
    {
        "id": "doc_01",
        "categoria": "Títulos Públicos",
        "subcategoria": "Empréstimo ao Governo",
        "ativo": "Tesouro Selic",
        "descricao": "Título público federal atrelado à taxa básica de juros (Selic), ideal para reservas de emergência devido ao baixo risco e liquidez diária.",
        "fonte_nome": "Tesouro Nacional / B3",
        "fonte_url": "https://www.tesourodireto.com.br/titulos/tipos-de-tesouro.htm"
    },
    {
        "id": "doc_02",
        "categoria": "Títulos Públicos",
        "subcategoria": "Empréstimo ao Governo",
        "ativo": "Tesouro IPCA+",
        "descricao": "Título público focado no longo prazo que garante rentabilidade real, pois rende uma taxa fixa mais a variação oficial da inflação.",
        "fonte_nome": "Tesouro Nacional / B3",
        "fonte_url": "https://www.tesourodireto.com.br/titulos/tipos-de-tesouro.htm"
    },
    {
        "id": "doc_03",
        "categoria": "Títulos Bancários",
        "subcategoria": "Empréstimo a Bancos",
        "ativo": "CDB Liquidez Diária",
        "descricao": "Certificado de Depósito Bancário emitido por instituições financeiras com o compromisso de recompra diária dos juros acumulados, protegida pelo FGC.",
        "fonte_nome": "C6 Bank",
        "fonte_url": "https://ajuda.c6bank.com.br/s/article/O-que-é-CDB"
    },
    {
        "id": "doc_04",
        "categoria": "Títulos Bancários",
        "subcategoria": "Empréstimo a Bancos",
        "ativo": "LCI/LCA",
        "descricao": "Letras de Crédito emitidas por bancos para financiar exclusivamente os setores imobiliário (LCI) e do agronegócio (LCA), com atrativo de isenção de Imposto de Renda.",
        "fonte_nome": "Banco Santander",
        "fonte_url": "https://www.santander.com.br/blog/o-que-sao-lci-lca"
    },
    {
        "id": "doc_05",
        "categoria": "Títulos Bancários",
        "subcategoria": "Empréstimo a Bancos",
        "ativo": "Letra de Câmbio (LC)",
        "descricao": "Título de renda fixa emitido por sociedades de crédito e financiamento (financeiras) para captar recursos, contando também com a garantia do FGC.",
        "fonte_nome": "Portal do Investidor (CVM)",
        "fonte_url": "https://www.investidor.gov.br/menu/Menu_Investidor/valores_mobiliarios/letra_cambio.html"
    },
    {
        "id": "doc_06",
        "categoria": "Títulos Bancários",
        "subcategoria": "Empréstimo a Bancos",
        "ativo": "Poupança",
        "descricao": "Aplicação financeira mais tradicional do país, com rendimento fixado mensalmente por lei (0,5% + TR) e isenta de taxas ou impostos.",
        "fonte_nome": "Banco Central do Brasil / Santander",
        "fonte_url": "https://www.bcb.gov.br/meubc/faqs/c/poupanca"
    },
    {
        "id": "doc_07",
        "categoria": "Crédito Privado",
        "subcategoria": "Empréstimo a Empresas",
        "ativo": "CRI / CRA",
        "descricao": "Certificados de Recebíveis lastreados em dívidas dos setores imobiliário (CRI) ou do agronegócio (CRA), emitidos por securitizadoras e isentos de IR.",
        "fonte_nome": "Mercado Bitcoin",
        "fonte_url": "https://www.mercadobitcoin.com.br/blog/educacao/tipos-de-investimentos/"
    },
    {
        "id": "doc_08",
        "categoria": "Crédito Privado",
        "subcategoria": "Empréstimo a Empresas",
        "ativo": "Debêntures Incentivadas",
        "descricao": "Títulos de dívida de empresas privadas emitidos especificamente para financiar projetos de infraestrutura do país, contando com isenção fiscal para a pessoa física.",
        "fonte_nome": "B3 - Bora Investir",
        "fonte_url": "https://borainvestir.b3.com.br/tipos-de-investimentos/debentures-o-que-sao-e-como-investir-bora-investir/"
    },
    {
        "id": "doc_09",
        "categoria": "Fundos de Investimento",
        "subcategoria": "Carteiras Coletivas",
        "ativo": "Fundo Multimercado",
        "descricao": "Carteira gerida por profissionais que mescla ativos de vários mercados (juros, câmbio, ações), buscando retornos acima da média por meio de estratégias flexíveis.",
        "fonte_nome": "ANBIMA / Fundação ELOS",
        "fonte_url": "https://www.anbima.com.br/pt_br/educar/certificacoes/cpa-20/material-de-estudos/fundos-multimercado.htm"
    },
    {
        "id": "doc_10",
        "categoria": "Fundos de Investimento",
        "subcategoria": "Carteiras Coletivas",
        "ativo": "Fundo de Ações",
        "descricao": "Condomínio de investimento que aplica a maior parte de seu patrimônio na compra de papéis e participações de empresas listadas na Bolsa de Valores.",
        "fonte_nome": "Efí Bank",
        "fonte_url": "https://sejaefi.com.br/blog/qual-melhor-investimento-hoje-para-iniciantes"
    },
    {
        "id": "doc_11",
        "categoria": "Fundos de Investimento",
        "subcategoria": "Carteiras Coletivas",
        "ativo": "Fundo Imobiliário (FII)",
        "descricao": "Comunidade de investidores que junta recursos para aplicar no desenvolvimento ou locação de grandes imóveis comerciais, distribuindo rendimentos mensais isentos.",
        "fonte_nome": "Portal Mais Retorno",
        "fonte_url": "https://maisretorno.com/portal/o-que-sao-fundos-imobiliarios-fii"
    }
]

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
