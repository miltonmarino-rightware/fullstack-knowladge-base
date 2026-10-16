# INF-001 — instalação, operação e recuperação

- **Estado:** síntese documental inicial e roteiro proposto; sem execução.
- **Revisão:** ChatGPT/Codex, 2026-10-16.
- **Pergunta:** que evidência permite afirmar que um serviço pode ser instalado, operado e recuperado?

## Investigar e compreender

Fontes em [fontes.md](fontes.md): infraestrutura-F001 a F004. A seleção distingue currículo de sistemas, referência de recuperação e experiência operacional.

A documentação PostgreSQL 18 separa SQL dump, cópia ao nível do sistema de ficheiros e arquivo contínuo. As técnicas têm pressupostos diferentes; não basta chamar “backup” a qualquer cópia. Foi consultada a introdução do capítulo 25, não executado um restauro. [F003]

O capítulo Emergency Response do Google SRE descreve preparação e treino e relata um teste que expôs dependências inesperadas. A lição aplicável ao estudo é verificar pressupostos e prever como interromper um exercício; não reproduzir falhas em produção por iniciativa própria. [F004]

## Modelar — ciclo operacional proposto

| Etapa | Informação necessária | Evidência proposta |
| --- | --- | --- |
| Instalar | Sistema operativo, runtime, versões, artefacto e dependências | Instalação reproduzida num ambiente limpo |
| Configurar | Parâmetros, permissões, portas e localização segura de segredos | Configuração efetiva conferida sem divulgar segredos |
| Iniciar | Processo/serviço, identidade de execução e dependências | Arranque e operação funcional mínima |
| Observar | Logs, métricas, sintomas e responsáveis | Diagnóstico de uma falha conhecida em ambiente de teste |
| Atualizar | Artefacto alvo, compatibilidade e migrações | Atualização ensaiada e critérios de interrupção |
| Recuperar | Cópias, chaves, configuração e procedimento | Restauro separado, validação funcional e tempos registados |

Tabela de autoria própria: critérios a adaptar ao sistema concreto, não certificação nem resultado observado.

## Questionar e comparar

Um processo ativo não demonstra que a operação do utilizador funciona. Um ficheiro de backup existente não demonstra que todas as dependências necessárias à recuperação estão disponíveis.

Reverter o binário e restaurar dados são ações diferentes. Se uma migração remove informação, o código antigo pode já não conseguir operar sobre o novo estado. A opção de reversão precisa de ser definida antes da atualização.

| Alternativa proposta | Benefício | Limite |
| --- | --- | --- |
| Configuração manual documentada | Boa para compreender passos iniciais | Facilita divergência entre ambientes |
| Configuração automatizada e versionada | Permite repetir e rever alterações | A automação também precisa de verificação |
| Recuperação apenas em instruções | Regista intenção | Não fornece tempo ou resultado observado |
| Ensaio isolado de recuperação | Produz evidência contextual | Não garante todos os cenários de desastre |

## Decidir, construir e testar

Para um futuro exercício, usar dados sintéticos num ambiente separado: identificar versão → produzir cópia pelo método escolhido → restaurar num destino vazio → verificar estrutura e operações → registar falhas, duração e limites.

Não incluir comandos genéricos destrutivos antes de fixar ferramenta, versão, origem e destino. **Nenhum ambiente foi instalado, atualizado ou restaurado nesta investigação.**

Pendências: serviços Linux/Windows, rede/TLS, CI/CD, gestão de segredos, monitorização, atualização de esquemas e recuperação pontual. [Percurso inicial](percurso-formacao.md).
