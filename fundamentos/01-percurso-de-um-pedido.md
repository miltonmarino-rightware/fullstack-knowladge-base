# FND-001 — do pedido web à alteração dos dados

**Estado:** síntese documental revista após relatório complementar; laboratórios pendentes.
**Data:** 2026-10-16.
**Âmbito:** modelo introdutório de uma aplicação web. Não cobre toda a computação nem define uma arquitetura de produção.
**Pré-requisitos:** reconhecer ficheiro, programa, navegador e endereço web.
**Fontes:** IDs e referências completas em [fontes.md](fontes.md).

## 1. Pergunta

Como ligar interface, comunicação, execução e armazenamento sem confundir as garantias de cada camada?

O objetivo de aprendizagem é conseguir desenhar o percurso de uma operação, indicar onde observar uma falha e explicar o que ainda não sabemos. O exemplo de criar uma inscrição é fictício e não foi implementado.

## 2. Navegador e comunicação

O navegador atua como cliente; o servidor recebe pedidos e devolve recursos. HTML, CSS, JavaScript e imagens podem ser obtidos em pedidos distintos. O domínio é parte do endereço; DNS participa na localização dos endereços usados na comunicação. Uma resposta permite ao navegador continuar a construir a página. Este é um resumo introdutório, não uma descrição completa de caches, resolução de nomes ou renderização. [fundamentos-F001]

A descrição “HTTP usa TCP” precisa de contexto: HTTP/3 usa QUIC sobre UDP. A RFC 9114 descreve estabelecimento e reutilização de ligações, incluindo verificação do certificado. Portanto, não devemos diagnosticar todo o tráfego web procurando apenas ligações TCP. [fundamentos-F005, §§3.1–3.3]

### 2.1. Três mecanismos distintos

DNS permite consultar registos associados a nomes; não é o encaminhamento dos pacotes. O TTL participa no controlo da permanência dos registos em cache. Não existe uma relação obrigatória de uma consulta DNS por pedido HTTP. Este resumo cobre o modelo base; extensões e políticas concretas dos resolvedores precisam de estudo próprio. [fundamentos-F008, §§2.4 e 3.6]

A cache HTTP guarda respostas reutilizáveis. Quando as condições do protocolo permitem, uma resposta fresca pode ser utilizada sem contactar a origem; a revalidação permite verificar uma resposta armazenada. Por isso, obter um recurso não comprova uma nova execução do backend. [fundamentos-F006, §§4–4.3]

A reutilização da ligação é outra questão: HTTP/1.1 tem persistência por omissão, sujeita às regras de delimitação das mensagens e fecho. Para reutilizar a ligação, o cliente precisa de consumir o corpo completo da resposta. [fundamentos-F007, §9.3]

## 3. Mensagem e efeito

O método HTTP expressa a intenção do pedido; o código da resposta comunica o resultado segundo as semânticas do protocolo. GET obtém uma representação; POST solicita processamento específico do recurso. Idempotência significa que repetir pedidos idênticos tem o mesmo efeito pretendido de um pedido, não que as respostas sejam sempre iguais. Repetir automaticamente um método não idempotente exige conhecimento adicional sobre a operação. [fundamentos-F002, §§9.1–9.3]

### 3.1. Ler o código exato e o contrato

200 indica sucesso segundo o método; 202 indica aceitação para processamento ainda não concluído. Uma resposta 2xx não é uma garantia universal de conclusão do trabalho de negócio. O contrato deve esclarecer o que já ocorreu e como acompanhar resultados posteriores. [fundamentos-F002, §§15.3.1 e 15.3.3]

## 4. Programa em execução

Um programa guardado é diferente do processo que o executa. O processo tem estado, incluindo memória, registos e recursos de entrada/saída. O sistema operativo gere execução e alternância entre processos. O modelo introdutório distingue estar em execução, pronto a executar e bloqueado à espera de um evento. Uma espera por entrada/saída ajuda a perceber por que um programa pode demorar sem estar continuamente a calcular. [fundamentos-F004, cap. 4]

Uma thread é um fluxo de execução dentro de um processo. Threads do mesmo processo partilham o espaço de endereçamento e possuem estado de execução próprio, incluindo registos e stack no modelo apresentado. [fundamentos-F009, cap. 26, introdução]

Um pedido é uma mensagem; uma thread é um mecanismo de execução. Não há correspondência obrigatória de um para um. A distribuição de pedidos por processos, threads ou outros mecanismos exige estudar o servidor e runtime concretos.

## 5. Unidade de alteração dos dados

