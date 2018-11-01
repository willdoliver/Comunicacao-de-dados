import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5050            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        coded = con.recv(1024)
        msg = ''
        for x in coded.split(' '):
            msg += str(unichr(int(x, 2)))
        if not coded: break
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()
