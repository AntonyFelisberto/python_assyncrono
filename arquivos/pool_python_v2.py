import multiprocessing

def calcular(dado):
    return dado ** 2

def imprimir_processo():
    print(f"iniciando processo com nome: {multiprocessing.current_process().name}")

def main():
    tamanho_pool = multiprocessing.cpu_count() * 3
    print(f"tamanho pool {tamanho_pool}")
    pool = multiprocessing.Pool(processes=tamanho_pool,initializer=imprimir_processo)
    entradas = list(range(7))
    saidas = pool.map(calcular,entradas)
    print(f"saidas {saidas}")
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()