# FND-001 — laboratórios propostos

**Estado de todos os laboratórios:** não executados.
**Origem:** experiências sugeridas no PDF complementar, delimitadas na revisão da RIGHTWARE.
**Objetivo:** produzir evidências pequenas e reproduzíveis, sem construir um produto.

Antes de executar, registar sistema operativo, versões, configuração, data e comandos efetivos. Usar apenas dados fictícios e ambiente próprio. Os resultados abaixo são expectativas, não observações.

## L01 — separar cache HTTP e reutilização de ligação

Pré-requisitos: navegador com ferramentas de rede; servidor de teste próprio com um recurso de conteúdo fixo e política de cache conhecida.

1. Registar URL, cabeçalhos do recurso e configuração do servidor.
2. Capturar uma primeira carga sem resposta previamente armazenada.
3. Fazer uma segunda navegação normal, anotando se houve pedido, transferência ou revalidação; recarregamentos forçados podem alterar o comportamento.
4. Comparar cabeçalhos e indicadores de cache. Uma resposta servida em cache não prova novo contacto com a origem.
5. Separadamente, provocar dois pedidos de rede e observar identificadores de ligação, quando disponíveis, ou logs do servidor que distingam a ligação.
6. Se a ferramenta não permitir demonstrar reutilização, marcar esse resultado como inconclusivo.

Esperado: conseguir distinguir evidência de cache de evidência de ligação. Não presumir que a segunda carga será sempre mais rápida.
Limites: não demonstra consultas DNS, transações nem ausência de intermediários.

## L02 — timeout depois de uma gravação

Pré-requisitos: servidor HTTP local instrumentado, cliente com timeout configurável e armazenamento de teste consultável.

1. Preparar uma operação com identificador único que grave um registo e confirme a gravação antes de atrasar a resposta.
2. Usar atraso superior ao timeout configurado no cliente; registar ambos.
3. Enviar uma única operação e registar o resultado do cliente.
4. Consultar o armazenamento por um caminho independente e correlacionar o identificador.
5. Comparar a ordem dos eventos: recebimento, confirmação da escrita, timeout e tentativa de resposta.
6. Não repetir automaticamente a operação nesta experiência.

Esperado: observar uma escrita concluída apesar de o cliente não receber a resposta a tempo.
Limites: ilustra uma possibilidade; não prova que todos os timeouts tenham esta causa, nem valida deduplicação ou resistência a avarias.

## L03 — rollback local e efeito externo

Pré-requisitos: PostgreSQL 18 de teste, cliente SQL e terminal separado para criar um ficheiro fictício.

1. Criar e confirmar previamente uma tabela de laboratório com uma coluna obrigatória.
2. Iniciar uma transação, inserir um registo válido e provocar uma violação da restrição.
3. Executar ROLLBACK e consultar a tabela; registar ausência do registo.
4. Repetir com operações válidas e COMMIT; consultar de novo.
5. Numa nova transação, inserir outro registo; no terminal separado, escrever um ficheiro de teste.
6. Executar ROLLBACK e verificar separadamente a tabela e o ficheiro.

Esperado: a inserção revertida não permanece; o ficheiro escrito fora do PostgreSQL permanece.
Limites: não valida todos os níveis de isolamento, durabilidade em avaria, transações distribuídas ou configurações de outros motores.

## Modelo do relatório de execução

| Campo | Registo |
| --- | --- |
| Laboratório e data | Preencher após executar |
| Ambiente e versões | Preencher |
| Configuração e comandos | Preservar os efetivamente usados |
| Resultado esperado | Referenciar o cenário |
| Resultado observado | Descrever sem interpretar além da evidência |
| Evidências | Logs e saídas sem credenciais |
| Divergências e limites | Explicar |
| Estado final | Validado apenas no contexto / inconclusivo / falhou |

Não promover o FND-001 inteiro a validado com base num só laboratório.
