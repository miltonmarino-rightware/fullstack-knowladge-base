# LNG-001 — Tipos, execução e fronteiras de confiança

- **Pilar:** Linguagens.
- **Estado:** síntese documental inicial; exemplo próprio não executado.
- **Autor/revisor:** assistente, com revisão das fontes primárias; revisão independente pendente.
- **Data:** 2026-10-16.
- **Contexto:** TypeScript Handbook contínuo; compilador e configuração ainda não fixados.

## 1. Pergunta e âmbito

O que uma declaração de tipo permite concluir sobre dados recebidos de uma API? Estudamos TypeScript como caso concreto, sem generalizar as suas garantias a todas as linguagens. Pré-requisitos: funções, objetos e JSON.

## 2. Investigar

[Fontes](fontes.md): linguagens-F003, The Basics, secções Static type-checking, Erased Types e strictNullChecks; linguagens-F004, Everyday Types, secção Type Assertions. As páginas explicam mecanismos; não fornecem evidência sobre o nosso exemplo.

## 3. Compreender

A análise estática procura incompatibilidades antes da execução, segundo a informação disponível ao compilador. As anotações TypeScript são removidas do JavaScript emitido. Uma asserção com `as` informa o verificador; não inspeciona nem transforma o valor recebido. Com `strictNullChecks`, valores potencialmente nulos exigem tratamento explícito dentro desse modelo estático. Isso não certifica dados externos nem regras de negócio. [linguagens-F003, F004]

## 4. Questionar

No nosso exemplo, uma API devolve um identificador. Precisamos de distinguir três perguntas: a propriedade existe e é texto? O texto respeita o formato acordado? A pessoa pode consultar o recurso? O exemplo abaixo responde apenas à primeira e exige texto não vazio.

## 5. Comparar

Comparação proposta para esta fronteira:

| Escolha | Benefício | Limite |
| --- | --- | --- |
| Asserção direta | Pouco código | Não verifica a resposta |
| Validador manual | Regras pequenas e explícitas | Exige manutenção quando o contrato muda |
| Validador por esquema | Pode centralizar contratos maiores | Biblioteca e geração exigem avaliação própria |

A terceira alternativa é uma linha de investigação; nenhuma biblioteca foi selecionada ou comparada experimentalmente.

## 6. Modelar

Proposta: entrada desconhecida → verificação estrutural → objeto interno → regras do caso de uso. Falha estrutural deve impedir o uso como objeto válido. Autorização continua a pertencer ao serviço que controla o recurso; ver [domínio e invariantes](../backend/01-dominio-e-invariantes.md).

## 7. Decidir

Para este exemplo didático, receber `unknown` e validar explicitamente. Rever a escolha se houver muitos contratos ou necessidade de interoperabilidade. Não estabelecer uma stack obrigatória.

## 8. Construir

Exemplo próprio, ainda não compilado nem executado:

```ts
type Equipamento = { id: string };

function lerEquipamento(valor: unknown): Equipamento {
  if (typeof valor !== "object" || valor === null) {
    throw new Error("Objeto esperado");
  }
  if (!("id" in valor) || typeof valor.id !== "string") {
    throw new Error("Identificador textual esperado");
  }
  const id = valor.id.trim();
  if (id.length === 0) {
    throw new Error("Identificador vazio");
  }
  return { id };
}
```

O retorno reconstrói apenas o campo necessário. Esta é uma decisão didática: não verifica existência na base de dados, propriedade do recurso ou unicidade.

## 9. Testar

Verificação pendente: fixar versão do compilador, ativar `strict` e registar diagnóstico e execução separadamente. Casos propostos: `null`, `{}`, `{id: 7}` e `{id: " "}` devem ser rejeitados; `{id: " eq-1 "}` deve produzir `{id: "eq-1"}`. Não há resultados observados nesta nota.

## 10. Consolidar e rever

Perguntas de compreensão: por que uma asserção não substitui este código? Que garantia ainda falta depois do retorno? Que alteração de contrato obrigaria a rever o validador?

Próximos estudos: narrowing, tipos estruturais, generics e comparação com o sistema de tipos de Java no percurso CS61B. Reabrir esta nota quando houver compilação reproduzível ou mudança do contrato.

[Índice](README.md) · [Pendências](perguntas.md)
