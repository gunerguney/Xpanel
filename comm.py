__author__ = 'guney'

import socket
from struct import*
import time
import xpanel
import plotting

data = []
start_time = 0

start_time = time.time()
record_data = False

def start_com1(drefList):

    BUFFER_SIZE = 1024
    UDP_IP = '192.168.1.21'
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
    UDP_IP = '192.168.1.21'
    UDP_PORT = 49000

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

    global elevator

    header = message[0:4]

    part1 = message[4:39]
    part2 = message[40:75]
    part3 = message[76:111]
    part4 = message[112:147]
    part5 = message[148:183]
    part6 = message[184:219]
    part7 = message[220:255]

    index1 = unpack('i', part1[1:5])
    index2 = unpack('i', part2[1:5])
    index3 = unpack('i', part3[1:5])
    index4 = unpack('i', part4[1:5])

    vind             = unpack('f',part1[5:9])
    verticalSpeed    = unpack('f',part2[13:17])
    pitch            = unpack('f',part4[5:9])
    altitude         = unpack('f',part6[25:29])
    elevator         = unpack('f',part7[5:9])


    elapsed_time = time.time() - start_time

    dat = {'time':elapsed_time, 'speed':vind[0], 'verticalSpeed':verticalSpeed[0],'pitch':pitch[0],'altitude':altitude[0]}

    if record_data==True:
        data.append(dat)


def start_test():
    global start_time
    global record_data
    start_time = time.time()
    record_data = True

def stop_test():
    global record_data
    global data

    record_data = False

    speed = []
    time = []
    verticalSpeed = []
    pitch = []
    altitude = []


    for i in range(0,len(data)):
        speed.append( data[i]['speed'])
        time.append( data[i]['time'])
        verticalSpeed.append(data[i]['verticalSpeed'])
        pitch.append(data[i]['pitch'])
        altitude.append(data[i]['altitude'])



    plotting.plot_chart(time,speed,"time-speed")
    plotting.plot_chart(time,verticalSpeed,"time-verticalSpeed")
    plotting.plot_chart(time,pitch,"time-pitch")
    plotting.plot_chart(time,altitude,"time-altitude")