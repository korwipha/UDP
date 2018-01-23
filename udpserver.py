import socket


host ="127.0.0.1"
port= 5001
server =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))

print("start .....")
while True :
    fac = 1
    data,addr =server.recvfrom(1024)
    n = (int)(data)
    if not data : break
    while n >=1:
        fac = fac*n
        n = n - 1
        
    data = (str)(fac)
    print("Message From Client : " +data)
    server.sendto(data,addr)
server.close()
