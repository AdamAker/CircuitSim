import Protoboard as pb
import numpy as np
import cmath as c
import Matpy as mp

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
     
     #set vmax for capacitor
    def setvmax(self, vmax):
         self.vmax=vmax
    #end setvmax
     
    #get vmax for capacitor
    def getvmax(self):
         return self.vmax
    #end getvmax
     
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
               self.source=[Vpp*np.cos(2*(3.141592654)*f*t) for t in range(1000)]
          elif type == "sin":
               self.source=[Vpp*np.sin(2*(3.141592654)*f*t) for t in range(1000)]
          elif type == "const":
               self.source=[Vpp for t in range(1000)]
          else:
               print("type is not sinusoidal")
    #end setv
    
    #def setvsqr(self, Vpp, dcycle, T):
    #for t in range(1000):
    
    #get the voltage source
    def getvsource(self):
          return self.source
    #end getvsource

##--Loop subclass--##
    
class Loop(Component):

     #inialize loop
     def __init__(self,obj1,obj2,obj3,obj4):
          s1=obj1.getwiresz()
          s3=obj3.getwiresz()
          self.vert1=s1[0]
          self.vert2=s1[1]
          self.vert3=s3[0]
          self.vert4=s3[1]
          wire1=obj1.getcompstr()
          wire2=obj2.getcompstr()
          wire3=obj3.getcompstr()
          wire4=obj4.getcompstr()
          self.loop={1:obj1, 2:obj2, 3:obj3, 4:obj4}
          self.loopstr={1:wire1, 2:wire2, 3:wire3, 4:wire4}
          self.R=0
          self.L=0
          self.C=0
          self.V=[]
          self.i=[]
          self.q=[]
          self.didt=[]
          self.VC=[]
          self.VR=[]
          self.VL=[]
     #end __init__

     #resizes and repositions the loop (based on self.vert1)
     def setloopsz(self, x0, y0, n, m):
          x0=int(x0)
          y0=int(y0)
          n=int(n)
          m=int(m)
          self.vert1=[x0,y0]
          self.vert2=[x0+n,y0]
          self.vert3=[x0+n,y0+m]
          self.vert4=[x0,y0+m]
          obj1.setwiresz(x0,y0,n,"horz")
          obj2.setwiresz((x0+n),y0,m,"vert")
          obj3.setwiresz((x0+n),(y0+m),-1*n,"horz")
          obj4.setwiresz(x0,(y0+m),-1*m,"vert")
          
     #end setloopsz
     
     #searches the loop for components
     def searchloop(self):
          for i in range(4):
               l=self.loopstr[i+1]
               for j in range(len(l)):
                    if self.loopstr[i+1][j]=="R":
                         self.R=self.R+self.loop[i+1].comps[j].getR()
                    elif self.loopstr[i+1][j]=="L":
                         self.L=self.L+self.loop[i+1].comps[j].getL()
                    elif self.loopstr[i+1][j]=="C":
                         if self.C == 0:
                              self.C=self.loop[i+1].comps[j].getC()
                         else:
                              self.C=1/(1/(self.C)+1/(self.loop[i+1].comps[j].getC()))
                         #end if
                    elif self.loopstr[i+1][j]=="V":
                         self.V=self.loop[i+1].comps[j].getvsource()
                    #end if
               #end for     
          #end for
          return [self.R, self.L, self.C, self.V]
     #end search loop
     
     #solve the loop
     def loopsolver(self,i0,q0,dt,tmax, *args):
          c=self.searchloop()
          M=mp.Matpy()
          t=M.domain(0,dt,tmax)
          dt=t[1]-t[0]
          self.didt=[0 for k in range(len(c[3]))]
          self.i=[0 for k in range(len(c[3]))]
          self.q=[0 for k in range(len(c[3]))]
          if c[1]==0:
               self.q[0]=q0/2
               for l in range(len(c[3])-1):
                    self.i[l]=-1*(1/(c[0]*c[2]))*self.q[l]+(1/c[0])*c[3][l]
                    self.q[l+1]=self.q[l]+(c[2]*c[0])*self.i[l]*dt
               #end for
          elif c[2]==0:
               self.i[0]=i0/2
               for l in range(len(c[3])-1):
                    self.didt[l]=-1*(c[0]/c[1])*self.i[l]+(1/c[1])*c[3][l]
                    self.i[l+1]=self.i[l]+(c[1]/c[0])*self.didt[l]*dt
               #end for
          elif c[0]==0:
               self.q[0]=q0/2
               self.i[0]=i0/2
               for l in range(len(c[3])-1):
                    self.didt[l]=-1*(1/(c[1]*c[2]))*self.q[l]+(1/c[1])*c[3][l]
                    self.i[l+1]=self.i[l]+c[1]*self.didt[l]*dt
                    self.q[l+1]=self.q[l]+c[2]*self.i[l]*dt
               #end for
          else:
               self.q[0]=q0/2
               self.i[0]=i0/2
               for l in range(len(c[3])-1):
                    self.didt[l]=-1*(1/(c[1]*c[2]))*self.q[l]+-1*(c[0]/c[1])*self.i[l]+(1/c[1])*c[3][l]
                    self.i[l+1]=self.i[l]+(c[1]/c[0])*self.didt[l]*dt
                    self.q[l+1]=self.q[l]+(c[2]*c[0])*self.i[l]*dt
               #end for
          #end if
               
     #end loopsolver
     #gets loop verticies
     def getloopsz(self):
          return [self.vert1,self.vert2,self.vert3,self.vert4]
     #end getloopsz
     
     def getloopstr(self):
          return self.loopstr
     #end getloopstr
     
     def getloop(self):
          return self.loop
     #end getloop  
     
     def getloopatr(self):
          return [self.didt, self.i, self.q]
     #end getloopatr
     
     def getloopv(self):
          for j in range(len(self.didt)):
               self.VL.append(self.L*self.didt[j])
          #end for
          for j in range(len(self.i)):
               self.VR.append(self.R*self.i[j])
          #end for
          for j in range(len(self.q)):
               if self.C!=0:
                    self.VC.append((1/self.C)*self.q[j])
               else:
                    self.VC.append(0)
          #end for
          
          return [self.VL,self.VR,self.VC,self.V]
     #end getloopv
     
