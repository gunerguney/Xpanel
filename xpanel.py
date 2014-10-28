__author__ = 'guney'

from Tkinter import*
import threading
from onChange import*
import comm

drefList = []

def startThread():
    t = threading.Thread(target= comm.start_com1,args=[drefList])
    t.start()

def startThread2(cmd):
    t1 = threading.Thread(target= comm.start_com2,args=[cmd])
    t1.start()


batLed = Label()
bcnLed = Label()
landLed = Label()
taxiLed = Label()
navLed = Label()
strobeLed = Label()
pitotHeatLed = Label()
avionicsMasterLed = Label()


class XPanel(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        menu = Menu(self)
        self.config(menu=menu)

        variable = StringVar()

        global drefList
        global batLed,bcnLed,landLed,taxiLed,navLed,strobeLed,pitotHeatLed,avionicsMasterLed

        def callback():
            print "called the callback"

        def new_file():
            print "new file selected"

        def open_file():
            print "open file selected"

        #battery toggle callback
        def battery_toggle_callback(value):
            if value == 0:
                print "battery off"
                batLed.configure(fg="orange")

            elif value == 1:
                print "battery on"
                batLed.configure(fg="green")

        #beacon toggle callback
        def bcn_toggle_callback(value):
            if value == 0:
                print "beacon off"
                bcnLed.configure(fg="orange")

            elif value == 1:
                print "beacon on"
                bcnLed.configure(fg="green")

        #landing lights toggle callback
        def landing_toggle_callback(value):
            if value == 0:
                print "landing lights off"
                landLed.configure(fg="orange")

            elif value == 1:
                print "landing lights on"
                landLed.configure(fg="green")

        #taxi light toggle callback
        def taxi_toggle_callback(value):
            if value == 0:
                print "taxi lights off"
                taxiLed.configure(fg="orange")

            elif value == 1:
                print "taxi lights on"
                taxiLed.configure(fg="green")

        #nav light toggle callback
        def nav_toggle_callback(value):
            if value == 0:
                print "nav lights off"
                navLed.configure(fg="orange")

            elif value == 1:
                print "nav lights on"
                navLed.configure(fg="green")

        #strobe toggle callback
        def strobe_toggle_callback(value):
            if value == 0:
                print "strobe lights off"
                strobeLed.configure(fg="orange")

            elif value == 1:
                print "strobe lights on"
                strobeLed.configure(fg="green")

        #pitot heat toggle callback
        def pitot_heat_toggle_callback(value):
            if value == 0:
                print "pitot heat off"
                pitotHeatLed.configure(fg="orange")

            elif value == 1:
                print "pitot heat on"
                pitotHeatLed.configure(fg="green")

        #avionics power toggle callback
        def avionics_toggle_callback(value):
            if value == 0:
                print "avionics off"
                avionicsMasterLed.configure(fg="orange")

            elif value == 1:
                print "avionics on"
                avionicsMasterLed.configure(fg="green")

        drefList.append(OnChangeClass(battery_toggle_callback))
        drefList.append(OnChangeClass(bcn_toggle_callback))
        drefList.append(OnChangeClass(landing_toggle_callback))
        drefList.append(OnChangeClass(taxi_toggle_callback))
        drefList.append(OnChangeClass(nav_toggle_callback))
        drefList.append(OnChangeClass(strobe_toggle_callback))
        drefList.append(OnChangeClass(pitot_heat_toggle_callback))
        drefList.append(OnChangeClass(avionics_toggle_callback))

        #command callbacks
        #battery on command callback
        def battery_on_callback():
            cmd = "sim/electrical/battery_1_on"
            startThread2(cmd)

        def battery_off_callback():
            cmd = "sim/electrical/battery_1_off"
            startThread2(cmd)

        #beacon lights on command callback
        def bcn_on_callback():
            cmd = "sim/lights/beacon_lights_on"
            startThread2(cmd)

        def bcn_off_callback():
            cmd = "sim/lights/beacon_lights_off"
            startThread2(cmd)

        #landing lights on command callback
        def land_on_callback():
            cmd = "sim/lights/landing_lights_on"
            startThread2(cmd)

        def land_off_callback():
            cmd = "sim/lights/landing_lights_off"
            startThread2(cmd)

        #taxi lights on command callback
        def taxi_on_callback():
            cmd = "sim/lights/taxi_lights_on"
            startThread2(cmd)

        def taxi_off_callback():
            cmd = "sim/lights/taxi_lights_off"
            startThread2(cmd)

        #nav lights on command callback
        def nav_on_callback():
            cmd = "sim/lights/nav_lights_on"
            startThread2(cmd)

        def nav_off_callback():
            cmd = "sim/lights/nav_lights_off"
            startThread2(cmd)

        #strobe lights on command callback
        def strobe_on_callback():
            cmd = "sim/lights/strobe_lights_on"
            startThread2(cmd)

        def strobe_off_callback():
            cmd = "sim/lights/strobe_lights_off"
            startThread2(cmd)

        #pitot heat on command callback
        def pitot_heat_on_callback():
            cmd = "sim/ice/pitot_heat_on"
            startThread2(cmd)

        def pitot_heat_off_callback():
            cmd = "sim/ice/pitot_heat_off"
            startThread2(cmd)

        #avionics master on command callback
        def avionics_master_on_callback():
            cmd = "sim/systems/avionics_on"
            startThread2(cmd)

        def avionics_master_off_callback():
            cmd = "sim/systems/avionics_off"
            startThread2(cmd)


        #menu components

        filemenu = Menu(menu)
        menu.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label="New",command=new_file)
        filemenu.add_command(label="Open...",command=open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=callback)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help",menu=helpmenu)
        helpmenu.add_command(label="About...",command=callback)

        #menu components

        #begin - buttons

        batOnBtn = Button(self, text="Battery On", width=10, command=battery_on_callback)    #battery switch buttons
        batOnBtn.grid(row=1,column=1)

        batOffBtn = Button(self, text="Battery Off", width=10, command=battery_off_callback)
        batOffBtn.grid(row=1,column=2)

        #-------lights----
        bcnOnBtn = Button(self, text="BCN On", width=10, command=bcn_on_callback )    #beacon lights buttons
        bcnOnBtn.grid(row=2,column=1)

        bcnOffBtn = Button(self, text="BCN Off", width=10, command=bcn_off_callback)
        bcnOffBtn.grid(row=2, column=2)

        landOnBtn = Button(self, text="LAND On", width=10, command=land_on_callback)   #landing lights buttons
        landOnBtn.grid(row=3, column=1)

        landOffBtn = Button(self, text="LAND Off", width=10, command=land_off_callback)
        landOffBtn.grid(row=3, column=2)

        taxiOnBtn = Button(self, text="TAXI On", width=10, command=taxi_on_callback)   #taxi lights buttons
        taxiOnBtn.grid(row=4, column=1)

        taxiOffBtn = Button(self, text="TAXI Off", width=10, command=taxi_off_callback)
        taxiOffBtn.grid(row=4, column=2)

        navOnBtn = Button(self, text="NAV On", width=10,  command=nav_on_callback)   #nav lights buttons
        navOnBtn.grid(row=5, column=1)

        navOffBtn = Button(self, text="NAV Off", width=10, command= nav_off_callback)
        navOffBtn.grid(row=5, column=2)

        strobeOnBtn = Button(self, text="STROBE On", width=10,  command=strobe_on_callback)   #strobe lights buttons
        strobeOnBtn.grid(row=6, column=1)

        strobeOffBtn = Button(self, text="STROBE Off", width=10, command=strobe_off_callback)
        strobeOffBtn.grid(row=6, column=2)

        pitotHeatOnBtn = Button(self, text="PITOT HEAT On", width=10,  command=pitot_heat_on_callback)   #pitot heat buttons
        pitotHeatOnBtn.grid(row=7, column=1)

        pitotHeatOffBtn = Button(self, text="PITOT HEAT Off", width=10, command=pitot_heat_off_callback)
        pitotHeatOffBtn.grid(row=7, column=2)

        avionicsMasterOnBtn = Button(self, text="AVIONICS\n MASTER On", width=10, command=avionics_master_on_callback)   #avionics master buttons
        avionicsMasterOnBtn.grid(row=8, column=1)

        avionicsMasterOffBtn = Button(self, text="AVIONICS\n MASTER Off", width=10, command=avionics_master_off_callback)
        avionicsMasterOffBtn.grid(row=8, column=2)

        #end - buttons

        #--------------------begin - leds

        #battery switch led
        batLed = Label(self, text="BATTERY", fg="orange", bg="black", font="Verdana 15 bold" ,width=10,height=1)
        batLed.grid(row=1,column=3)

        #beacon light led
        bcnLed = Label(self, text="BEACON" , fg="orange", bg="black", font="Verdana 15 bold", width=10)
        bcnLed.grid(row=2,column=3)

        #landing light led
        landLed = Label(self, text="LAND" , fg="orange", bg="black", font="Verdana 15 bold", width=10)
        landLed.grid(row=3,column=3)

        #taxi light led
        taxiLed = Label(self, text="TAXI" , fg="orange", bg="black", font="Verdana 15 bold", width=10)
        taxiLed.grid(row=4,column=3)

        #nav light led
        navLed = Label(self, text="NAV" , fg="orange", bg="black", font="Verdana 15 bold", width=10)
        navLed.grid(row=5,column=3)

        #strobe light led
        strobeLed = Label(self, text="STROBE" , fg="orange", bg="black", font="Verdana 15 bold", width=10)
        strobeLed.grid(row=6,column=3)

        #pitot heat led
        pitotHeatLed = Label(self, text="PITOT HEAT" , fg="orange", bg="black", font="Verdana 15 bold", width=10)
        pitotHeatLed.grid(row=7,column=3)

        #avionics master led
        avionicsMasterLed = Label(self, text="AVIONICS\n MASTER" , fg="orange", bg="black", font="Verdana 15 bold", width=10)
        avionicsMasterLed.grid(row=8,column=3)


        #--------------------end - leds

        startThread()


if __name__ == "__main__":
    app = XPanel(None)
    app.title("XPANEL V0.0")
    app.mainloop()






