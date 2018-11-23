import socket
import binascii
import pdb
import matplotlib.pyplot as plt

HOST = '127.0.0.1'
PORT = 5029
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
		coded.append('0') # return to zero

	return coded

def createGraph(title, nums):
	plt.plot(nums)
	plt.title(title)
	plt.xlabel("Quantidade de bits")
	plt.show()

def menu():
	print("########################################")
	print("     1 - Para NRZ")
	print("     2 - Para RZ")
	print("     0 - Sair")
	print("########################################")
	op = raw_input("Selecione a opcao desejada: ")
	print('*Para sair use -1\n')
	
	if op == '0':
		print("Abortando programa...")
		exit(0)
	elif op == '1':
		print("--------------------")
		print("Opcao NRZ selecionada")
		print("--------------------")
	else:
		print("---------------------")
		print("Opcao RZ selecionada")
		print("---------------------")
		print("")
		op = 0
	return str(op)

def main():
	
	while True:
		op = menu()
		
		msg = raw_input("Digite a mensagem desejada: ")
		
		binary = ''.join(format(ord(x), 'b') for x in msg)
		print('Mensagem em binario: ', str(binary))
		
		vetBinary = list(binary)
		#print(vetBinary)

		coded = ''
		if op == '1':
			coded = NRZ(binary)  
		else:
			coded = RZ(binary)

		coded = ''.join(coded)
		vetCoded = list(coded)
		print('Mensagem codificada: ', coded)
		
		createGraph("Binario - cliente", vetBinary)
		createGraph("Binario codificado - cliente", vetCoded)
		#pdb.set_trace()
		str_coded = ''
		for x in coded: str_coded += x

		tcp.send(str_coded)

	tcp.close()

if __name__ == "__main__":
    main()