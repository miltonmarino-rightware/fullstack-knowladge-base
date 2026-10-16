# L03 — rollback, commit e efeitos fora da garantia

**Estado:** preparado; não executado.
**Bloqueio observado em 2026-10-16:** psql, postgres, initdb e Docker não encontrados no ambiente de execução. Nenhum servidor foi instalado ou contactado.
**Alvo:** PostgreSQL 18 e psql 18, numa base de teste com permissão para objetos temporários.
**Ligação teórica:** [DAD-001](../../../dados/01-transacoes-e-limites.md).
**Roteiro:** [experimento.sql](experimento.sql).

## Preparação e execução

Criar uma pasta local vazia para esta execução e copiar para lá o roteiro. A ligação deve apontar para uma base própria de testes; configurar autenticação fora do ficheiro SQL.

```bash
psql -X -d rightware_lab -f experimento.sql > resultado.txt 2>&1
```

O nome rightware_lab é um exemplo: a base deve existir. Não colocar passwords no comando nem guardar credenciais no Git. Usar uma sessão nova por execução.

O roteiro cria objetos temporários e um ficheiro local chamado efeito-externo.txt na pasta atual. Esse nome será sobrescrito; por isso usar uma pasta vazia. A tabela temporária serve para observar COMMIT na mesma sessão; desaparece ao sair e não testa persistência entre reinícios.

## Resultados esperados, ainda não observados

| Caso | Expectativa |
| --- | --- |
| A — inserção e erro NOT NULL | Erro intencional; após ROLLBACK, zero linhas |
| B — inserção e COMMIT | Uma linha visível na mesma sessão |
| C — escrita pelo cliente e ROLLBACK | Registo do caso C ausente; ficheiro local existente |
| D — nextval e ROLLBACK | Primeiro valor 1; chamada posterior devolve 2 |

Os SELECT com nomes iniciados por caso_ deverão produzir verdadeiro. O caso A inclui um erro propositado; outros erros não devem ser ignorados. O código de saída sozinho não basta: o roteiro permite prosseguir especificamente no trecho do erro esperado. Conferir a mensagem e todos os resultados.

Após a execução, abrir efeito-externo.txt e verificar o marcador EFEITO_EXTERNO_L03. O ficheiro resulta de saída do cliente psql; não é uma escrita transacional do servidor.

## Evidência a guardar

- Versões de psql e servidor, data e sistema operativo.
- resultado.txt e conteúdo do ficheiro externo, sem dados de conexão privados.
- Resultados reais de cada caso e divergências.
- Hash ou commit do roteiro utilizado.
- Estado: passou no contexto, falhou ou inconclusivo.

Não criar resultado “observado” a partir desta tabela de expectativas.

## Limites

Uma sessão, objetos temporários e dados fictícios. Não testa concorrência, todos os níveis de isolamento, falhas de energia, backup, restauro, desempenho, serviços externos reais ou exatamente uma execução. A experiência de sequência é um caso separado do ficheiro externo.

A configuração do cliente é explícita: AUTOCOMMIT on, ON_ERROR_ROLLBACK off e controlo localizado de ON_ERROR_STOP. Consultar dados-F003 no [registo de fontes](../../../dados/fontes.md).
