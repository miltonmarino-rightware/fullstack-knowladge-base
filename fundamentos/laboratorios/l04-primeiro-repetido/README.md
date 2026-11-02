# L04 — Primeira repetição na ordem de leitura

**Estudo:** [FND-002](../../02-estruturas-de-dados-e-custos.md).
**Execução:** 2026-11-02, CPython 3.12.14, Linux.
**Estado:** verificação funcional executada no domínio declarado.

## Contrato e escolha

Receber uma sequência finita de inteiros e devolver o valor cuja segunda ocorrência surge primeiro durante a leitura. Devolver `None` se não houver repetição. Como os valores válidos são inteiros, este sentinela distingue ausência de zero; o contrato não admite `None` como código. A pré-condição é responsabilidade do chamador; não há validador de entradas neste exercício.

Para [9, 2, 2, 9], a resposta é 2. Escolher o primeiro valor da entrada que se repete em algum lugar daria 9 e violaria o contrato.

A função usa um conjunto de valores vistos. Python foi escolhido para verificar o pseudocódigo sem dependências; isso não constitui escolha obrigatória para projetos.

## Reproduzir

Na raiz do repositório, com Python 3.10 ou superior:

```bash
python3 fundamentos/laboratorios/l04-primeiro-repetido/experimento.py
```

O programa escreve JSON na saída padrão e termina com erro se houver divergência. A evidência guardada corresponde à versão indicada acima; outras versões não foram ensaiadas.

- [Código integral](experimento.py)
- [Resultado observado](resultado.json), com SHA-256 do código executado.

## Verificações e resultado

Sete exemplos explícitos incluem vazio, ausência, zero repetido, negativos e ordem de deteção. Todos passaram.

Foram enumeradas todas as sequências de comprimento 0 a 6 sobre os cinco valores {-2, -1, 0, 1, 2}: soma de 5^k, para k de 0 a 6, totalizando **19.531 casos**. Não houve divergências.

O oráculo usa pares de índices, sem hashing. Além de comparar os resultados, verifica-se que o prefixo anterior à segunda ocorrência devolvida não contém duplicados. Esta propriedade ajuda a detetar uma resposta que identifica uma repetição posterior à primeira.

## Limites e aprendizagem

A enumeração é exaustiva apenas dentro do domínio finito declarado. Não cobre todas as sequências de inteiros, memória esgotada, concorrência ou entradas fora do contrato. Não há medições de tempo ou memória; o teste não confirma os custos assintóticos de uma implementação de conjunto.

Resultado de engenharia: a escolha da estrutura deve preservar o contrato semântico. Uma solução que devolve algum repetido pode estar errada mesmo que use uma estrutura eficiente.

Próxima investigação: pesquisa binária e invariantes, mantendo a formação universitária como percurso principal.
