import socket
import binascii

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print 'Para sair use CTRL+X\n'

msg = raw_input()

while msg <> '\x18':
	print(' '.join(format(ord(x), 'b') for x in msg))
	tcp.send (msg)
	msg = raw_input()
tcp.close()