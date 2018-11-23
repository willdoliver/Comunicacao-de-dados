import socket
import pdb
import binascii
import matplotlib.pyplot as plt

HOST = ''
PORT = 5029
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
    sliced = ''
    aux = 0
	
    binary = binary.replace(' ', '')
    for i in range(len(binary)):
        sliced += str(binary[i])
        aux+=1
		
        if (aux % 7 == 0):
            sliced += ','

    #print(sliced)
    bin_chars = sliced.split(',')
    #print(bin_chars)

    #pdb.set_trace()
    msg = ''
    for x in bin_chars: 
        try:
            msg += chr(int(x, 2))
        except:
            pass
    return msg

def createGraph(title, nums):
    plt.plot(nums)
    plt.title(title)
    plt.show()


def main():
    print("Servidor Iniciado!")
    while True:
        con, cliente = tcp.accept()
        print('Concetado por', cliente)

        while True:
            # Grafico do coded
            coded = con.recv(1024)
            print('Mensagem codificada: ',coded)
            vetCoded = list(coded)
            decoded = decodeMsg(coded)
            #print(decoded)
            # Grafico do binaryT
            binaryT = decoded.replace(' ', '')
            vetBinaryT = list(binaryT)
            print('Mensagem em binario: ', binaryT)
            # Printar MSG
            msg = bin2Msg(decoded)
            print('Texto da mensagem: ', msg)
            if not coded: break
            print(cliente, msg)

            createGraph('binario codificado - server', vetCoded)
            createGraph('binario - server', vetBinaryT)

        print('Finalizando conexao do cliente', cliente)
        con.close()


if __name__ == "__main__":
    main()