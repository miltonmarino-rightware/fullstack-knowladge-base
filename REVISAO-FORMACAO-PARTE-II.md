# Revisão da formação — Parte II

**Data:** 2026-10-16. **Estado:** integração parcial com correções; formação não concluída.
Entrada: “Formação RIGHTWARE — Parte II.pdf”, relatório externo entregue pelo utilizador.
SHA-256: 5ed01837f3c7894e484f4516028085e9c3eff6a08a957bcdd51bc4afe5ab998e.

## Avaliação

O relatório contribui para Linguagens e Frontend e reúne referências complementares para Backend e Arquitetura. Não resolve modelação de domínio, design de APIs ou arquitetura modular. A afirmação de que os quatro pilares estão cobertos deve ser entendida como mapa parcial, não percurso completo.

## Decisões de revisão

| Afirmação/seleção do relatório | Decisão desta revisão |
| --- | --- |
| CS61B como principal de Linguagens | Aceitar para Java, referências, estruturas e engenharia de programas; não basta para paradigmas, compiladores e comparação de runtimes |
| Entradas CS61B ainda “a confirmar” | Fixar Spring 2026 e selecionar títulos efetivos do calendário |
| TypeScript Interfaces | Substituir a página antiga, que declara estar descontinuada, por Object Types no Handbook atual |
| Release notes 5.5 como referência de versão | Não usar uma página de release notes para datar todo o manual; fixar compilador e configuração quando houver estudo executável |
| MDN “não é um curso de frameworks” | Qualificar: o percurso inclui módulos de frameworks/bibliotecas e React; a nossa seleção inicial privilegia a plataforma web |
| MDN com consulta em 2025-10-29 | Não transportar essa data como consulta desta revisão; fontes reabertas em 2026-10-16 |
| OWASP como principal de Backend | Reclassificar como complemento de segurança; domínio, contratos e integração continuam em aberto |
| SRE como principal de Arquitetura | Reclassificar como complemento de fiabilidade e requisitos mensuráveis; não cobre sozinho modularidade e decisões arquiteturais |
| MIT 6.5840 2024 com URL móvel | Preservar a edição 2024 indicada pelo relatório sem a confundir com R10/2026; detalhes não revalidados nesta revisão |
| Distribuídos apenas perante necessidade atual | Ajuste pedagógico nosso: é legítimo estudar para capacitação futura após os pré-requisitos, sem exigir projeto comercial atual |
| Materiais não avaliados pelo Perplexity | Preservar verificações anteriores; não significam rejeição |

Fontes primárias reabertas:
- [CS61B Spring 2026 — calendário](https://sp26.datastructur.es/).
- [TypeScript — Interfaces, página antiga](https://www.typescriptlang.org/docs/handbook/interfaces.html) e [Object Types](https://www.typescriptlang.org/docs/handbook/2/objects.html).
- [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development).
- [web.dev — Accessibility](https://web.dev/learn/accessibility) e [Animation and motion](https://web.dev/learn/accessibility/motion/).
- [OWASP — Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).
- [Google SRE — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/).

Esta é uma verificação dirigida das contribuições integradas, não auditoria de todas as 47 referências do PDF. Não foram assistidos vídeos, concluídos cursos ou executados exercícios nesta revisão.

## Resultados e próxima investigação

Percursos parciais publicados em [Linguagens](linguagens/percurso-formacao.md), [Frontend](frontend/percurso-formacao.md), [Backend](backend/percurso-formacao.md) e [Arquitetura](arquitetura/percurso-formacao.md).

Prioridades ainda abertas:
1. Formação comparativa em paradigmas, avaliação, memória e runtimes.
2. Domínio/invariantes; contratos, erros, compatibilidade e evolução de APIs.
3. Modularidade, dependências, requisitos, diagramas e decisões.
4. Segurança, Qualidade, Infraestrutura e Entrega profissional.
5. Cursos e séries concretas em português, design de interação e motion aprofundado.

O [fluxo NotebookLM](FLUXO-NOTEBOOKLM.md) permite começar a estudar unidades já selecionadas enquanto a pesquisa continua. Não esperar pelo catálogo completo para produzir conhecimento.
