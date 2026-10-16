# Dados — percurso de formação

**Data:** 2026-10-16. **Estado:** seleção curricular; aulas não concluídas.
Origem: [revisão da Parte I](../REVISAO-FORMACAO-PARTE-I.md).

## R09 — CMU 15-445/645, Fall 2024

[Calendário oficial](https://15445.courses.cs.cmu.edu/fall2024/schedule.html), edição arquivada, com notas, slides e vídeos. Acesso público aos materiais não garante avaliação externa, acompanhamento ou bibliografia integral gratuita.

| Bloco | Aulas selecionadas | Pergunta orientadora |
| --- | --- | --- |
| Modelo e consultas | 01 — Relational Model & Algebra; 02 — Modern SQL | Como separar modelo lógico e representação? |
| Armazenamento e acesso | 03–04 — Database Storage; 08–09 — Indexes & Filters | Que custos introduz a organização física? |
| Execução | 12 — Joins Algorithms; 13–14 — Query Execution; 15 — Query Planning & Optimization | Por que consultas equivalentes têm custos diferentes? |
| Concorrência | 16 — Concurrency Control Theory; 19 — Multi-Version Concurrency Control | Que comportamentos podem ocorrer entre transações? |
| Recuperação | 20 — Database Logging; 21 — Database Recovery | Que informação permite recuperar após falhas? |

## Como usar

Proposta: começar pelo modelo e SQL, avançar para armazenamento e execução, depois concorrência e recuperação. Rever estruturas de dados, memória e concorrência quando necessário. Projetos de implementação exigem preparação adicional em C++; não são obrigatórios para ler todas as aulas conceptuais.

Para cada bloco, produzir síntese própria, pergunta ainda aberta e comparação com requisitos definidos. Ligar transações ao [DAD-001](01-transacoes-e-limites.md), sem confundir mecanismos do curso com garantias específicas de PostgreSQL. Registar novas leituras em [fontes](fontes.md).

## Lacunas que o curso não encerra

- Modelação conceptual, normalização e evolução de esquemas.
- Migrações, administração, backup, restauro e recuperação operacional.
- Seleção de modelos documentais, chave-valor, grafos e séries temporais.
- Integração entre integridade, segurança e requisitos do domínio.

Selecionar fontes próprias para estes assuntos antes de considerar o pilar coberto. O laboratório PostgreSQL já preparado continua pendente; esta curadoria não altera o seu estado.
