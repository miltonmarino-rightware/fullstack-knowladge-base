# Investigação com ChatGPT e Perplexity

**Atualização:** 2026-10-16.

## Divisão de trabalho proposta

| Frente | Trabalho | Resultado |
| --- | --- | --- |
| Pesquisa neste ambiente | Consultar fontes originais, estudar mecanismos e formular sínteses | Notas com fontes, limites e perguntas |
| Perplexity | Procurar referências complementares e contestar lacunas da síntese | Relatório com URLs, secções e divergências |
| Revisão conjunta | Abrir originais, comparar afirmações e corrigir conclusões | Conteúdo consolidado por pilar |
| Laboratórios | Verificar comportamentos específicos | Evidências com versão, ambiente e resultados |

Concordância entre duas IAs não equivale a confirmação independente: ambas podem repetir a mesma fonte ou o mesmo erro. A verificação deve regressar à origem e, quando necessário, à experiência reproduzível.

## Ciclo de trabalho

1. Delimitar uma pergunta e os resultados esperados.
2. Recolher fontes primárias e registar secções consultadas.
3. Produzir uma síntese inicial com afirmações rastreáveis.
4. Pedir ao segundo motor uma revisão crítica e procura de contraexemplos.
5. Verificar referências novas e contradições, sem copiar a resposta automaticamente.
6. Definir e executar laboratórios quando necessários.
7. Atualizar índice, fontes, conhecimento e pendências; guardar em Git.

## Investigação FND-001

- Tema: percurso de um pedido web, execução e confirmação de dados.
- [Primeiro estudo](fundamentos/01-percurso-de-um-pedido.md).
- [Registo de fontes](fundamentos/fontes.md).
- [Tarefa para Perplexity](fundamentos/pesquisa-perplexity-001.md).
- Estado: síntese revista; [L02 validado localmente](fundamentos/laboratorios/l02-timeout/README.md). L01, L03 e revisão externa linha a linha pendentes.
- Pesquisa neste ambiente: realizada em fontes indicadas no registo.
- Relatório complementar: recebido em PDF; o documento declara não ter acedido ao estudo. Contribuições verificadas e integradas conforme [registo de revisão](fundamentos/revisao-fnd-001.md).
- Próxima expansão: DNS e caches; memória e processos; depois concorrência e transações, mantendo as ligações aos pilares próprios.

O primeiro estudo liga camadas para orientar a aprendizagem. Não esgota o pilar Fundamentos nem determina a escolha de linguagens.

## Investigação DAD-001

- [Transações e limites](dados/01-transacoes-e-limites.md): síntese documental iniciada com quatro referências oficiais.
- [L03 PostgreSQL](fundamentos/laboratorios/l03-postgresql/README.md): roteiro preparado, execução bloqueada pela ausência de PostgreSQL/psql/Docker neste ambiente.
- Nenhuma execução PostgreSQL foi simulada ou substituída por resultados SQLite.

## Frente prioritária — formação abrangente

A pedido do utilizador, o foco passa a incluir sistematicamente cursos universitários, livros abertos, percursos gratuitos e aulas em vídeo. [Catálogo inicial](CATALOGO-FORMACAO.md): 15 entradas, páginas/programas consultados, sem alegação de cursos concluídos. [Pesquisa Perplexity](PESQUISA-PERPLEXITY-FORMACAO.md): complementar lacunas. A indisponibilidade de um ambiente de laboratório não bloqueia esta investigação.

## Formação — relatório Parte I recebido

Relatório revisto em 2026-10-16: [decisões, fontes reabertas e limites](REVISAO-FORMACAO-PARTE-I.md). Integrados percursos de Fundamentos e Dados, sem alterar estados de execução anteriores. Próxima pesquisa externa: [Parte II — Linguagens, Frontend, Backend e Arquitetura](PESQUISA-PERPLEXITY-PARTE-II.md). Perplexity entrega relatórios; a verificação e integração no GitHub são feitas neste fluxo.

## Formação — Parte II e NotebookLM

[Parte II revista](REVISAO-FORMACAO-PARTE-II.md) em 2026-10-16: curadoria parcial integrada em quatro pilares; Backend e Arquitetura ainda sem percurso principal completo. [NotebookLM](FLUXO-NOTEBOOKLM.md) passa a compor o método proposto para estudo de fontes selecionadas. Nenhuma sessão ou importação foi executada aqui. Resumos recebidos serão verificados antes da integração.

## Continuidade — domínio, APIs e arquitetura

Em 2026-10-16 foram produzidos [BCK-001](backend/01-dominio-e-invariantes.md), [BCK-002](backend/02-contratos-de-api.md) e [ARQ-001](arquitetura/01-modulos-dependencias-e-decisoes.md), com fontes primárias e exemplos próprios não executados. Foram selecionados livro aberto e referências complementares; não se declara domínio completo desses pilares.

Por preferência do utilizador, NotebookLM permanece opcional e adiado. A pesquisa direta não depende de importações manuais ou de novos relatórios externos.
