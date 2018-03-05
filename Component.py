import Protoboard as pb
import numpy as np
import cmath as c

class Component(object):

    #Initialize internal component characteristics
    def __init__(self):
        self.Z=0                #Ohms
        self.L=0                #Henrys
        self.C=0                #Farads

        #initialize component locaton at origin of prortoboard.
        self.locx = 0           #x location of component
        self.locy = 0           #y location of component
    #end __init__

    #recharacterize internal component characteristics
    def setchar(self, r,l,c):
        self.Z=r
        self.L=l
        self.C=c
    #end setchar

    #get component characteristics
    def getchar(self):
        return[self.Z,self.L,self.C]
    #end getchar

    #repositions the component to location (x,y) on the protoboard
    def setpos(self, obj, x,y):
        bounds=obj.getsize()
        x=int(x)
        y=int(y)
        if x>0 and x<=bounds[0] and y>0 and y<=bounds[1]:
            self.locx=x
            self.locy=y
        else:
            print("index out of bounds of protoboard.")
        #endif
    #end setpos

    #get position of component
    def getpos(self):
        return[self.locx,self.locy]
    #end getpos
    
    #erase component
    def erase(self,obj):
          del obj
    #end erase

##--Resistor subclass--##

class Resistor(Component):

    #initialize resistor
    def __init__(self):
        super().__init__()
        self.pmax=0
    #end __init__
    
    #set Pmax for resistor
    def setpmax(self, P):
         self.pmax=P
    #end setPmax

    #get getPmax
    def getpmax(self):
        return self.pmax
    #end getPmax
    
    #set resistance
    def setR(self, R):
         self.setchar(R,0,0)
    #end setR
    
    #get resistance
    def getR(self):
         s=self.getchar()
         return s[0]
    #end getR

##--Capacitor subclass--##

class Capacitor(Component):

    #initialize capacitor
    def __init__(self):
        super().__init__()
        self.vmax=0
    #end __init__ 

    #set capacitance
    def setC(self, C):
         self.setchar(0,0,C)
    #end setR
    
    #get capacitance
    def getC(self):
         s=self.getchar()
         return s[2]
    #end getR

##--Inductor subclass--##

class Inductor(Component):

    #initialize inductor
    def __init__(self):
        super().__init__()
        
    #end __init__
    
    #set inductance
    def setL(self, L):
         self.setchar(0,L,0)
    #end setR
    
    #get inductance
    def getL(self):
         s=self.getchar()
         return s[1]
    #end getR

##--Voltage Source subclass--##

class VoltageSource(Component):

    #initialize source
    def __init__(self):
        super().__init__()
        self.source=[0 for i in range(1000)]
    #end __init__
    
    def setvsinu(self, Vpp, type, f):
          if type == "cos":
               self.source=[Vpp*cos(2*(3.141592654)*f*t) for t in range(1000)]
          elif type == "sin":
               self.source=[Vpp*sin(2*(3.141592654)*f*t) for t in range(1000)]
          else:
               print("type is not sinusoidal")
    #end setv
    
    #def setvsqr(self, Vpp, dcycle, T):
    #for t in range(1000):

class Loop(Component):

     #inialize loop
     def __init__(self):
          super().__init__()
          self.vert1=[0,0]
          self.vert2=[1,0]
          self.vert3=[1,1]
          self.vert4=[0,1]
          self.loop={1: self.vert1, 2: self.vert2, 3: self.vert3, 4: self.vert4}
     #end __init__

     #add a component
     def addcomp(self,key,obj):
          s=obj.getpos()
          self.loop[key : s]
     #end addcomp

     #resizes and repositions the loop (based on vert1
     def setloopsz(self, x0, y0, n, m):
          x0=int(x0)
          y0=int(y0)
          n=int(n)
          m=int(m)
          self.vert1=[x0,y0]
          self.vert2=[x0+n,y0]
          self.vert3=[x0+n,y0+m]
          self.vert4=[x0,y0+m]
     #end setloopsz
     
     def getloopsz(self):
          return [self.vert1,self.vert2,self.vert3,self.vert4]
     #end getloopsz