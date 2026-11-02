# FND-002 — Escolher estruturas de dados e interpretar custos

- **Pilar:** Fundamentos.
- **Data:** 2026-11-02.
- **Estado:** síntese documental; exercício implementado e verificado num domínio finito; sem benchmark.
- **Autor/revisor:** assistente; revisão independente pendente.
- **Contexto:** MIT 6.006, Spring 2020, notas das aulas 2 e 4.

## 1. Pergunta e âmbito

Como escolher uma estrutura a partir das operações necessárias? Estudamos coleções em memória. Concorrência, armazenamento persistente e particularidades de bibliotecas precisam de estudos próprios.

## 2. Investigar

Fontes primárias consultadas: [fundamentos-F010 e F011](fontes.md), ligadas ao recurso R02 do [catálogo](../CATALOGO-FORMACAO.md). Foram lidas as notas textuais indicadas; não se declara visualização dos vídeos nem conclusão do curso.

## 3. Compreender

A interface define operações; a representação determina como realizá-las. Uma sequência permite acesso por posição; um dicionário procura por chave. Arrays permitem acesso por índice em tempo constante no modelo adotado. Listas ligadas percorrem nós para chegar a uma posição, mas permitem alterações constantes na cabeça. [F010]

Arrays dinâmicos reservam capacidade adicional. Uma expansão pode copiar muitos elementos; distribuir esse custo por uma sequência de inserções no fim produz custo amortizado constante. Isso não garante baixa latência para cada inserção. [F010]

Hashing associa chaves a posições numa tabela. Colisões exigem resolução. Com encadeamento, distribuição adequada e fator de carga controlado, a pesquisa tem custo esperado constante; uma cadeia concentrada pode exigir percurso linear. Redimensionamento acrescenta análise amortizada. [F011]

## 4. Questionar

“Esperado” depende de um modelo probabilístico; “amortizado” distribui custo por operações. Nenhum equivale automaticamente a pior caso constante. A análise também pressupõe custos para comparar, copiar e calcular hashes: chaves de tamanho variável podem exigir outro parâmetro. [F010, F011]

## 5. Comparar

Custos no modelo das notas, para n elementos; operações indicadas explicitamente:

| Representação | Operação | Custo e condição |
| --- | --- | --- |
| Array dinâmico | Ler por índice | O(1) |
| Array dinâmico | Inserir no fim | O(1) amortizado; expansão individual O(n) |
| Lista simplesmente ligada com cabeça | Inserir na cabeça | O(1) |
| Lista simplesmente ligada | Procurar uma posição arbitrária | O(n) |
| Array ordenado | Procurar por chave | O(log n), por pesquisa binária |
| Array ordenado | Inserir mantendo ordem | O(n), por deslocações |
| Tabela hash com encadeamento | Procurar por chave | O(1) esperado nas hipóteses acima; O(n) no pior caso |

Fontes: F010 para sequências; F011 para procura por chave. Esta tabela não mede implementações reais.

## 6. Modelar — exercício próprio

Requisito fictício: receber códigos inteiros e indicar a primeira repetição, preservando a ordem de leitura. Para a entrada [8, 3, 8, 5], a resposta deve ser 8.

Alternativa A: guardar os códigos anteriores numa sequência e comparar cada novo código com todos eles. Num lote de n códigos distintos, são feitas 0 + 1 + … + (n−1) comparações de igualdade.

Alternativa B: manter um conjunto de códigos vistos e consultar pertença antes de inserir.

## 7. Decidir

Para este exercício, um conjunto é candidato natural porque a operação relevante é pertença. A implementação deve ser escolhida depois de definir limites de memória, tamanho das chaves e exigências de pior caso. Ordenar primeiro o lote altera a ordem de descoberta e exige trabalho adicional para cumprir o contrato.

## 8. Construir — pseudocódigo próprio

```text
vistos ← conjunto vazio
para cada codigo, na ordem recebida:
    se codigo pertence a vistos:
        devolver Encontrado(codigo)
    inserir codigo em vistos
devolver Ausente
```

Invariante proposto: antes de cada iteração, vistos contém exatamente os códigos do prefixo já processado. Assim, uma pertença identifica repetição; a paragem imediata respeita a primeira ocorrência repetida na leitura.

## 9. Testar

Casos de revisão manual propostos:

| Entrada | Resultado esperado |
| --- | --- |
| [] | Ausente |
| [0] | Ausente |
| [0, 0] | Encontrado(0) |
| [8, 3, 8, 3] | Encontrado(8) |

Os casos acima foram executados em 2026-11-02 no [L04 — código e evidência](laboratorios/l04-primeiro-repetido/README.md), juntamente com outros três exemplos e 19.531 sequências do domínio finito descrito no laboratório. Não houve falhas. A implementação usa None para ausência sob o contrato de códigos inteiros, distinguindo-o de zero. Esta evidência não é benchmark nem prova universal.

## 10. Consolidar e rever

Perguntas: por que ordenar não resolve diretamente o contrato? Onde entra o custo do hash? Que requisito justificaria trocar a representação? Por que medir um lote pequeno não prova um limite assintótico?

Próximas unidades: análise formal de complexidade, pesquisa binária com invariantes, árvores equilibradas e filas de prioridade. Para reutilizar, registar requisitos, operação dominante, hipóteses e evidência da implementação escolhida.

[Índice](README.md) · [Percurso universitário](percurso-formacao.md)
