# SEG-001 — ameaças, controlos e evidências

- **Estado:** síntese documental inicial; exemplo proposto, sem testes executados.
- **Revisão:** ChatGPT/Codex, 2026-10-16.
- **Âmbito:** raciocínio de segurança de uma aplicação; não é auditoria completa.

## Pergunta e fonte

Como relacionar o que queremos proteger com uma ameaça e uma verificação concreta?

Fonte [seguranca-F001](fontes.md): OWASP Threat Modeling Cheat Sheet, secções Overview e System Modeling. A referência organiza o raciocínio em compreensão do sistema, problemas possíveis, respostas e revisão. O modelo deve evoluir com a aplicação; precisa de mostrar dados, fluxos, processos, armazenamento e fronteiras de confiança.

Essa abordagem ajuda a escolher controlos segundo o contexto. Uma lista genérica de vulnerabilidades não descreve, sozinha, os riscos específicos de um sistema.

## Modelar — exemplo próprio

Considere uma aplicação de empréstimo de equipamentos: utilizador → API → dados de empréstimos. O cliente envia pedidos, mas não é autoridade sobre identidade, permissões ou disponibilidade.

| Ativo/regra | Ameaça considerada | Controlo proposto | Evidência a procurar |
| --- | --- | --- | --- |
| Dados de outro utilizador | Consultar um empréstimo alheio alterando o identificador | Autorização sobre recurso e ação no servidor | Casos permitidos e negados entre utilizadores |
| Integridade do empréstimo | Dois pedidos confirmam o mesmo exemplar | Regra de domínio e proteção transacional | Execução concorrente preserva a invariável |
| Credenciais e tokens | Segredos aparecem nos logs | Evitar registo de segredos e restringir acesso aos logs | Inspeção de amostras e configuração |
| Disponibilidade | Operações caras consomem recursos sem limite | Limites compatíveis com a operação e observação de carga | Medições e comportamento de rejeição |

Tudo na tabela é proposta didática. Não demonstra que algum sistema da RIGHTWARE tenha esses controlos ou vulnerabilidades.

## Questionar e comparar

Uma resposta negada na interface não prova autorização no servidor. Da mesma forma, login bem-sucedido não autoriza qualquer recurso. Relacionar com a [referência de autorização](../backend/percurso-formacao.md).

Comparação proposta: controlos preventivos procuram impedir a ação; controlos de deteção ajudam a observá-la; mecanismos de recuperação tratam consequências. Podem complementar-se, mas cada um exige evidência própria.

Priorizar pelo impacto, exposição e plausibilidade no contexto. Evitar números de risco aparentemente precisos sem dados. Registar também o risco que permanece depois do controlo.

## Decidir, construir e testar

Para cada ameaça selecionada, documentar pressupostos, responsável pela verificação, evidência e condição de revisão. Executar testes apenas em ambientes próprios ou autorizados. Nenhum teste de segurança foi feito nesta pesquisa.

Percurso inicial proposto: ler a referência OWASP → desenhar um fluxo → identificar uma fronteira de confiança → justificar ameaças → definir verificações. PortSwigger R11 é complemento para estudo prático, sem presumir conclusão de laboratórios.

Pendências: sessões, gestão de segredos, dependências, infraestrutura, resposta a incidentes e critérios de verificação mais completos.