No PostgreSQL, uma transação pode agrupar alterações para que sejam aplicadas como uma unidade. BEGIN e COMMIT delimitam um bloco explícito; ROLLBACK cancela alterações ainda não confirmadas. A biblioteca cliente também pode gerir esses comandos. [fundamentos-F003, §3.4]

Aprofundar isolamento, configuração de durabilidade e recuperação será necessário antes de estabelecer garantias de produção. Este tutorial é uma introdução, não uma validação desses requisitos.

### 5.1. Delimitar a garantia

Inferência de engenharia: uma alteração local transacional não demonstra a entrega da resposta HTTP nem a conclusão de um efeito externo. Por exemplo, um email enviado por outro serviço não fica automaticamente desfeito por um ROLLBACK local. A validação desta fronteira exige observar os dois sistemas. [fundamentos-F003; âmbito do tutorial]

Outbox, deduplicação, compensação e reconciliação são tópicos futuros. Não estabelecemos aqui um padrão aprovado nem uma promessa de exactly-once.

## 6. Modelo de raciocínio: inscrição

A tabela é uma proposta didática da RIGHTWARE. Serve para formular perguntas; não é um procedimento validado.

| Momento | Ação proposta | Evidência a procurar |
| --- | --- | --- |
| Interface | O utilizador preenche e envia uma inscrição fictícia | Pedido observado no navegador |
| Entrada da aplicação | O servidor interpreta e valida a operação | Registo do pedido e motivo de rejeição, quando exista |
| Regra | A aplicação decide se a inscrição pode ser criada | Regra explícita e caso de teste |
| Persistência | A aplicação solicita a gravação | Resultado da transação e consulta posterior |
| Resposta | O servidor comunica o resultado | Resposta recebida e identificador da operação |
| Apresentação | A interface mostra o estado | Correspondência entre informação apresentada e registo consultado |

Pergunta crítica: se a gravação ocorrer e a resposta se perder, o que sabe o cliente?

Inferência de engenharia a partir das fronteiras acima: a ausência de resposta não permite concluir, por si só, que nenhuma alteração ocorreu. É necessário investigar um mecanismo para consultar o resultado ou repetir com segurança. A política concreta de idempotência fica pendente de estudo e teste; não basta adicionar um cabeçalho arbitrário. [fundamentos-F002; fundamentos-F003]

## 7. Comparação a investigar

| Cenário | Pergunta que orienta a arquitetura |
| --- | --- |
| Página de apresentação com conteúdo fixo | Que requisito justificaria acrescentar armazenamento ou backend próprio? |
| Inscrições guardadas e consultadas por utilizadores | Onde vivem as regras, o controlo de acesso e o estado? |
| Inscrição com confirmação por serviço externo | Como detetar e recuperar uma divergência entre sistemas? |

Estas perguntas não elegem tecnologias. A decisão futura deverá explicitar requisitos, custos, riscos e evidências.

## 8. Exercício de observação proposto

**Estado: não executado.** Usar uma página própria de teste, com dados fictícios e autorização para observar os pedidos.

1. Registar navegador, versão, sistema operativo, URL e data.
2. Abrir as ferramentas de desenvolvimento e o separador de rede.
3. Recarregar a página; registar os pedidos efetivamente observados, métodos, códigos, tipos de conteúdo e protocolo.
4. Identificar qual resposta corresponde ao documento principal e quais aos recursos.
5. Repetir e comparar observações, registando configuração de cache e diferenças.
6. Explicar quais componentes do percurso não podem ser comprovados só com essa observação.

Resultado esperado: uma tabela de evidências e uma explicação das limitações. O exercício não demonstra a transação do servidor nem recuperação após falhas. Essa parte precisa de um laboratório separado e instrumentado.

## 9. Critérios de compreensão e pendências

Conseguir explicar a diferença entre mensagem, processo e transação; localizar uma afirmação na sua fonte; distinguir observação de hipótese; explicar por que falta de resposta deixa incerteza.

Ainda investigar:
- DNS, caches e ligações reutilizadas em detalhe.
- Threads, concorrência e modelos de execução.
- O que constitui uma confirmação durável na configuração escolhida.
- Isolamento, duplicação, idempotência e efeitos externos.
- Um laboratório que provoque perda de resposta após gravação.

O [relatório de integração](revisao-fnd-001.md) regista as decisões sobre o PDF recebido. O relatório externo não teve acesso ao texto original; o confronto com o estudo foi feito nesta revisão. Os [três laboratórios propostos](laboratorios-fnd-001.md) continuam por executar. Nenhuma conclusão aqui comprova domínio prático da equipa.
