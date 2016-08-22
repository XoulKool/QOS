import socket                   # Import socket module
import time
import sys
import os

i=0

fp = open('bparlog1.txt', 'a')
fp1 = open('bparlog2.txt', 'a')
s = socket.socket()             # Create a socket object     # Get local machine name
s1 = socket.socket()
port = 60000                    # Reserve a port for your service.
s.bind(('10.100.0.6', port))
s.connect(('10.100.0.5', port))
s1.bind(('10.100.0.6', 60001))
s1.connect(('10.100.0.7', 60001))
s.send("Server 6:  Hello server 5!")
s1.send("Server 6:  Hello server 7!")
f = open('received_file', 'wb')
print 'file 1 opened'
f1 = open('received_file1', 'wb')
fp.write('Start:  ')
fp.write(str(int(time.time() * 1000)))
fp.write('\n')
fp1.write('Start:  ')
fp1.write(str(int(time.time() * 1000)))
fp1.write('\n')
print 'file 2 opened'
newpid = os.fork()
if newpid == 0:
    while True:
        data1 = s1.recv(4096)
        if not data1:
            break
        f1.write(data1)
    f1.close()
    print('Successfully got file 2')
    fp1.write('End:    ')
    fp1.write(str(int(time.time() * 1000)))
    fp1.write('\n')
    s1.close()
    print('Connection to server 7 closed')
    os._exit(0)
while True:
    data = s.recv(4096)
    if not data:
        break
        # write data to a file
    f.write(data)

f.close()
fp.write('End:    ')
fp.write(str(int(time.time() * 1000)))
fp.write('\n')
print('Successfully get the file 1')
s.close()
print('connection closed to server 5')
os.wait()

