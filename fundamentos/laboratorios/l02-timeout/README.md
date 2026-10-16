# L02 — timeout depois de uma gravação

**Estado:** validado no contexto descrito abaixo, em 2026-10-16.
**Origem:** cenário L02 de [FND-001](../../laboratorios-fnd-001.md).
**Código:** [experimento.py](experimento.py).
**Evidência original:** [resultado.json](resultado.json).

## Pergunta e resultado

Pode o cliente receber timeout apesar de a gravação já ter sido confirmada pelo servidor? Sim, nesta execução local: o commit retornou, o cliente expirou sem resposta e uma consulta independente encontrou a linha. Este é um contraexemplo à regra “timeout implica que nada foi guardado”.

## Ambiente observado

- Linux 6.18.44.
- Python 3.12.14 e SQLite 3.53.1.
- HTTP/1.1 sobre loopback, sem proxy ou TLS.
- Biblioteca padrão; sem pacotes externos.
- Duas operações fictícias e uma base temporária eliminada no fim.
- Hash do script: `72bbab3f8e6788f2cc882d90e35b12feaab4fa077013b514db458b116c9cd1e1`.

SQLite foi escolhido apenas como armazenamento local do experimento. Esta escolha não altera a stack da RIGHTWARE nem substitui o laboratório PostgreSQL L03.

## Como reproduzir

A partir da raiz do repositório, com Python 3 disponível:

```bash
python3 fundamentos/laboratorios/l02-timeout/experimento.py
```

No Windows, se o Python estiver instalado através do launcher:

```powershell
py -3 fundamentos/laboratorios/l02-timeout/experimento.py
```

A execução nesta entrega foi feita em Linux; o comando Windows não foi testado. A saída é JSON; código de saída 0 significa que as verificações passaram. Um ambiente mais lento pode tornar a experiência inconclusiva ou fazê-la falhar; examinar os eventos antes de interpretar.

## Funcionamento do código

1. Criar uma tabela numa base SQLite temporária.
2. Iniciar um servidor em `127.0.0.1`, numa porta atribuída pelo sistema.
3. No POST, inserir a operação e esperar pelo retorno do commit.
4. Atrasar deliberadamente a resposta apenas no cenário lento.
5. Observar a resposta ou timeout no cliente, sem retry.
6. Abrir outra conexão à base e contar o registo pelo identificador.
7. Esperar pela tentativa de resposta, parar o servidor e eliminar a base temporária.

Os eventos usam relógio monotónico e são registados sob lock. O relatório guarda também data UTC e versões. O servidor é exclusivamente didático.

## Observações desta execução

| Cenário | Atraso após commit | Timeout do cliente | Resultado do cliente | Linhas encontradas |
| --- | --- | --- | --- | --- |
| Controlo | 0 s | 2 s | Resposta 201 | 1 |
| Resposta atrasada | 1 s | 0,2 s | Timeout | 1 |

Cronologia do cenário atrasado, relativa ao início desse cenário:

| Evento | Tempo observado |
| --- | --- |
| Pedido recebido | 1,249 ms |
| Commit retornou | 1,609 ms |
| Cliente recebeu timeout | 201,647 ms |
| Consulta independente encontrou a linha | 202,086 ms |
| Servidor tentou responder | 1001,777 ms |
| Escrita da resposta lançou BrokenPipeError | 1001,992 ms |

Os valores são observações de uma execução, não metas de desempenho. O erro de escrita não é requisito universal: buffers e plataformas podem produzir outro resultado. A verificação central é a ordem commit → timeout → tentativa de resposta, junto da linha encontrada.

## Verificações efetivas

- Controlo recebeu 201 com o identificador correto.
- Cada operação tinha exatamente uma linha na consulta independente.
- Cenário atrasado produziu timeout.
- Commit precedeu timeout; timeout precedeu a tentativa de resposta.
- Não houve erro interno do handler.
- Ambos os cenários passaram; código de saída 0.

## Conclusão e limites

A falta de resposta pode coexistir com uma alteração concluída. No cenário real, o cliente precisará de um contrato que permita determinar o resultado ou repetir com segurança; este laboratório não implementa esse contrato.

Não testámos: falha de energia, restauro, PostgreSQL, proxies, TLS, carga, duplicação, deduplicação, retries ou exactly-once. O retorno do commit e a leitura subsequente não constituem teste de durabilidade após avaria. O programa usa identificadores distintos, portanto a chave primária não foi testada como mecanismo de idempotência.

O resultado comprova uma propriedade neste contexto. Não demonstra domínio prático do utilizador nem valida todo o FND-001.
