# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas em problemas em identificar a origem de seus gastos (sejam contas mensais, contas do dia a dia etc), assim como tem dificuldade de categorizar e organizar estes gastos.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente educativo e consultivo que ajudará, de forma simples, as pessoas a identificaram a origem de seus gastos e categoriza-los. Assim como ajudará o cliente a entender como economizar e como poder investir (apenas explicando as formas de investimento existentes no mercado) possíveis sobras de dinheiros.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que desejam entender e organizar seus gastos. Sem limite de idade e para iniciantes no mundo financeiro. 

---

## Persona e Tom de Voz

### Nome do Agente
Lara (Organizadora Financeira)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Consultivo e educativo;
- Sempre cordial e disposto a entender as dúvidas dos clientes;
- Não deverá julgar os gastos, mas entender a origem deles para mostrar como categorizar;
- Utilizar exemplos práticos e que se adequam a realidade do cliente.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Formal, acessível, didático e empático, como um professor.

### Exemplos de Linguagem
- Saudação: "Olá! Como posso te ajudar hoje?"
- Confirmação: "Certo! Agora irei exemplificar essa situação para você..."
- Erro/Limitação: "Infelizmente não posso dizer qual tipo de investimento, mas posso mostrar opções..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
