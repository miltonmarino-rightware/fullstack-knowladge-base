# FND-001 — tarefa de pesquisa para Perplexity

**Estado:** relatório complementar recebido em 2026-10-16; contribuições integradas. O relatório não acedeu ao estudo original; revisão externa linha a linha continua pendente. Ver [decisões](revisao-fnd-001.md).
**Destino da revisão:** [estudo inicial](01-percurso-de-um-pedido.md).
**Data:** 2026-10-16.

Copiar o texto abaixo para o Perplexity. Disponibilizar também o estudo e o registo de fontes, por conteúdo ou links acessíveis.

---

Investiga e revê criticamente o percurso de um pedido numa aplicação web, para a base de conhecimento full stack da RIGHTWARE. O objetivo é aprender mecanismos e limites antes de escolher frameworks.

Não assumes que todos os sistemas precisam de frontend separado, API e base de dados. Compara uma página estática com uma aplicação que altera dados. Explica o percurso entre navegador, DNS, transporte, HTTP, processo do servidor e armazenamento. Distingue HTTP/1.1, HTTP/2 e HTTP/3; não generalizes TCP a todas as versões.

Aprofunda estas perguntas:
1. Quando há resolução DNS, caches ou reutilização de ligações?
2. O que distingue programa, processo, thread e pedido HTTP? Que correspondências não podemos assumir?
3. O que o sucesso HTTP permite concluir? E o que continua desconhecido depois de um timeout?
4. O que uma transação de base de dados garante dentro do seu âmbito? Que efeitos externos ficam de fora?
5. Como investigar retries, idempotência e duplicação sem prometer exactly-once de ponta a ponta?
6. Que simplificações do estudo inicial precisam de ser corrigidas ou delimitadas?

Prioriza especificações IETF, documentação oficial dos sistemas e materiais universitários publicados pelos autores. Parte das RFCs 9110 e 9114, do capítulo 4 de Operating Systems: Three Easy Pieces e do tutorial de transações do PostgreSQL 18. Procura fontes adicionais quando estas forem insuficientes.

Entrega:
- mapa de conceitos e pré-requisitos;
- explicação dos mecanismos e exceções;
- tabela por afirmação: conclusão, URL original, secção, versão/data, limites e grau de certeza;
- divergências entre fontes e forma de as resolver;
- correções propostas ao estudo, cada uma com evidência;
- três experiências pequenas, com pré-requisitos, procedimento, resultado esperado e limitações;
- perguntas ainda sem resposta.

Não inventes fontes, versões ou testes. Identifica material inacessível. Se não conseguires ler o repositório, declara isso e pede o conteúdo; não simules uma revisão. Não escolhas uma stack nem faças recomendações universais. Escreve em português.

---

## Receção e integração

Quando houver resposta: registar data, consulta utilizada e relatório; abrir as fontes originais; aceitar ou rejeitar cada correção com motivo. Atualizar o estudo e as perguntas. Não marcar revisão concluída apenas por receber texto.