##--Wire subclass--##
     
class Wire(Component):

     #initialize wire
     def __init__(self,x0,y0,n,orient):
          x0=int(x0)
          y0=int(y0)
          n=int(n)
          self.vert1=[x0,y0]
          if orient == "horz":
               self.vert2=[x0+n,y0]
               self.orient="horz"
          elif orient == "vert":
               self.vert2=[x0,y0+n]
               self.orient="vert"
          else:
               print("Not a valid orientation")
          #end if
          self.comps=[]
          self.compstr=[]
     #end __init__
     
     #set the wire size
     def setwiresz(self, x0, y0, n, orient):
          x0=int(x0)
          y0=int(y0)
          n=int(n)
          self.vert1=[x0,y0]
          if orient == "horz":
               self.vert2=[x0+n,y0]
          elif orient == "vert":
               self.vert2=[x0,y0+n]
          else:
               print("Not a valid orientation")
          #end if
     #end setwiresz
     
     def getwiresz(self):
          return [self.vert1, self.vert2]
     #end getwiresz
     
     def getorient(self):
          return self.orient
     #end getorient
     
     #add a component to the wire
     def addcomp(self,obj1,obj2,x,y):
          obj1.setpos(obj2,x,y)
          s=obj1.getpos()
          self.comps.append(obj1)
          if isinstance(obj1,Resistor):
               self.compstr.append("R")
          elif isinstance(obj1,Inductor):
               self.compstr.append("L")
          elif isinstance(obj1,Capacitor):
               self.compstr.append("C")
          elif isinstance(obj1, VoltageSource):
               self.compstr.append("V")
          else:
               print("Not a valid component type")
     #end addcomp
     
     def getcompstr(self):
          return self.compstr
     #end getcompstr
     
     #swap two components in a wire
     def swapcomp(self,i,j):
          if len(self.comps)>=2:
               a=self.comps[i]
               self.comps[i]=self.comps[j]
               self.comps[j]=a
          else:
               print("wire has less than two elements")
          #end if
     #end swapcomp