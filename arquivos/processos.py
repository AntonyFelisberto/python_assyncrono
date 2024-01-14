import multiprocessing

print(f"iniciando processo com nome: {multiprocessing.current_process().name}")

def faz_algo(valor):
    print(f"fazendo algo com o valor: {valor}")

def main():
    pc = multiprocessing.Process(target=faz_algo, args=("Passaro",),name="processamento total")
    print(f"iniciando processo com o nome {pc.name}")
    pc.start()
    pc.join()

if __name__ == "__main__":
    main()