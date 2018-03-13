import Protoboard as pb
import numpy as np
import matplotlib as ml
from matplotlib import pyplot as plt
import Matpy as mp

class Oscilloscope(object):

    def __init__(self,l):
        
        #initialize readings from all four probes
        self.probe1=[0 for i in range(l)]  #probe1
        self.probe2=[0 for i in range(l)]  #probe2
        self.probe3=[0 for i in range(l)]  #probe3
        self.probe4=[0 for i in range(l)]  #probe4

        #initialize probe locations
        self.probe1x=-1     #x coordinate of probe1  
        self.probe1y=0      #y coordinate of probe1

        self.probe2x=-1     #x coordinate of probe2
        self.probe2y=1      #y coordinate of probe2

        self.probe3x=-1     #x coordinate of probe3
        self.probe3y=2      #y coordinate of probe3

        self.probe4x=-1     #x coordinate of probe4
        self.probe4y=3      #y coordinate of probe4

        #initialize trigger voltages for channels 1-4
        self.trigger1=[1 for i in range(l)]      #trigger voltage for channel1
        self.trigger2=[1 for i in range(l)]      #trigger voltage for channel2
        self.trigger3=[1 for i in range(l)]      #trigger voltage for channel3
        self.trigger4=[1 for i in range(l)]      #trigger voltage for channel4

        #initialize screen for scope object
        self.scr=plt
        self.scr.figure(2)
        
        #set labels
        self.scr.xlabel("time (s)")
        self.scr.ylabel("voltage (V)")
    #end __init__

    #set the values in probe given by num
    def setprobe(self, num, V=[], *args):
        if   num == 1:
            self.probe1=V
        elif num == 2:
            self.probe2=V
        elif num == 3:
            self.probe3=V
        elif num == 4:
            self.probe4=V
        else:
            print("Invalid channel number")
        #end settrig

    #get the values in probe given by num
    def getprobe(self, num):
        if   num == 1:
            return self.probe1
        elif num == 2:
            return self.probe2
        elif num == 3:
            return self.probe3
        elif num == 4:
            return self.probe4
        else:
            print("There are no probes with that number")  
    #end getprobe

    #get the location of a given probe on the protoboard
    def getloc(self, num):
        if    num == 1:
            return [self.probe1x,self.probe1y]
        elif num == 2:
            return [self.probe2x,self.probe2y]
        elif num == 3:
            return [self.probe3x,self.probe3y]
        elif num == 4:
            return [self.probe4x,self.probe4y]
        else:
            print("There are no probes with that number")
    #end getloc

    #set trigger values for a channel
    def settrig(self, num, V=[], *args):
        if   num == 1:
            self.trigger1=V
        elif num == 2:
            self.trigger2=V
        elif num == 3:
            self.trigger3=V
        elif num == 4:
            self.trigger4=V
        else:
            print("Invalid channel number")
        #end settrig
            
    #get trigger value for a channel
    def gettrig(self, num):
        if   num == 1:
            return self.trigger1
        elif num == 2:
            return self.trigger2
        elif num == 3:
            return self.trigger3
        elif num == 4:
            return self.trigger4
        else:
            print("Invalid channel number")
    #end gettrig
            
    #set screen/plot parameters
    def setscreen(self, scaleT, scaleV, tmax, Vmax, trig=[],color=[],linetype=[], chon=[], *args):
        l=len(self.getprobe(1))
        M=mp.Matpy()
        p=[[0 for i in range(l)],[0 for i in range(l)],[0 for i in range(l)],[0 for i in range(l)]]
        t=[[0 for i in range(l)],[0 for i in range(l)],[0 for i in range(l)],[0 for i in range(l)]]
        delta=[[0 for i in range(l)],[0 for i in range(l)],[0 for i in range(l)],[0 for i in range(l)]]
        ax=self.scr.subplot(111, facecolor='w') 
        time=[i for i in range(l)] 
        self.scr.axis([0, tmax , -Vmax , Vmax])
        for j in range(4):
          p[j]=self.getprobe(j+1)
          t[j]=self.gettrig(j+1)
          self.scr.plot([1,1,1], label="probe"+ " " +str(j+1))
          for k in range(l):
               if trig[j]:
                    if p[j][k]>t[j][k]:
                         delta[j][k]=p[j][k]
                    else:
                         delta[j][k]=0
                    #end if
               else:
                    delta[j][k]=p[j][k]
               #end if
               
          #end for
               
        #end for
        labels=[0,0,0,0]
        for j in range(4):
             if chon[j]:
                  if color[j] == "red":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'r:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'r-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'r--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'r-')
                      else:
                         print("Invalid line type")
                  elif color[j] == "blue":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'b:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'b-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'b--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'b-')
                      else:
                         print("Invalid line type")
                  elif color[j] == "cyan":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'c:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'c-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'c--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'c-')
                      else:
                         print("Invalid line type")
                  elif color[j] == "green":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'g:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'g-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'g--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'g-')
                      else:
                         print("Invalid line type")
                  elif color[j] == "yellow":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'y:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'y-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'y--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'y-')
                      else:
                         print("Invalid line type")
                  elif color[j] == "black":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'k:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'k-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'k--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'k-')
                      else:
                         print("Invalid line type")
                  elif color[j] == "magenta":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'm:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'm-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'm--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'm-')
                      else:
                         print("Invalid line type")
                  elif color[j] == "white":
                      if linetype[j] == ":":
                         labels[j]=self.scr.plot(delta[j], 'w:')
                      elif linetype[j] == "-.":
                         labels[j]=self.scr.plot(delta[j], 'w-.')
                      elif linetype[j] == "--":
                         labels[j]=self.scr.plot(delta[j], 'w--')
                      elif linetype[j] == "-":
                         labels[j]=self.scr.plot(delta[j], 'w-')
                      else:
                         print("Invalid line type")
                  else:
                      print("Invalid color")
                  #end if
             #end if
        #end for

        if scaleT == "ns":
             self.scr.xlabel("time (ns)")
        elif scaleT == "us":
             self.scr.xlabel("time (us)")
        elif scaleT == "ms":
             self.scr.xlabel("time (ms)")
        elif scaleT == "s":
             self.scr.xlabel("time (s)")
        else:
             print("Entry is not a valid time scale")
        #end if
        
        
        if scaleV == "mV":
             self.scr.ylabel("voltage (mV)")
        elif scaleV == "V":
             self.scr.ylabel("voltage (V)")
        else:
              print("Entry is not a valid voltage scale")
        #end if
        self.scr.legend(bbox_to_anchor=(0.,1.02,1.,.102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
    #end setscreen

    #gets the screen (plots the screen)
    def getscreen(self):
          self.scr.show()
    #end getscreen
     
    def erase(self):
          self.scr.remove()
    #end erase

