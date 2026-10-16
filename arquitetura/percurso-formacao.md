# Arquitetura — referências complementares e lacunas

**Data:** 2026-10-16. **Estado:** seleção parcial; arquitetura modular ainda sem percurso principal.
[Revisão da Parte II](../REVISAO-FORMACAO-PARTE-II.md).

## Fiabilidade — R12, Google SRE

[Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), capítulo público em inglês. Secções de indicadores e objetivos consultadas: SLI identifica uma medida do serviço; SLO define o alvo para essa medida.

Proposta de estudo: escolher uma necessidade do utilizador, definir indicador, população observada, janela temporal e alvo justificado. Distinguir medição do cliente e do servidor. Não copiar alvos numéricos dos exemplos como política da empresa.

O capítulo apoia requisitos mensuráveis; não resolve sozinho fronteiras, dependências e modularidade. Exercício não executado.

## Distribuição

MIT 6.5840 permanece aprofundamento após sistemas, redes e concorrência. A Parte II menciona 2024; o catálogo R10 regista 2026. Não misturar materiais sem fixar edição.

É legítimo estudar distribuição para capacitação futura, mesmo sem projeto atual. A decisão de adotar distribuição num produto exige requisitos próprios.

## Lacunas e produção esperada

Procurar curso/livro de arquitetura de software e fontes originais para requisitos, modularidade, diagramas e registo de decisões. Uma nota futura deverá relacionar requisito, alternativas, decisão, consequências e condição de revisão.

SRE e OWASP ficam como complementos transversais. Esta curadoria não constitui formação completa em arquitetura.
