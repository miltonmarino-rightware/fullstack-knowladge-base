-- L03: preparado para psql 18; ainda nao executado.
-- Executar numa sessao nova, base de testes e pasta vazia.
\set AUTOCOMMIT on
\set ON_ERROR_ROLLBACK off
\set ON_ERROR_STOP on
\pset pager off
SELECT version();
SHOW transaction_isolation;
CREATE TEMP TABLE rw_l03 (id integer PRIMARY KEY, nome text NOT NULL);

-- A: erro deliberado; apenas este comando pode prosseguir apos erro.
BEGIN;
INSERT INTO rw_l03 VALUES (1, 'a-reverter');
\set ON_ERROR_STOP off
INSERT INTO rw_l03 VALUES (2, NULL);
\set erro_a :SQLSTATE
\set ON_ERROR_STOP on
ROLLBACK;
SELECT :'erro_a' = '23502' AS caso_a_erro_esperado;
SELECT count(*) = 0 AS caso_a_sem_linhas FROM rw_l03;

-- B: confirmar e ler na mesma sessao.
BEGIN;
INSERT INTO rw_l03 VALUES (10, 'confirmado');
COMMIT;
SELECT count(*) = 1 AS caso_b_confirmado FROM rw_l03 WHERE id = 10;

-- C: gravacao LOCAL pelo cliente psql, fora da transacao do servidor.
BEGIN;
INSERT INTO rw_l03 VALUES (20, 'a-reverter-com-efeito-externo');
\o efeito-externo.txt
SELECT 'EFEITO_EXTERNO_L03' AS marcador;
\o
ROLLBACK;
SELECT count(*) = 0 AS caso_c_sem_linha FROM rw_l03 WHERE id = 20;
\echo Verificar manualmente efeito-externo.txt na pasta atual.

-- D: a sequencia e criada antes do bloco que sera revertido.
CREATE TEMP SEQUENCE rw_l03_seq START 1;
BEGIN;
SELECT nextval('rw_l03_seq') AS primeiro_valor;
ROLLBACK;
SELECT nextval('rw_l03_seq') = 2 AS caso_d_valor_nao_reutilizado;
-- Objetos temporarios desaparecem no fim da sessao.
