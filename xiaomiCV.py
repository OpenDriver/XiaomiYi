'''
Only for Mac OS X
How-to get Xiaomi Yi Camera IP address to send commands to it through sockets
 airport -s | grep "XDJ"
 - parse output with python to save only SSID.
 networksetup -setairportnetwork $INTERFACE $SSID $PASSWORD
 Xiaomi Yi password: 1234567890
 ifconfig | grep "192.168.42"
 - parse output with python to only get Xiaomi IP address.
 - do magic!
'''

import subprocess
import os, re, sys, time, socket

INTERFACE = "en1"
PASSWORD = "1234567890"

XIAOMI_IP = "192.168.42.1"
XIAOMI_PORT = 7878

def SocketConnection(xiaomiIP):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((XIAOMI_IP, XIAOMI_PORT))

    server.send('{"msg_id":257,"token":0}')
    data = server.recv(512)

    if "rval"in data:
        token = re.findall('"param": (.+) }',data)[0]
    else:
        data = server.recv(512)
        if "rval"in data:
            token = re.findall('"param": (.+) }',data)[0]

    tosend = '{"msg_id":259,"token":%s,"param":"none_force"}' %token
    server.send(tosend)
    server.recv(512)

    print "Live webcam stream is now available."
    print 'Run VLC, select "Media"->"Open network stream" and open'
    print 'rtsp://%s/live' %xiaomiIP
    print
    print "Press CTRL+C to end this streamer"

    while 1:
	       time.sleep(1)

def Connect2Xiaomi(INTERFACE, SSID, PASSWORD):
    program = "networksetup"
    argList = ["-setairportnetwork", INTERFACE, SSID, PASSWORD]

    command = [program]
    command.extend(argList)

    output = str(subprocess.Popen(command, stdout = subprocess.PIPE).communicate()[0])
    if output != None:
        print '\tYou are now connected to your Xiaomi Yi!'
    else:
        print '\tSorry, there was a problem :-('

def NetworkScan():
    var = None

    scanner = subprocess.Popen(['airport', '-s'], stdout = subprocess.PIPE,)
    grep = subprocess.Popen(['grep', '.. YDXJ'], stdin = scanner.stdout, stdout = subprocess.PIPE,)

    end_of_pipe = grep.stdout

    for line in end_of_pipe:
        var = line.strip()

    if var == None:
        print '\tI cannot find your Xiaomi Yi, is it turned on?'
        print '\tPlease take a look and run the code again :-)'
        return var
    else:
        xiaomiSSID = var.split()
        return xiaomiSSID[0]

def main():
    # Scan the network with airport utility
    SSID = NetworkScan()
    #Connect to your Xiaomi Yi
    if SSID != None:
        Connect2Xiaomi(INTERFACE, SSID, PASSWORD)
        SocketConnection()


if __name__ == '__main__':
    main()
