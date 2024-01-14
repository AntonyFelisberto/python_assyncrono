import threading
import time

def main():
    threads = [
        threading.Thread(target=contar,args=("elefante",10)),
        threading.Thread(target=contar,args=("buraco",8)),
        threading.Thread(target=contar,args=("moeda",23)),
        threading.Thread(target=contar,args=("pato",12))
    ]
    [th.start() for th in threads] #adicionando thread para executar

    print("executando outras coisas enquanto thread esta rodando")
    print("executando novas coisas " * 2)

    [th.join() for th in threads] #aguardar thread terminar
    print("pronto")

def contar(o_que,numero):
    for n in range(numero+1):
        print(f"{n} {o_que}(s)")
        time.sleep(1)

if __name__ == "__main__":
    main()