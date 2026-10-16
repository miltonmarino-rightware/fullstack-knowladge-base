# FND-001 — revisão e integração do relatório complementar

**Data:** 2026-10-16.
**Documento recebido:** FND-001 — Percurso de um pedido numa aplicação web.pdf.
**Origem:** anexo fornecido pelo utilizador no seguimento da tarefa para Perplexity; sessão original da ferramenta não inspecionada.
**SHA-256 do PDF:** ac530c40a37f33c93e179ef5ca5bfe44d75b75177c09643ffc316ac36404f799.
**Base comparada:** commit 6310497b96e446d3864672ff8cb737819060d397.
**Resultado:** contribuições documentais integradas; validação prática pendente.

## Limite da revisão externa

O PDF declara não ter acedido ao estudo nem ao repositório. Portanto, as suas sete correções são hipóteses condicionais, não falhas demonstradas no FND-001. Nesta integração lemos o texto existente e verificámos as referências necessárias às alterações. Não validámos integralmente todos os 29 links da bibliografia.

## Decisões sobre as sete correções propostas

| Proposta condicional do PDF | Situação no estudo original | Decisão |
| --- | --- | --- |
| Não equiparar pedido a processo | §4 já recusava correspondência assumida | Manter e acrescentar definição de thread com OSTEP cap. 26 |
| Não exigir DNS em cada pedido | §2 não fazia essa afirmação; detalhe estava pendente | Aprofundar cache DNS e distinguir resolução de encaminhamento |
| Não generalizar TCP a HTTP | §2 já distinguia HTTP/3 e QUIC | Sem correção necessária |
| Não interpretar sucesso HTTP como conclusão de tudo | §3 remetia à semântica, mas sem exemplo específico | Acrescentar 200/202 e obrigação de explicitar o contrato |
| Não tratar timeout como certeza de falha | §6 já explicava a incerteza | Manter e preparar experiência controlada |
| Não inferir exactly-once de transações | O estudo não prometia exactly-once | Explicitar fronteiras e manter padrões distribuídos pendentes |
| Não impor frontend + API + base de dados | §7 já questionava a necessidade de backend numa página fixa | Manter comparação, sem escolher stack |

## Ajustes necessários ao próprio relatório

1. **Sucesso HTTP:** a formulação genérica de processamento concluído é demasiado ampla. 202 representa aceitação com processamento pendente. Usar o código concreto e o contrato. Fonte: fundamentos-F002, §15.3.3.
2. **Referência da persistência:** a tabela do PDF indica RFC 9112 §9.1; a secção pertinente é §9.3. Fonte: fundamentos-F007.
3. **Cache e ligação:** menor tempo ou tamanho transferido não demonstra reutilização da ligação. Os mecanismos precisam de evidências distintas; o laboratório foi reformulado.
4. **DNS:** evitar a frase absoluta de que só há consultas quando a cache expirou. O modelo introdutório não esgota comportamentos de clientes e resolvedores. A RFC 1034 é uma base histórica, não cobertura de todas as extensões.
5. **Página estática:** dispensar backend de negócio próprio não significa ausência de software servidor em execução. Essa distinção é pedagógica; não se deve concluir que servir ficheiros elimina processos.
6. **Metadados bibliográficos:** a data “2026-08-13” atribuída à documentação PostgreSQL no PDF não foi confirmada; não foi importada como data de publicação. Mantemos versão 18 e data de consulta.
7. **Padrões distribuídos:** outbox e exactly-once exigem fontes e estudos específicos antes de se tornarem orientações da RIGHTWARE.

## Verificação efetuada

Consultámos RFC 9111 para cache, RFC 9112 para persistência, RFC 9110 para 202, RFC 1034 para o modelo DNS e o capítulo de threads publicado pelos autores de OSTEP. Reconsultámos o tutorial PostgreSQL 18 para o âmbito introdutório das transações. Ver [registo de fontes](fontes.md).

## Evidências e próximos passos

- Síntese atualizada: [FND-001](01-percurso-de-um-pedido.md).
- Experiências propostas: [laboratórios](laboratorios-fnd-001.md).
- Os laboratórios não foram executados nesta revisão.
- Para nova revisão externa linha a linha, fornecer o conteúdo Markdown diretamente se o acesso ao GitHub voltar a falhar.
- O PDF foi identificado por nome e hash; não foi republicado integralmente. O conteúdo consolidado acima é uma análise própria.
