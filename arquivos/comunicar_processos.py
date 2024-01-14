import multiprocessing

def ping(conn):
    conn.send("pings")

def pong(conn):
    msg = conn.recv()
    print(f"{msg} item")

def main():
    #PIPE DIFERENTE DE QUEUE NAO DA PRA USAR LOCK
    conn1,conn2 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=ping,args=(conn1,))
    p2 = multiprocessing.Process(target=pong,args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()