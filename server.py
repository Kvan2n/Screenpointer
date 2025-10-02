import socket
import atexit

def run():
    s = socket.socket()


    port = 45238

    s.bind(("0.0.0.0", port))

    s.listen(5)


    rconnection = False
    sconnection = False



    while True:
        rconnection = False
        sconnection = False


        connection, addr = s.accept()

        receive = connection.recv(1024).decode()
        print("received: "+receive)

        if "receiver" in receive:
            rconnection = connection
            raddr = addr
            print("receiver connected")
        elif "sender" in receive:
            saddr = addr
            sconnection = connection
            print("sender connected")

        else:
            print("setup receiving error")

        
        if rconnection and sconnection:
            break

    print("setup complete")
    def cleanup():
        rconnection.close()
        sconnection.close()
    atexit.register(cleanup)

    while True:

        receive = sconnection.recv(1024).decode()

        if len(receive)>0:
            rconnection.send(receive.encode())
            print("passing on "+receive)


