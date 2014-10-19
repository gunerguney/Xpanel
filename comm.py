__author__ = 'guney'

import socket

def start_com1(drefList):

    BUFFER_SIZE = 1024
    UDP_IP = '192.168.1.101'
    UDP_PORT = 8894

    sock1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock1.connect((UDP_IP, UDP_PORT))

    counter = 0

    print "connected COMM1"

    while True:

        counter += 1
        sock1.send("Connected")
        data = sock1.recv(BUFFER_SIZE)
        recv_data = data.split('_')

        drefList[0].value = recv_data[5]
        drefList[1].value = recv_data[7]
        drefList[2].value = recv_data[8]
        drefList[3].value = recv_data[11]
        drefList[4].value = recv_data[9]
        drefList[5].value = recv_data[10]
        drefList[6].value = recv_data[12]
        drefList[7].value = recv_data[6]


def start_com2(MESSAGE):
    UDP_IP = '192.168.1.24'
    UDP_PORT = 49000

    #MESSAGE2 = "CMND0sim/electrical/battery_1_off" message asd
    MESSAGE = "CMND0" + MESSAGE
    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print str(bytes(MESSAGE)) + " sent"