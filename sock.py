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

try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip
