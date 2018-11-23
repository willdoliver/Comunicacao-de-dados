import socket
import binascii
import pdb
# import matplotlib.pyplot as plt

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5012            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

def NRZ(binary):
	coded = []

	for x in binary:
		coded.append(x)
		coded.append(x)

	return coded

def RZ(binary):
	coded = []

	for x in binary:
		coded.append(x)
		coded.append(0) # return to zero

	return coded

def main():
	nrz = raw_input("Digite 1 para nrz e 0 para rz: ")

	print('Para sair use -1\n')

	msg = raw_input()

	while msg != '\x18':
		binary = ''.join(format(ord(x), 'b') for x in msg)
		print(binary)

		coded = NRZ(binary) if nrz else RZ(binary)
		coded = ''.join(coded)
		print(coded)

		# plt.plot(vet)
		# plt.title("NRZ")
		# plt.show()

		str_coded = ''
		for x in coded: str_coded += x

		tcp.send(str_coded)
		msg = raw_input()

	tcp.close()

if __name__ == "__main__":
    main()