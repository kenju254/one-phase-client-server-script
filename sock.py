import socket # for sockets 
import sys  # for exits 

try:
    #Creating an AF_INET , SOCK socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error Code:' + str(msg[0]) + 'Error Message' + msg[1]
    sys.exit();
    
print 'Sock Created' 

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip

#Connect to remote server
s.connect((remote_ip, port))

print 'Socket connected to ' + host + ' on ip ' + remote_ip

# Sending some data to a remote server
message = "GET / HTTP/1. 1\r\n\r\n"

try:
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print "Sending failed"
    sys.exit()

print 'Message sent successfully'
