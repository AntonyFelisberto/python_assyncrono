#pip install snakeviz
import datetime
import math
import cProfile
import pstats
import io
from pstats import SortKey

import threading
import multiprocessing

def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Realizando processamento matematico com {qtd_cores} cores")

    inicio = datetime.datetime.now()

    threads = []
    for n in range(1,qtd_cores+ 1):
        ini = 50_000_000 * (n-1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f"Core {n} processando {ini} até {fim}")
        threads.append(
            threading.Thread(
                target=computar,
                kwargs={"inicio":ini, "fim":fim},
                daemon=True
            )
        )

    [th.start() for th in threads]
    [th.join() for th in threads]

    tempo = datetime.datetime.now() - inicio
    print(f"terminou em {tempo.total_seconds():.2f} segundos")

def computar(fim,inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    profiler.dump_stats("python_padrao1.stats")
    sec = io.StringIO()
    sortBy = SortKey.TIME
    ps = pstats.Stats(profiler,stream=sec).sort_stats(sortBy)
    ps.print_stats()
    print(sec.getvalue())

#snakeviz python_padrao.stats
#snakeviz python_padrao.profile
#python -m cProfile -o python_padra.profile python_padrao.py