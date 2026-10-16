# ENT-001 — documentação e passagem de responsabilidade

- **Estado:** síntese documental inicial; pacote e exercícios propostos.
- **Revisão:** ChatGPT/Codex, 2026-10-16.
- **Pergunta:** que informação permite a outra equipa continuar o trabalho sem depender da memória do autor?

## Investigar e compreender

Fontes: [entrega-F001 e F002](fontes.md).

Diátaxis distingue tutorial, guia de tarefa, referência e explicação. Um tutorial acompanha aprendizagem; um guia ajuda alguém preparado a realizar uma tarefa; a referência descreve factos técnicos; a explicação desenvolve contexto e razões. A escolha deve refletir a necessidade do leitor. [F001]

Google Technical Writing disponibiliza percursos de escrita técnica, incluindo trabalho individual e opções de sessões orientadas. A página informa que não atribui certificado e que os cursos são em inglês. Foi consultada a visão geral, não concluídas as lições. [F002]

## Modelar — pacote proposto

| Documento/artefacto | Pergunta que responde | Critério de revisão proposto |
| --- | --- | --- |
| README de entrada | O que é, para quem serve e onde começar? | Um novo leitor identifica o caminho adequado |
| Guia de instalação | Como preparar um ambiente suportado? | Outro operador consegue reproduzir os passos |
| Referência de configuração | Quais parâmetros existem e quais os seus efeitos? | Versões, valores admissíveis e segredos estão distinguidos |
| Arquitetura e ADRs | Porque existem estes limites e dependências? | Consequências e alternativas são rastreáveis |
| Contratos de interface | Como integrar e interpretar falhas? | Exemplos coincidem com o comportamento observado |
| Runbooks | Como diagnosticar e resolver uma situação delimitada? | Pré-condições, verificação e interrupção estão explícitas |
| Registo da entrega | O que foi entregue, aceite e ficou pendente? | Liga artefactos, versões, evidências e responsabilidades |

A tabela é uma proposta própria, não um conjunto obrigatório de ficheiros para todos os projetos. Um sistema pequeno pode reunir secções no mesmo documento, desde que permaneçam localizáveis.

## Questionar

Um ZIP entregue não demonstra que o destinatário tem acesso, configuração ou capacidade de operação. “Funciona na minha máquina” também não verifica instalação limpa.

Não guardar segredos na documentação. Explicar como o responsável autorizado obtém e gere o acesso. Diferenciar comportamento confirmado, decisão proposta e limitação conhecida.

## Comparar e decidir

Documentação curta e ligada ao código favorece manutenção, mas pode exigir uma entrada mais acessível para leitores não técnicos. Um documento extenso pode servir uma entrega institucional, mas não deve esconder procedimentos difíceis de encontrar.

Proposta: organizar pela tarefa e pelo leitor. Usar diagramas e [ADRs](../arquitetura/01-modulos-dependencias-e-decisoes.md) quando ajudam a compreender decisões; ligar a [operação e recuperação](../infraestrutura-e-producao/01-operacao-e-recuperacao.md).

## Construir, testar e rever

Ensaio de handoff proposto: fornecer a outra pessoa um commit e instruções; pedir instalação, uma operação funcional e localização de um procedimento de diagnóstico. Registar perguntas e passos ausentes; corrigir a documentação e repetir o trecho afetado.

**Este ensaio não foi executado.** Só depois de evidência real poderá servir ao marco de reutilização da base.

Pendências: requisitos e aceitação, formação de utilizadores, manutenção, suporte e controlo de alterações. [Percurso inicial](percurso-formacao.md).
