import socket
import binascii
import matplotlib.pyplot as plt

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5001            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use -1\n')

msg = input()

signal = []
while msg != '-1':
	binary = ''.join(format(ord(x), 'b') for x in msg)
	
	tmp = list(binary)
	coded = []
	for x in tmp:
		coded.append(x)
		coded.append(x)

	plt.plot(vet)
	plt.title("NRZ-RZ")
	plt.show()

	tcp.send(binary)
	msg = input()

tcp.close()
