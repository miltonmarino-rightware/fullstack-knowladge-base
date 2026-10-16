# FRT-001 — Navegador, semântica e interação

- **Pilar:** Frontend.
- **Estado:** síntese documental inicial; interface e desempenho não testados.
- **Autor/revisor:** assistente; revisão independente pendente.
- **Data:** 2026-10-16.
- **Contexto:** documentação MDN contínua; nenhum navegador/versionamento de ensaio fixado.

## 1. Pergunta e âmbito

Como relacionar o documento, a imagem apresentada e as ações disponíveis ao utilizador? Esta introdução não cobre todo o event loop, frameworks ou conformidade de acessibilidade.

## 2. Investigar

[Fontes](fontes.md): frontend-F003, How browsers work, secções Parsing e Render; frontend-F004, button, introdução e atributos. O modelo documental precisa de medições para diagnosticar uma interface concreta.

## 3. Compreender

O navegador analisa HTML e CSS e constrói representações do documento e dos estilos. O cálculo de estilos determina a apresentação; layout calcula geometria; pintura produz a representação visual e composição reúne camadas quando aplicável. Alterações podem exigir repetir parte desse trabalho. É um modelo conceptual: não implica que toda mudança percorra sempre todas as etapas. [frontend-F003]

Um botão HTML fornece um controlo interativo nativo, acionável por diferentes formas de entrada. O atributo `type="button"` explicita uma ação sem submissão de formulário. `disabled` impede interação e foco. [frontend-F004]

## 4. Questionar

Inferência para o estudo: uma captura de ecrã mostra aparência, mas não prova que uma ação seja utilizável pelo teclado ou compreensível por tecnologia de apoio. Do mesmo modo, uma alteração visual rápida numa máquina não caracteriza desempenho noutros dispositivos.

## 5. Comparar

Comparação de estratégias para uma ação simples, como proposta de implementação:

| Estratégia | Motivo para escolher | Trabalho a verificar |
| --- | --- | --- |
| Botão HTML | A ação corresponde a um controlo nativo | Texto, foco e resultado da ação |
| Controlo personalizado | Requisito de interação realmente diferente | Semântica, entradas e estados completos |
| Componente de framework | Integração com aplicação existente | HTML final e comportamento efetivo |

A escolha de framework não foi avaliada nesta etapa.

## 6. Modelar

No exemplo proposto, distinguir: estado da aplicação (pedido ainda não enviado), estado visual (botão apresentado) e resultado da operação (resposta do serviço). Alterar o texto do botão não demonstra sucesso no servidor; ver [contratos de API](../backend/02-contratos-de-api.md).

## 7. Decidir

Começar com o controlo nativo para a ação simples. Definir estados de espera, sucesso e erro antes de integrar rede. Esta decisão é limitada ao exemplo, não é uma conclusão sobre qualquer sistema de design.

## 8. Construir

Fragmento próprio para discussão, sem ligação a serviço e ainda não ensaiado:

```html
<button type="button" id="pedir">
  Pedir empréstimo do equipamento
</button>
```

O fragmento define o controlo, mas não implementa o empréstimo. A próxima implementação deve especificar o que acontece ao ativar, falhar e tentar novamente. Evitar tratar uma maquete como funcionalidade concluída.

## 9. Testar

Plano pendente para a futura interface:

| Questão | Evidência a recolher |
| --- | --- |
| A ação é localizável e acionável pelo teclado? | Percurso, foco e resultado em navegador identificado |
| O controlo tem nome e estado compreensíveis? | Inspeção da árvore de acessibilidade e ensaio assistivo |
| O erro permite recuperar? | Cenário de falha e nova tentativa |
| Que trabalho ocorre numa atualização visual? | Registo de desempenho com ação, dispositivo e versão |

Nenhum destes ensaios foi realizado. Não há benchmark nem auditoria de conformidade.

## 10. Consolidar e rever

Perguntas de compreensão: qual a diferença entre layout e pintura? O que falta ao fragmento para funcionar? Como distinguir sucesso visual de sucesso da operação?

Próximas unidades: formulários, CSS responsivo, DOM/eventos e acessibilidade de estados dinâmicos. Reavaliar com uma interface completa e com as unidades do percurso MDN e web.dev.

[Índice](README.md) · [Pendências](perguntas.md)
