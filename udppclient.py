import socket


host ="127.0.0.1"
port= 5001
se= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data =raw_input("Number for fac : ")

while data!='' :
    print "UDP target IP:",host
    print "UDP target port:",port
    print "Number:",data
    se.sendto(data,(host,port))
    data,addr=server.recvfrom(1024)
    
    print("fac is : " +data)
    data = raw_input("Number for fac : ")
se.close()

