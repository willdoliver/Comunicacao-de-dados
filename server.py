import socket
import pdb

HOST = ''              # Endereco IP do Servidor
PORT = 5012            # Porta que o Servidor esta
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

	print(sliced)
	bin_chars = sliced.split(',')
	print(bin_chars)

	# Transformar binario do bin_chars para letras

	#pdb.set_trace()
	msg = ''
	for x in bin_chars: 
		print(x)
		msg += chr(int(x)) 
	return msg

def main():
    print("Servidor Iniciado!")
    while True:
        con, cliente = tcp.accept()
        print('Concetado por', cliente)

        while True:
            coded = con.recv(1024)
            #print(coded)
            decoded = decodeMsg(coded)
            #print(decoded)
            msg = bin2Msg(decoded)
            if not coded: break
            print(cliente, msg)

        print('Finalizando conexao do cliente', cliente)
        con.close()


if __name__ == "__main__":
    main()