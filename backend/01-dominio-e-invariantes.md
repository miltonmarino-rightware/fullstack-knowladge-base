# BCK-001 — domínio, invariantes e casos de uso

- **Estado:** síntese documental inicial; exemplos propostos, não executados.
- **Revisão:** ChatGPT/Codex, 2026-10-16.
- **Âmbito:** modelar regras e separar responsabilidades antes de escolher framework.
- **Pré-requisitos:** programação, objetos/funções e transações básicas.

## Pergunta e investigação

Como transformar uma regra de negócio numa responsabilidade explícita, incluindo situações em que pedidos concorrem?

Fontes: [backend-F002, F003 e F004](fontes.md), capítulos 1, 4 e 7 de Architecture Patterns with Python. Foram consultadas as secções sobre linguagem de domínio, serviços e fronteiras de consistência; o livro não foi concluído. Python é o veículo didático, não uma escolha obrigatória.

## Compreender

Um modelo de domínio representa os conceitos e regras relevantes para o problema. A estrutura de tabelas não basta para explicar quais mudanças são permitidas. Entidades distinguem-se pela identidade ao longo do tempo; objetos de valor pelo valor que representam. A escolha depende do significado no domínio, não apenas da forma dos dados. O capítulo 1 propõe esclarecer o vocabulário com especialistas e exemplos concretos. [F002]

A camada de aplicação coordena um caso de uso: obtém informação, invoca regras e conduz a persistência. Um serviço de domínio expressa uma regra que não pertence naturalmente a uma entidade ou objeto de valor. Dar a ambos o nome “service” não torna as suas responsabilidades iguais. [F003]

Um agregado delimita objetos que precisam de permanecer consistentes numa operação. A fronteira deve resultar das regras; juntar todo o sistema num agregado pode criar contenção, enquanto separar demais dificulta preservar invariantes. A proteção em memória não elimina concorrência entre processos. [F004]

## Modelar — exemplo próprio

Considere uma biblioteca de empréstimo de equipamentos, com exemplares físicos identificados.

| Conceito | Decisão proposta | Regra |
| --- | --- | --- |
| Exemplar | Entidade com identificador estável | Tem no máximo um empréstimo ativo |
| Intervalo de utilização | Objeto de valor | Fim posterior ao início |
| Empréstimo | Entidade com ciclo de vida | Apenas um empréstimo ativo pode ser devolvido |
| Emprestar exemplar | Caso de uso | Verifica elegibilidade, disponibilidade e regista a mudança |

Fluxo proposto: identificar o utilizador → autorizar → carregar o estado → aplicar a regra → persistir de forma protegida contra concorrência → responder.

A autorização controla quem pode tentar; a regra do domínio controla se a mudança faz sentido. Não aceitar do cliente uma indicação de “disponível” como verdade.

## Questionar

Contraexemplo: dois pedidos leem o mesmo exemplar disponível. Ambos passam numa verificação local. Sem proteção no armazenamento, ambos podem registar empréstimos. Uma classe bem encapsulada não prova a invariável global.

A escolha concreta entre restrição de unicidade, bloqueio ou controlo de versão depende do modelo e da base de dados. Ver [transações e limites](../dados/01-transacoes-e-limites.md). Não foi escolhida nem testada uma implementação nesta nota.

## Comparar e decidir

| Opção | Adequação proposta | Custo |
| --- | --- | --- |
| Procedimento simples com regras explícitas | Poucas operações e regras estáveis | Duplicação possível ao crescer |
| Modelo de domínio com operações próprias | Regras combinadas e evolução frequente | Mais abstrações e necessidade de vocabulário consistente |

Decisão pedagógica: modelar primeiro uma operação e os seus contraexemplos. Não introduzir todos os padrões do livro por antecipação.

## Construir, testar e rever

Exercícios propostos: formular casos de empréstimo permitido, exemplar ocupado, devolução repetida e duas tentativas simultâneas. Separar testes de regras dos testes da proteção transacional. **Nenhum foi executado.**

Pendências: descoberta de domínio com especialistas, fronteiras entre contextos, estratégias de concorrência e efeitos externos. Reavaliar o modelo quando surgir uma regra que o vocabulário atual não consegue expressar.
