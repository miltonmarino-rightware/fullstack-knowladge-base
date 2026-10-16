# DAD-001 — transações e limites das garantias

**Estado:** síntese documental; execução PostgreSQL pendente.
**Data:** 2026-10-16.
**Pré-requisitos:** tabelas, INSERT, SELECT e percurso de um pedido em [FND-001](../fundamentos/01-percurso-de-um-pedido.md).
**Pergunta:** o que uma transação protege e o que continua a exigir outros mecanismos?

## 1. Delimitar a unidade de trabalho

Uma transação agrupa alterações. BEGIN inicia um bloco explícito; COMMIT confirma; ROLLBACK cancela as alterações transacionais ainda não confirmadas. Fora de um bloco explícito, cada instrução pode constituir uma transação; bibliotecas clientes também podem gerir os limites automaticamente. Antes de interpretar um exemplo, verificar quem controla a transação. [dados-F001]

Num bloco em erro, continuar a enviar comandos não é uma estratégia de recuperação. O tutorial apresenta ROLLBACK e recuperação para savepoints; o comportamento observado também depende da configuração do cliente. [dados-F001; dados-F003]

## 2. Atomicidade e isolamento respondem a perguntas diferentes

Atomicidade trata a aplicação da unidade de alterações. Isolamento trata a interação entre transações concorrentes. No PostgreSQL, Read Committed é o nível por omissão: dois SELECT sucessivos na mesma transação podem observar alterações confirmadas entretanto por outra transação. Repeatable Read e Serializable oferecem comportamentos diferentes; Serializable pode exigir repetir uma transação após falha de serialização. Não escolher um nível apenas pelo nome. [dados-F002, §§13.2.1–13.2.3]

## 3. Um limite que não devemos esconder

Valores obtidos através de nextval não são recuperados para reutilização quando a transação aborta. Sequências podem, portanto, ter lacunas; o mesmo pode ocorrer em outras circunstâncias. Um identificador gerado por sequência não deve ser confundido com um contador sem intervalos. [dados-F004]

Inferência para modelação: se um requisito exigir numeração sem lacunas, precisamos de estudar esse requisito e um mecanismo específico. Não o prometer apenas por usar uma coluna com sequência.

## 4. Fora da transação

Hipótese de engenharia para verificar no L03: um ficheiro escrito pelo cliente enquanto a transação está aberta não é revertido pelo ROLLBACK da base. Estar próximo no tempo ou no código não coloca dois efeitos dentro da mesma garantia.

Também não devemos inferir conclusão de email, webhook ou serviço externo a partir do commit local. Essas integrações requerem investigação própria; outbox e compensações continuam pendentes.

## 5. Perguntas de decisão para uma operação

| Questão | O que precisamos de explicitar |
| --- | --- |
| Que alterações devem acontecer juntas? | Fronteira da transação |
| Que regra deve permanecer verdadeira? | Invariante e forma de a verificar |
| Há operações concorrentes? | Anomalias admissíveis e isolamento |
| Há efeitos externos? | Como detetar divergências e recuperar |
| O cliente perdeu a resposta? | Como consultar o resultado e avaliar repetição |
| O número gerado pode ter lacunas? | Significado do identificador |
| Há falha de energia? | Configuração e teste específico de durabilidade |

Estas são perguntas de investigação da RIGHTWARE, não decisões fechadas para todos os sistemas.

## 6. Como verificar

O [L03](../fundamentos/laboratorios/l03-postgresql/README.md) propõe quatro cenários: erro e rollback, commit, ficheiro externo e sequência. O roteiro ainda não foi executado.

O [L02](../fundamentos/laboratorios/l02-timeout/README.md) já demonstrou timeout após gravação em SQLite. Essa evidência não valida o comportamento PostgreSQL.

## 7. Critério de aprendizagem

Explicar a fronteira transacional de um exemplo, prever cada resultado, executá-lo, comparar evidências e declarar o que permanece desconhecido. Antes de um padrão de produção, ainda estudar restrições, locks, deadlocks, serialização, retries, durabilidade e recuperação.

## Fontes

IDs, versões e secções em [fontes.md](fontes.md). As fontes fundamentam a síntese; não substituem evidência experimental.
