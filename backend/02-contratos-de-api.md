# BCK-002 — contratos de APIs e comportamento perante falhas

- **Estado:** síntese documental inicial; proposta didática, sem API implementada.
- **Revisão:** ChatGPT/Codex, 2026-10-16.
- **Âmbito:** API HTTP; não pretende cobrir todos os estilos de integração.
- **Pré-requisitos:** HTTP e [domínio/invariantes](01-dominio-e-invariantes.md).

## Pergunta e fontes

O que um consumidor precisa de saber para usar uma operação sem depender da implementação?

Fontes em [backend-F005 a F007](fontes.md): guia de desenho da Microsoft, RFC 9110 e RFC 9457. O guia contém recomendações; as RFCs definem semântica de protocolo e representação de erros nos respetivos âmbitos.

## Compreender

Uma API pode expor recursos do negócio sem refletir cada tabela. O guia Microsoft recomenda equilibrar respostas fragmentadas, que exigem muitas chamadas, com respostas excessivas, que transferem informação desnecessária. Nomes de recursos são parte do desenho, não prova suficiente de uma boa API. [F005]

Idempotência refere-se ao efeito pretendido de pedidos idênticos repetidos; não exige respostas byte a byte iguais. PUT e DELETE têm semântica idempotente; POST não a garante genericamente. If-Match permite condicionar uma alteração à representação conhecida, usando comparação forte de etiquetas, e prevenir sobrescritas acidentais. Uma condição falsa normalmente conduz a 412, com a exceção prevista para operação já realizada. [F006, §§9.2.2 e 13.1.1]

Problem Details fornece formato de erros legível por máquinas. Em application/problem+json, type identifica o tipo; title resume-o; detail explica a ocorrência; instance identifica-a. Quando presente, status deve concordar com o código HTTP. Consumidores não devem extrair lógica estruturada de detail; usar tipos/extensões documentados. Não expor detalhes internos de depuração indiscriminadamente. [F007, §§3 e 5]

## Modelar — contrato proposto para empréstimos

Exemplo próprio, não especificação aprovada de um produto:

| Aspeto | Decisão a documentar |
| --- | --- |
| Operação | POST /emprestimos solicita um empréstimo |
| Entrada | Identificador do exemplar e datas; distinguir campo ausente, nulo e inválido |
| Identidade | Obtida do contexto autenticado; acesso ao exemplar autorizado no servidor |
| Sucesso | 201 quando o recurso tiver sido criado; identificar o recurso resultante |
| Conflito de domínio | Definir erro para exemplar já emprestado e ação possível do consumidor |
| Timeout | Resultado incerto: definir consulta de estado e política de repetição |
| Listagem | Ordenação estável, limites, paginação e comportamento perante mudanças |
| Evolução | Identificar consumidores afetados e condições de compatibilidade |

Essas escolhas são uma proposta nossa, não regras universais da Microsoft ou das RFCs.

## Questionar e comparar

Uma chave de deduplicação só ajuda se houver um contrato: quem a pode usar, por quanto tempo, como tratar conteúdo diferente com a mesma chave e como coordenar pedidos simultâneos. Guardar uma chave depois do efeito pode deixar uma janela para duplicação. Este mecanismo requer investigação específica; não é implementado por nomear um cabeçalho.

| Estratégia proposta | Benefício | Limite |
| --- | --- | --- |
| Documentação descritiva | Explica intenção e exemplos | Pode divergir do comportamento |
| Esquema verificável e exemplos | Ajuda a verificar formatos | Não demonstra invariantes, autorização ou efeitos |
| Testes de contrato | Detetam incompatibilidades observadas | Só cobrem cenários e consumidores exercitados |

## Decidir, construir e testar

Antes de implementar, rever sucesso, erro, repetição, concorrência e evolução para cada operação. Escolher convenções consistentes e justificar exceções.

Exercícios propostos: alteração com versão antiga; repetição após timeout; nova enumeração num cliente antigo; paginação enquanto entram novos registos. **Nenhum teste foi executado.**

Pendências: esquema OpenAPI versionado, compatibilidade com consumidores, política de idempotência, paginação por cursor e operações assíncronas.
