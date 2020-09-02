import socket
import sys

def valida_puertos(ip, listapuestos):
    try:
        for puerto in listapuestos:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex( (ip, puerto) )
            if result == 0:
                print ("Puerto {}: \t Abierto".format(puerto))
            else :
                print ("Puerto {}: \t Cerado" . format(puerto))

            sock.close()

    except socket.error as e:
        print(str(e))
        print("Error de conexion")
        sys.exit()

if __name__ == "__main__":
    valida_puertos('192.168.1.1', [80, 8080,3306])