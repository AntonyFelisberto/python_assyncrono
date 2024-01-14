import threading
import time

def main():
    th = threading.Thread(target=contar,args=("elefante",10))
    th.start() #adicionando thread para executar

    print("executando outras coisas enquanto thread esta rodando")
    print("executando novas coisas " * 2)

    th.join() #aguardar thread terminar
    print("pronto")

def contar(o_que,numero):
    for n in range(numero+1):
        print(f"{n} {o_que}(s)")
        time.sleep(1)

if __name__ == "__main__":
    main()