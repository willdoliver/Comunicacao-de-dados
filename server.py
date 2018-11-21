import socket
import pdb

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

# Nao varia entre nrz e rz pois considera somente os sinais pares do vetor
def decodeMsg(coded):
    binary = ''

    for i, x in enumerate(coded):
        if i % 2 != 0:
            binary += x 
            if i < len(coded) - 1:
                binary += ' '
        else: continue
    
    return binary

def bin2Msg(binary):
    bin_chars = binary.split(', ', 7)
    msg = ''
    pdb.set_trace()
    for x in bin_chars: msg += unichr(int(x, 2)) 
    return msg

def main():
    print("Servidor Iniciado!")
    while True:
        con, cliente = tcp.accept()
        print('Concetado por', cliente)

        while True:
            coded = con.recv(1024)
            decoded = decodeMsg(coded)
            msg = bin2Msg(decoded)
            if not coded: break
            print(cliente, msg)

        print('Finalizando conexao do cliente', cliente)
        con.close()


if __name__ == "__main__":
    main()