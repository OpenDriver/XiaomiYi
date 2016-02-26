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

def main():
    print("Hello world!")

if __name__ == '__main__':
    main()
