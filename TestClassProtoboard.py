import Protoboard as pb
import Component as cm
import Oscilloscope as osc
import numpy as np
import Matpy as mp
import matplotlib as ml
from matplotlib import pyplot as plt


#testing protoboard
n=25
m=50
b=pb.Protoboard()
s=b.regrid(n,m)
b.setboard()



#test matpy class
#M=mp.Matpy()
#B=M.zeros(3,2)
#print(B)
#print(B[1][1])
#B=M.tran(B)
#print(B)
#A=M.ones(3,2)
#print(A)
#C=M.mul(A,B)
#print(C)
#I=M.identity(3,3)
#print(I)
#D=M.smul(5,I)
#print(D)

#G=M.domain(0,.01,1)
#print(G)


#testing components
v1=cm.VoltageSource()
v1.setvsinu(0,"const",1/50)
v1.setpos(b,5,5)

r1=cm.Resistor()
r1.setpmax(10)
r1.setpos(b,10,10)
r1.setR(1e6)

c1=cm.Capacitor()
c1.setvmax(30)
c1.setpos(b,15,15)
c1.setC(1e-6)

l1=cm.Inductor()
l1.setpos(b,20,20)
l1.setL(1e-3)

wire1=cm.Wire(10,5,6,"horz")
wire1.addcomp(c1,b,13,5)
wire2=cm.Wire(16,5,6,"vert")
wire2.addcomp(l1,b,16,8)
wire3=cm.Wire(16,11,-6,"horz")
wire3.addcomp(r1,b,13,11)
wire4=cm.Wire(10,11,-6,"vert")
wire4.addcomp(v1,b,10,8)
loop1=cm.Loop(wire1,wire2,wire3,wire4)
dict1=loop1.getloopstr()
#print(dict1)
#print(dict1[1][0]=="C")

c=loop1.searchloop()
#print(c)
loop1.loopsolver(0,5e-7,.1,1000)
s=loop1.getloopv()
l=len(s[0])
scope1=osc.Oscilloscope(l)
scope1.setprobe(1,s[0])
scope1.setprobe(2,s[1])
scope1.setprobe(3,s[2])
scope1.setprobe(4,s[3])
trig=[False,False,False,False]
color=["blue","yellow","green","red"]
linetype=["-","-.","-",":"]
chon=[True,True,True,True]
scope1.setscreen("s","V",300,2.5,trig,color,linetype,chon)

#print(isinstance(r1,cm.Resistor))

b.drawloop(loop1,"red")
b.drawR(r1,"black")
b.drawL(l1,"blue")
b.drawC(c1,"green")
b.drawV(v1,"magenta")

scope1.getscreen()


#testing oscilloscope
#l=1000
#scope=osc.Oscilloscope(l)
#f=[np.cos(2*3.14/500*i) for i in range(l)]
#g=[.5*np.sin(2*3.14/500*i) for i in range(l)]
#h=[0 for i in range(l)]
#a=[1 for i in range(l)]
#b=[np.exp(-.01*i) for i in range(l)]
#scope.setprobe(1,f)
#scope.settrig(1,h)
#scope.setprobe(2,g)
#scope.settrig(2,f)
#scope.setprobe(3,a)
#scope.settrig(3,h)
#scope.setprobe(4,b)
#scope.settrig(4,h)
#trig=[True,True,True,True]
#color=["yellow","cyan","green","red"]
#linetype=["--","-.","-",":"]
#chon=[True,True,True,True]
#scope.setscreen("us","mV",1.5, trig,color,linetype,chon)
#scope.getscreen()

#testing the redrawing capability

#b=pb.Protoboard()
#b.regrid(n,m)
#b.setboard()
#b.drawloop(loop1,"black")
#b.drawwire(14,20,12,0,"horz","green")
#scope.getscreen()






