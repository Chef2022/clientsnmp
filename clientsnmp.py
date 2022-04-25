import socket
host, port = ('127.0.0.1', 5556)
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
   client.connect((host, port))
   print("client connecté")
   a=0
   while a<5 :

       data1= input('tapez votre requête:')
       data1= data1.encode("utf8")
       client.sendall(data1)
       a=a+1

except:
    print("connexion au serveur échouée")

finally:
    client.close()
