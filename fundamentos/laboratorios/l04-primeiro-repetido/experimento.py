"""Exercício próprio FND-002; executar com Python 3.10+ sem dependências."""
import hashlib
import itertools
import json
import platform
from pathlib import Path


def primeiro_repetido(codigos):
    """Pré-condição: sequência finita de inteiros; None indica ausência."""
    vistos = set()
    for codigo in codigos:
        if codigo in vistos:
            return codigo
        vistos.add(codigo)
    return None


def referencia(codigos):
    # Oráculo por pares de índices, sem conjunto ou hashing.
    for segundo in range(len(codigos)):
        for primeiro in range(segundo):
            if codigos[primeiro] == codigos[segundo]:
                return codigos[segundo]
    return None


def exigir(condicao, contexto):
    if not condicao:
        raise AssertionError(contexto)


def main():
    exemplos = [([], None), ([0], None), ([0, 0], 0),
                ([8, 3, 8, 3], 8), ([9, 2, 2, 9], 2),
                ([-1, 0, -1], -1), ([1, 2, 3], None)]
    registos = []
    for entrada, esperado in exemplos:
        observado = primeiro_repetido(entrada)
        exigir(observado == esperado, (entrada, esperado, observado))
        registos.append(dict(entrada=entrada, esperado=esperado, observado=observado))
    dominio = [-2, -1, 0, 1, 2]
    total = 0
    for tamanho in range(7):
        for entrada in itertools.product(dominio, repeat=tamanho):
            observado = primeiro_repetido(entrada)
            exigir(observado == referencia(entrada), entrada)
            if observado is not None:
                segunda_posicao = [i for i, x in enumerate(entrada)
                                   if x == observado][1]
                prefixo = entrada[:segunda_posicao]
                exigir(len(prefixo) == len(set(prefixo)), entrada)
            total += 1
    resultado = {
        'estudo': 'FND-002',
        'python': platform.python_version(),
        'implementacao': platform.python_implementation(),
        'sistema': platform.system(),
        'codigo_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'exemplos': registos,
        'dominio_exaustivo': dominio,
        'comprimentos': [0, 6],
        'casos_exaustivos': total,
        'falhas': 0,
        'limite': 'Verificacao funcional finita; nao e benchmark ou prova universal.'
    }
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
