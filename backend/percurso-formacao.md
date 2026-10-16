# Backend — referências complementares e lacunas

**Data:** 2026-10-16. **Estado:** seleção parcial; não existe ainda percurso principal completo.
[Revisão da Parte II](../REVISAO-FORMACAO-PARTE-II.md).

## Segurança como complemento — R19

[OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), referência pública em inglês, consultada nas recomendações de autorização. Não é curso sequencial de backend.

Questões de estudo: quem pode executar que ação sobre que recurso? Como verificar permissões em cada pedido? Como impedir que um acesso legítimo a um recurso permita acesso indevido a outro? Preparação sugerida: HTTP, identidade e modelo de dados.

Proposta de evidência: matriz de decisões permitidas/negadas e casos de teste. Não executada nesta revisão. Consultar a folha específica de autenticação numa unidade própria; não tratar identidade e permissão como equivalentes.

## Requisitos operacionais

Os SLOs são complemento para requisitos de fiabilidade; ver [Arquitetura](../arquitetura/percurso-formacao.md). Não substituem invariantes de negócio.

## Lacunas prioritárias

Selecionar formação coerente em domínio e invariantes, contratos de APIs, compatibilidade, erros, paginação, idempotência, concorrência, tarefas assíncronas e integração. Full Stack Open permanece candidato já catalogado, não rejeitado pela ausência de avaliação na Parte II.

A futura síntese deve ligar cada regra de negócio aos seus limites transacionais e às falhas possíveis. [Transações](../dados/01-transacoes-e-limites.md) fornece investigação anterior, sem encerrar o tema.
