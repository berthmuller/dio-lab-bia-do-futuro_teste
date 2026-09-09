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

Os dados poderão ser injetados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos no código. Conforme o arquivo `app.py`.


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

TRANSAÇÕES VIA CARTÃO DE CRÉDITO (data/transacoes_cartao.csv):
cliente_id,cliente_nome,data,descricao,categoria,valor,parcelas,cartao_bandeira
CLI001,João Silva,2025-10-02,Supermercado Extra,alimentacao,320.50,1,Mastercard
CLI001,João Silva,2025-10-04,Posto Ipiranga,transporte,180.00,1,Mastercard
CLI001,João Silva,2025-10-06,Farmácia Droga Raia,saude,65.90,1,Mastercard
CLI001,João Silva,2025-10-09,Amazon - Fone de Ouvido,compras,199.00,3,Mastercard
CLI001,João Silva,2025-10-14,Restaurante Sushi,alimentacao,145.00,1,Mastercard
CLI001,João Silva,2025-10-18,Loja de Roupas Renner,vestuario,289.90,2,Mastercard
CLI001,João Silva,2025-10-22,Cinema Cinemark,lazer,68.00,1,Mastercard
CLI001,João Silva,2025-10-28,Uber,transporte,52.30,1,Mastercard
CLI002,Maria Oliveira,2025-10-01,Supermercado Pão de Açúcar,alimentacao,410.20,1,Visa
CLI002,Maria Oliveira,2025-10-05,Academia Smart Fit,saude,109.90,1,Visa
CLI002,Maria Oliveira,2025-10-08,Magazine Luiza - Liquidificador,compras,159.00,1,Visa
CLI002,Maria Oliveira,2025-10-11,Netflix,lazer,55.90,1,Visa
CLI002,Maria Oliveira,2025-10-15,Posto Shell,transporte,220.00,1,Visa
CLI002,Maria Oliveira,2025-10-19,Restaurante Italiano,alimentacao,175.50,1,Visa
CLI002,Maria Oliveira,2025-10-23,Farmácia Pacheco,saude,42.00,1,Visa
CLI002,Maria Oliveira,2025-10-27,Loja Centauro - Tênis,vestuario,399.00,4,Visa
CLI003,Carlos Mendes,2025-10-03,Restaurante Outback,alimentacao,210.00,1,Elo
CLI003,Carlos Mendes,2025-10-06,Posto BR,transporte,190.00,1,Elo
CLI003,Carlos Mendes,2025-10-10,Farmácia São Paulo,saude,78.50,1,Elo
CLI003,Carlos Mendes,2025-10-13,Loja C&A,vestuario,159.90,2,Elo
CLI003,Carlos Mendes,2025-10-17,Spotify,lazer,21.90,1,Elo
CLI003,Carlos Mendes,2025-10-21,Supermercado Carrefour,alimentacao,380.00,1,Elo
CLI003,Carlos Mendes,2025-10-25,iFood,alimentacao,95.40,1,Elo
CLI003,Carlos Mendes,2025-10-29,Uber,transporte,38.00,1,Elo
CLI004,Ana Beatriz,2025-10-02,Supermercado Assaí,alimentacao,295.00,1,Mastercard
CLI004,Ana Beatriz,2025-10-07,Salão de Beleza,servicos,150.00,1,Mastercard
CLI004,Ana Beatriz,2025-10-09,Livraria Saraiva,educacao,89.90,1,Mastercard
CLI004,Ana Beatriz,2025-10-12,Posto Ale,transporte,160.00,1,Mastercard
CLI004,Ana Beatriz,2025-10-16,Restaurante Japonês,alimentacao,132.00,1,Mastercard
CLI004,Ana Beatriz,2025-10-20,Cinema Cinemark,lazer,58.00,1,Mastercard
CLI004,Ana Beatriz,2025-10-24,Farmácia Drogasil,saude,54.30,1,Mastercard
CLI004,Ana Beatriz,2025-10-30,Loja Zara,vestuario,349.00,3,Mastercard
CLI005,Pedro Almeida,2025-10-01,Supermercado Dia,alimentacao,265.40,1,Visa
CLI005,Pedro Almeida,2025-10-05,Posto Petrobras,transporte,210.00,1,Visa
CLI005,Pedro Almeida,2025-10-08,Farmácia Pague Menos,saude,48.70,1,Visa
CLI005,Pedro Almeida,2025-10-11,Livraria Cultura,educacao,112.00,1,Visa
CLI005,Pedro Almeida,2025-10-15,Restaurante Chinês,alimentacao,98.50,1,Visa
CLI005,Pedro Almeida,2025-10-19,Loja Decathlon,vestuario,229.90,2,Visa
CLI005,Pedro Almeida,2025-10-23,Disney+,lazer,33.90,1,Visa
CLI005,Pedro Almeida,2025-10-27,iFood,alimentacao,72.00,1,Visa
CLI006,Fernanda Costa,2025-10-02,Supermercado Big,alimentacao,340.00,1,Elo
CLI006,Fernanda Costa,2025-10-06,Clínica Odontológica,saude,320.00,3,Elo
CLI006,Fernanda Costa,2025-10-09,Posto Ipiranga,transporte,175.00,1,Elo
CLI006,Fernanda Costa,2025-10-13,Loja Riachuelo,vestuario,189.90,1,Elo
CLI006,Fernanda Costa,2025-10-16,Cinema Kinoplex,lazer,45.00,1,Elo
CLI006,Fernanda Costa,2025-10-20,Restaurante Português,alimentacao,168.00,1,Elo
CLI006,Fernanda Costa,2025-10-24,Farmácia Nissei,saude,39.80,1,Elo
CLI006,Fernanda Costa,2025-10-29,Uber,transporte,44.60,1,Elo
CLI007,Rafael Souza,2025-10-03,Supermercado Mundial,alimentacao,298.70,1,Mastercard
CLI007,Rafael Souza,2025-10-07,Academia Bio Ritmo,saude,129.90,1,Mastercard
CLI007,Rafael Souza,2025-10-10,Posto Ale,transporte,205.00,1,Mastercard
CLI007,Rafael Souza,2025-10-14,Loja Fast Shop - Fone,compras,349.00,4,Mastercard
CLI007,Rafael Souza,2025-10-17,iFood,alimentacao,85.30,1,Mastercard
CLI007,Rafael Souza,2025-10-21,Cinema Cinemark,lazer,64.00,1,Mastercard
CLI007,Rafael Souza,2025-10-25,Farmácia Drogasil,saude,58.20,1,Mastercard
CLI007,Rafael Souza,2025-10-30,Restaurante Árabe,alimentacao,140.00,1,Mastercard
CLI008,Juliana Ramos,2025-10-01,Supermercado Zaffari,alimentacao,355.00,1,Visa
CLI008,Juliana Ramos,2025-10-04,Posto Shell,transporte,198.00,1,Visa
CLI008,Juliana Ramos,2025-10-08,Farmácia Panvel,saude,61.40,1,Visa
CLI008,Juliana Ramos,2025-10-12,Loja Renner,vestuario,269.90,2,Visa
CLI008,Juliana Ramos,2025-10-16,Restaurante Vegano,alimentacao,110.00,1,Visa
CLI008,Juliana Ramos,2025-10-20,Spotify,lazer,21.90,1,Visa
CLI008,Juliana Ramos,2025-10-24,Curso Online Udemy,educacao,49.90,1,Visa
CLI008,Juliana Ramos,2025-10-28,Uber,transporte,41.20,1,Visa


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
