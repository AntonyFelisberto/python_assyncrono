import multiprocessing
import time

def func1(val,stat):
    if stat:
        res = val + 10
        stat = False
    else:
        res = val + 20
        val = 200
        stat = True

    print(f"o result da func1 é {res}")
    time.sleep(0.001)

def func2(val,stat):
    if stat:
        res = val + 30
        stat = False
    else:
        res = val + 40
        val = 400
        stat = True

    print(f"o result da func2 é {res}")
    time.sleep(0.001)

def main():
    valor = 100
    status = False

    p1 = multiprocessing.Process(target=func1, args=(valor,status))
    p2 = multiprocessing.Process(target=func2, args=(valor,status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()