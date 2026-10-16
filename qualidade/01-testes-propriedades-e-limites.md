# QLD-001 — testes, propriedades e limites da evidência

- **Estado:** síntese documental inicial; exercícios não executados.
- **Revisão:** ChatGPT/Codex, 2026-10-16.
- **Pré-requisitos:** funções, entradas/saídas e regras de negócio.

## Pergunta e investigação

Como escolher verificações que possam revelar defeitos relevantes?

Fontes em [qualidade-F001 a F003](fontes.md): The Fuzzing Book, introdução oficial de Hypothesis e notas CSC148 da Universidade de Toronto. Foram consultadas as secções introdutórias e exemplos indicados; não foram concluídos cursos.

## Compreender

Executar um teste, gerar entradas e avaliar resultados são atividades distintas que podem ser automatizadas. Testes não garantem ausência de defeitos: a conclusão depende dos cenários e verificações realizados. [F001]

Testes baseados em propriedades descrevem relações que devem manter-se para entradas do domínio definido. As notas de Toronto apresentam essa passagem de exemplos escolhidos para propriedades gerais. A propriedade continua a ser formulada por quem testa; escolher uma afirmação fraca pode deixar erros invisíveis. [F003]

Hypothesis permite declarar estratégias de geração e usar given para fornecer entradas ao teste. A introdução demonstra comparação entre uma ordenação e uma referência. Isso é uma técnica concreta de Python; não torna Python obrigatório na base. [F002]

## Modelar — exemplo próprio

Reutilizar a regra: um exemplar tem no máximo um empréstimo ativo.

| Verificação proposta | Pergunta | Limite |
| --- | --- | --- |
| Caso permitido e caso negado | A regra responde corretamente a exemplos conhecidos? | Não percorre todas as combinações |
| Sequências de operações | Emprestar/devolver repetidamente preserva invariantes? | Depende das operações e estados gerados |
| Integração com persistência | O estado gravado corresponde à decisão? | Não prova comportamento de todas as falhas |
| Pedidos concorrentes | Duas tentativas preservam a exclusividade? | Exige coordenação real e ambiente registado |
| Contrato externo | Respostas e erros respeitam o acordo com o consumidor? | Não demonstra toda a correção interna |

A tabela é uma estratégia proposta, não um conjunto de resultados.

## Questionar

Um teste que compara a saída consigo própria passa sem verificar a regra. Um substituto em memória pode omitir restrições ou concorrência presentes na base de dados. Uma propriedade válida apenas para entradas positivas não responde ao comportamento de zero, negativos ou valores fora do formato.

Definir o oráculo: qual observação distingue correto de incorreto? Se houver uma implementação de referência, avaliar se é suficientemente independente para não reproduzir o mesmo defeito.

## Comparar e decidir

Casos explícitos comunicam regras e regressões conhecidas. Propriedades ajudam a explorar variações; integração verifica fronteiras reais. Escolher segundo o risco, sem impor uma proporção universal de tipos de teste.

Decisão pedagógica: escrever primeiro a regra e um contraexemplo; depois escolher a técnica. Não iniciar pelo objetivo de acumular testes.

## Construir, testar e rever

Percurso proposto: introdução do Fuzzing Book → notas CSC148 §2.4 → introdução Hypothesis. Preparar Python apenas para executar os exemplos desses recursos.

Exercícios pendentes: escolher uma propriedade útil, desenhar uma implementação errada que a viole e definir como reproduzir uma falha encontrada. **Nenhuma execução foi efetuada nesta atualização.**

Faltam estratégia ampla de qualidade, revisão de código, acessibilidade, desempenho, contratos e observabilidade. A nota complementa [ameaças e evidências](../seguranca/01-ameacas-controlos-e-evidencias.md).
