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

INTERFACE = "en1"
PASSWORD = "1234567890"

def GetXiaomiIP():
    print 'Holder...'

def Connect2Xiaomi(INTERFACE, SSID, PASSWORD):
    program = "networksetup"
    argList = ["-setairportnetwork", INTERFACE, SSID, PASSWORD]

    command = [program]
    command.extend(argList)

    output = str(subprocess.Popen(command, stdout = subprocess.PIPE).communicate()[0])

    print 'You are now connected to your Xiaomi Yi!'

def NetworkScan():
    var = None

    scanner = subprocess.Popen(['airport', '-s'], stdout = subprocess.PIPE,)
    grep = subprocess.Popen(['grep', '.. YDXJ'], stdin = scanner.stdout, stdout = subprocess.PIPE,)

    end_of_pipe = grep.stdout

    for line in end_of_pipe:
        var = line.strip()

    if var == None:
        print '\t I cannot find your Xiaomi Yi, is it turned on?'
        print '\t Please take a look and run the code again :-)'
        return var
    else:
        xiaomiSSID = var.split()
        return xiaomiSSID[0]

def main():
    # Scan the network with airport utility
    SSID = NetworkScan()
    #Connect to your Xiaomi Yi
    if SSID != None:
        connection = Connect2Xiaomi(INTERFACE, SSID, PASSWORD)
        # Get Xiaomi Yi's IP Address
        GetXiaomiIP()


if __name__ == '__main__':
    main()
