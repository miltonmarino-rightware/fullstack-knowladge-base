# NotebookLM — estudo de aulas e integração no conhecimento

**Data:** 2026-10-16. **Estado:** fluxo proposto; nenhuma importação ou sessão NotebookLM executada aqui.

## Papel no trabalho

| Ferramenta/pessoa | Responsabilidade |
| --- | --- |
| Perplexity | Descobrir e comparar fontes; entregar relatórios autónomos |
| NotebookLM | Ajudar a explorar materiais selecionados e produzir notas ligadas às fontes |
| ChatGPT/Codex e revisão humana | Confrontar afirmações com originais, corrigir sínteses e integrar no GitHub |
| GitHub | Manter conhecimento revisto, referências, perguntas e histórico |

A concordância entre ferramentas não constitui verificação independente. Um resumo gerado continua a precisar de revisão.

## Capacidade confirmada e limites

A [ajuda oficial Google](https://support.google.com/notebooklm/answer/16215270?hl=en), consultada nesta data e redirecionada para ajuda Gemini Notebook, indica suporte a vídeos públicos do YouTube com legendas, incluindo automáticas. A importação por URL usa apenas a transcrição textual. Por isso, código ou diagramas mostrados sem descrição verbal precisam de consulta visual separada. Vídeos recentes podem não estar disponíveis para importação.

Não foi testada a importação na conta do utilizador. Verificar se a fonte ficou disponível antes de pedir um resumo.

## Organização sugerida

Começar com um notebook por curso ou tema delimitado, por exemplo “RIGHTWARE — Linguagens — Referências e coleções”. Associar o pilar no nome. Adicionar a aula e, quando possível, notas/slides/código originais pertinentes, respeitando os direitos de uso.

Evitar misturar relatórios de IA e fontes primárias sem identificação. Se um relatório for incluído, nomeá-lo como análise secundária não validada.

## Primeiro estudo proposto

- Curso: CS61B Spring 2026, UC Berkeley.
- Unidade do [calendário oficial](https://sp26.datastructur.es/): aula 3, “Lists, Arrays, Maps, References”.
- [Vídeo ligado pelo calendário](https://www.youtube.com/watch?v=ZumKK42NHbc).
- Objetivo: explicar a relação entre variável, referência e objeto; distinguir comportamentos observáveis de inferências sobre implementação.
- Preparação: programação básica; aulas 1–2 como revisão se houver lacunas.
- Estado: URL/título localizados; vídeo não assistido, legendas e importação não verificadas.

## Prompt para copiar no NotebookLM

Produz uma ficha de estudo em português para a base RIGHTWARE, usando apenas as fontes selecionadas neste notebook.

1. Identifica título, autor, URL, edição e quais materiais sustentam a resposta. Não inventes metadados em falta.
2. Formula a pergunta central e explica os conceitos e mecanismos, com pressupostos e limites.
3. Associa cada afirmação técnica relevante à fonte. Usa minutos apenas se estiverem disponíveis e forem verificáveis; caso contrário, cita a passagem sem inventar tempo.
4. Explica um exemplo existente na fonte. Se propuseres um exemplo novo, identifica-o como proposta e não como código executado.
5. Destaca o que não é possível confirmar apenas pela transcrição: código, diagramas, demonstrações ou resultados visuais.
6. Separa afirmações da fonte, inferências e dúvidas. Indica contradições entre fontes.
7. Propõe cinco perguntas de compreensão e dois exercícios, sem fingir que foram resolvidos.
8. Termina com pontos que precisam de revisão no material original e ligações com outros pilares.
Não reproduzas longos trechos. Não declares domínio, validação prática ou visualização integral do vídeo.

## Devolução e integração

O utilizador pode trazer o texto/PDF produzido, acompanhado das URLs originais. Na revisão:
- Abrir as fontes que sustentam as conclusões integradas.
- Conferir código e elementos visuais quando forem necessários.
- Produzir síntese própria no pilar, ligando à fonte e à unidade.
- Registar separadamente “resumo recebido”, “fonte consultada”, “síntese revista” e “exercício executado”.
- Atualizar índice, perguntas e fontes. Só guardar resultados de execução quando existir evidência.

Não publicar transcrições integrais nem cópias indiscriminadas das aulas. O repositório guarda sínteses próprias, referências e evidências autorizadas.
