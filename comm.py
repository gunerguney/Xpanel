__author__ = 'guney'

import socket
from struct import*

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

        drefList[0].value = recv_data[5]    #5 is battery on
        drefList[1].value = recv_data[7]    #7 is beacon lighs on
        drefList[2].value = recv_data[8]
        drefList[3].value = recv_data[11]
        drefList[4].value = recv_data[9]
        drefList[5].value = recv_data[10]
        drefList[6].value = recv_data[12]
        drefList[7].value = recv_data[6]


def start_com2(MESSAGE):
    UDP_IP = '192.168.1.24'
    UDP_PORT = 49004

    MESSAGE = "CMND0" + MESSAGE
    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print str(bytes(MESSAGE)) + " sent"


def start_com3():
    UDP_IP = '127.0.0.1'
    UDP_PORT = 49003
    BUFFER_SIZE = 1024

    sock3 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock3.bind((UDP_IP, UDP_PORT))


    while True:

        data = sock3.recv(BUFFER_SIZE)
        parseUDPData(data)

def parseUDPData(message):

    header = message[0:4]

    part1 = message[4:39]
    part2 = message[40:75]
    part3 = message[76:111]
    part4 = message[112:147]

    index1 = unpack('i', part1[1:5])
    index2 = unpack('i', part2[1:5])
    index3 = unpack('i', part3[1:5])
    index4 = unpack('i', part4[1:5])

    vind    = unpack('f',part1[5:9])

    gear    = unpack('f',part2[5:9])
    wbreak  = unpack('f',part2[9:13])

    pitch   = unpack('f', part4[5:9])

    print pitch[0]

start_com3()