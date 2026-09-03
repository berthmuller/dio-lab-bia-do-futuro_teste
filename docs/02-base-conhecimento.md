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

HISTÓRICO DE ATENDIMENTO DOS CLIENTES:

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


PRODUTOS DISPONIVEÍS PARA ENSINO:

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
