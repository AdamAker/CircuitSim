import numpy as np
import Matpy as mp
import Component as cm
import matplotlib as ml
from matplotlib import pyplot as plt

class Protoboard(object):
    
    #initialize a 40 by 40 grid of points.
    def __init__(self):
        k=40
        j=40

        #k is a multiplicative factor
        #j gives the noninclusive upperbound of the points to be ploted.
        self.x=[i%j for i in range(k*j)]
        self.y=[int(i/j) for i in range(k*j)]
        #x=[0, 1, 2, ... j-1, (repeats k times)]
        #y=[0, ... , 0 (j zeros), 1, ..., 1 (j zeros)]

        #master dictionary to store loops
        self.master={}

        #protoboard
        self.board=plt
        self.board.figure(1)
        self.ax=self.board.subplot()

    #end__init__

    #resizes grid to be n by m.
    def regrid(self, n, m):
        self.x=[i%m for i in range(n*m)]
        self.y=[int(i/m) for i in range(n*m)]
        self.sizex=m
        self.sizey=n
    #endregrid

    #returns size of the protoboard
    def getsize(self):
        return[self.sizex, self.sizey]
    #end boardsize

    #sets the protoboard.
    def setboard(self):
        self.board.plot(self.x,self.y,'.')
        self.board.rc('grid', c='0.5', ls='-', lw=5)
        self.board.grid(False)
        self.board.axis([-1, self.sizex, -1, self.sizey])
        self.board.title(r'$\sqrt{2\pi}F(\omega)=\int f(t)e^{i\omega t} dt$', fontsize = 20)
        self.board.xlabel('horizontal pins')
        self.board.ylabel('vertical pins')
        #plt.show()
    #endplotboard
     
    #draw loop on the protoboard
    def drawloop(self,obj,color):
         v=obj.getloopsz()
         M=mp.Matpy()
         xline1=M.domain(v[0][0], .01, v[1][0])
         yline1=[v[0][1] for i in range(len(xline1))]
         yline2=M.domain(v[1][1], .01, v[2][1])
         xline2=[v[1][0] for i in range(len(yline2))]
         xline3=M.domain(v[3][0], .01, v[2][0])
         yline3=[v[2][1] for i in range(len(xline3))]
         yline4=M.domain(v[0][1], .01, v[3][1])
         xline4=[v[3][0] for i in range(len(yline4))]
         if color == "black":
              self.ax.plot(xline1,yline1,"k-")
              self.ax.plot(xline2,yline2,"k-")
              self.ax.plot(xline3,yline3,"k-")
              self.ax.plot(xline4,yline4,"k-")
         elif color == "red":
              self.ax.plot(xline1,yline1,"r-")
              self.ax.plot(xline2,yline2,"r-")
              self.ax.plot(xline3,yline3,"r-")
              self.ax.plot(xline4,yline4,"r-")
         elif color == "green":
              self.ax.plot(xline1,yline1,"g-")
              self.ax.plot(xline2,yline2,"g-")
              self.ax.plot(xline3,yline3,"g-")
              self.ax.plot(xline4,yline4,"g-")
         elif color == "blue":
              self.ax.plot(xline1,yline1,"b-")
              self.ax.plot(xline2,yline2,"b-")
              self.ax.plot(xline3,yline3,"b-")
              self.ax.plot(xline4,yline4,"b-")
         elif color == "cyan":
              self.ax.plot(xline1,yline1,"c-")
              self.ax.plot(xline2,yline2,"c-")
              self.ax.plot(xline3,yline3,"c-")
              self.ax.plot(xline4,yline4,"c-")
         elif color == "magenta":
              self.ax.plot(xline1,yline1,"m-")
              self.ax.plot(xline2,yline2,"m-")
              self.ax.plot(xline3,yline3,"m-")
              self.ax.plot(xline4,yline4,"m-")
         elif color == "yellow":
              self.ax.plot(xline1,yline1,"y-")
              self.ax.plot(xline2,yline2,"y-")
              self.ax.plot(xline3,yline3,"y-")
              self.ax.plot(xline4,yline4,"y-")
         else:
              print("Invalid color")
         #end if
    #end drawloop
    
    #draws a horizontal or vertical wire on the protoboard
    def drawwire(self,obj,orient,color):
         M=mp.Matpy()
         orient=obj.getorient()
         v=obj.getwiresz()
         if orient == "vert":
               yline=M.domain(v[0][1],.01,v[1][1])
               xline=[v[0][0] for i in range(len(yline))]
         elif orient == "horz":
               xline=M.domain(v[0][0],.01,v[1][0])
               yline=[v[0][1] for i in range(len(xline))]
         else:
               print("Not a valid orientation")
         #end if
         if color == "black":
               self.ax.plot(xline,yline,"k-")
         elif color == "red":
               self.ax.plot(xline,yline,"r-")
         elif color == "green":
               self.ax.plot(xline,yline,"g-")
         elif color == "blue":
               self.ax.plot(xline,yline,"b-")
         elif color == "cyan":
               self.ax.plot(xline,yline,"c-")
         elif color == "magenta":
               self.ax.plot(xline,yline,"m-")
         elif color == "yellow":
               self.ax.plot(xline,yline,"y-")
         else:
              print("Invalid color")
         #end if
    #end draw wire
    
    #draw resistor
    def drawR(self,obj,color):
         s=obj.getpos()
         if color == "black":
               self.ax.plot(s[0],s[1],"ks")
         elif color == "red":
               self.ax.plot(s[0],s[1],"rs")
         elif color == "green":
               self.ax.plot(s[0],s[1],"gs")
         elif color == "blue":
               self.ax.plot(s[0],s[1],"bs")
         elif color == "cyan":
               self.ax.plot(s[0],s[1],"cs")
         elif color == "magenta":
               self.ax.plot(s[0],s[1],"ms")
         elif color == "yellow":
               self.ax.plot(s[0],s[1],"ys")
         else:
              print("Invalid color")
         #end if
    #end drawR
    
    #draw inductor
    def drawL(self,obj,color):
         s=obj.getpos()
         if color == "black":
               self.ax.plot(s[0],s[1],"k^")
         elif color == "red":
               self.ax.plot(s[0],s[1],"r^")
         elif color == "green":
               self.ax.plot(s[0],s[1],"g^")
         elif color == "blue":
               self.ax.plot(s[0],s[1],"b^")
         elif color == "cyan":
               self.ax.plot(s[0],s[1],"c^")
         elif color == "magenta":
               self.ax.plot(s[0],s[1],"m^")
         elif color == "yellow":
               self.ax.plot(s[0],s[1],"y^")
         else:
              print("Invalid color")
         #end if
    #end drawL
    
    #draw capacitor
    def drawC(self,obj,color):
         s=obj.getpos()
         if color == "black":
               self.ax.plot(s[0],s[1],"ko")
         elif color == "red":
               self.ax.plot(s[0],s[1],"ro")
         elif color == "green":
               self.ax.plot(s[0],s[1],"go")
         elif color == "blue":
               self.ax.plot(s[0],s[1],"bo")
         elif color == "cyan":
               self.ax.plot(s[0],s[1],"co")
         elif color == "magenta":
               self.ax.plot(s[0],s[1],"mo")
         elif color == "yellow":
               self.ax.plot(s[0],s[1],"yo")
         else:
              print("Invalid color")
         #end if
    #end drawR
    
    #draw voltage source
    def drawV(self,obj,color):
         s=obj.getpos()
         if color == "black":
               self.ax.plot(s[0],s[1],"kx")
         elif color == "red":
               self.ax.plot(s[0],s[1],"rx")
         elif color == "green":
               self.ax.plot(s[0],s[1],"gx")
         elif color == "blue":
               self.ax.plot(s[0],s[1],"bx")
         elif color == "cyan":
               self.ax.plot(s[0],s[1],"cx")
         elif color == "magenta":
               self.ax.plot(s[0],s[1],"mx")
         elif color == "yellow":
               self.ax.plot(s[0],s[1],"yx")
         else:
              print("Invalid color")
         #end if
    #end drawR
    
    #erases entire protoboard
    def erase(self):
          self.ax.remove()
    #end erase  
    
#endprotoboard
