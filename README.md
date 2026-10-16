# RIGHTWARE — Base de conhecimento full stack

Base de investigação, estudo e consulta para fundamentar as decisões de engenharia da RIGHTWARE.

**Método:** investigar → compreender → questionar → comparar → modelar → decidir → construir → testar.

## Estado inicial

Estrutura criada em 2026-10-16. A investigação começou em Fundamentos, com uma síntese documental inicial e fontes consultadas. O pilar Dados também tem uma síntese documental sobre transações, com execução PostgreSQL pendente. Backend e Arquitetura têm agora sínteses iniciais sobre domínio, contratos e modularidade. Os restantes tópicos continuam como mapa ou curadoria; não representam conhecimento validado. O foco atual é capacitação e construção da base de conhecimento. Projetos antigos são contexto histórico e não delimitam o âmbito.

## Progresso

[Estimativa e critérios da V1](PROGRESSO.md): cerca de 15%, avaliação provisória de planeamento, não medição de domínio técnico.

## Formação e materiais

- [Catálogo de universidades, cursos, livros e vídeos](CATALOGO-FORMACAO.md)
- [Revisão e integração do relatório — Parte I](REVISAO-FORMACAO-PARTE-I.md)
- [Revisão da Parte II e correções](REVISAO-FORMACAO-PARTE-II.md)
- [Estudar aulas com NotebookLM — fluxo e prompt](FLUXO-NOTEBOOKLM.md)
- [Prompt autónomo para Perplexity — Parte II](PESQUISA-PERPLEXITY-PARTE-II.md)
- [Pesquisa complementar para Perplexity](PESQUISA-PERPLEXITY-FORMACAO.md)

Prioridade atual: ampliar e avaliar materiais de formação por pilar, selecionar unidades e produzir conhecimento aprofundado. Os laboratórios existentes continuam como apoio à verificação.

## Pilares

| Pasta | Conteúdo |
| --- | --- |
| [Fundamentos](fundamentos/README.md) | Computação, lógica, estruturas de dados, sistemas operativos e redes. |
| [Linguagens](linguagens/README.md) | Funcionamento, paradigmas, execução, ferramentas e adequação a diferentes problemas. |
| [Frontend](frontend/README.md) | HTML, CSS, JavaScript, TypeScript, navegador, frameworks, acessibilidade, design e motion. |
| [Backend](backend/README.md) | Regras de negócio, APIs, autenticação, autorização, concorrência e processamento assíncrono. |
| [Dados](dados/README.md) | Modelação, SQL, diferentes tipos de bases de dados, transações, desempenho e recuperação. |
| [Arquitetura](arquitetura/README.md) | Componentes, limites, dependências, estilos arquiteturais, integração e decisões documentadas. |
| [Segurança](seguranca/README.md) | Ameaças, desenvolvimento seguro, proteção de infraestrutura e verificação de controlos. |
| [Qualidade](qualidade/README.md) | Testes, depuração, revisão de código e validação de requisitos. |
| [Infraestrutura e produção](infraestrutura-e-producao/README.md) | Instalação local, servidores, cloud, CI/CD, monitorização, atualizações e recuperação. |
| [Entrega profissional](entrega-profissional/README.md) | Estruturas de projeto, documentação, procedimentos operacionais e handoff. |

## Como utilizar

1. Ler o índice do pilar e escolher uma pergunta em `perguntas.md`.
2. Registar as fontes consultadas em `fontes.md`.
3. Documentar a investigação com o [modelo comum](MODELO-DE-INVESTIGACAO.md).
4. Consolidar explicações no documento principal do pilar, ligando cada afirmação relevante às fontes.
5. Registar comparações, limitações e resultados de validação.
6. Atualizar o estado e guardar a alteração num commit descritivo.

Cada pasta contém `README.md` (índice), `conhecimento.md` (documento principal), `fontes.md` (referências) e `perguntas.md` (investigação pendente). Quando o conteúdo crescer, separar assuntos em documentos temáticos e ligá-los a partir do índice. Criar subpastas para notas, comparações, laboratórios e procedimentos apenas quando houver conteúdo.

## Investigação em curso

- [SEG-001 — ameaças e evidências](seguranca/01-ameacas-controlos-e-evidencias.md)
- [QLD-001 — testes e propriedades](qualidade/01-testes-propriedades-e-limites.md)

- [BCK-001 — domínio e invariantes](backend/01-dominio-e-invariantes.md)
- [BCK-002 — contratos de APIs](backend/02-contratos-de-api.md)
- [ARQ-001 — módulos e decisões](arquitetura/01-modulos-dependencias-e-decisoes.md)

- [FND-001 — do pedido web à alteração dos dados](fundamentos/01-percurso-de-um-pedido.md)
- [Trabalho com ChatGPT e Perplexity](INVESTIGACAO.md)
- [Tarefa de pesquisa para o Perplexity](fundamentos/pesquisa-perplexity-001.md)
- [Revisão do relatório complementar](fundamentos/revisao-fnd-001.md)
- [Orientações para agentes](AGENTS.md)

- [DAD-001 — transações e limites](dados/01-transacoes-e-limites.md)

## Orientações comuns

- [Contexto e método da RIGHTWARE](CONTEXTO-RIGHTWARE.md)
- [Modelo de investigação](MODELO-DE-INVESTIGACAO.md)

Os nomes das pastas usam minúsculas, hífen e caracteres sem acentos para facilitar caminhos e ferramentas. Os documentos são escritos em português.

## Continuidade com assistentes

Este repositório é uma referência explícita para pessoas e assistentes com acesso. Não treina automaticamente uma conta de IA nem garante memória entre conversas. Em cada novo trabalho, indicar o repositório e pedir a leitura do contexto e dos pilares relevantes.
