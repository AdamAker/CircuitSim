import Protoboard as pb
import Component as cm
import Oscilloscope as osc
import numpy as np
import Matpy as mp


#import points to the module, not the class itself.
n=25
m=50
b=pb.Protoboard()
s=b.regrid(n,m)
b.setboard()



#test matpy class
M=mp.Matpy()
B=M.zeros(3,2)
print(B)
print(B[1][1])
B=M.tran(B)
print(B)
A=M.ones(3,2)
print(A)
C=M.mul(A,B)
print(C)
I=M.identity(3,3)
print(I)
D=M.smul(5,I)
print(D)

G=M.domain(0,.01,1)
print(G)

wire1=cm.Wire()

#test loop class
loop1=cm.Loop()
loop1.setloopsz(2,2,4,2)
v=loop1.getloopsz()
print(v)
b.drawloop(loop1,"black")
loop2=cm.Loop()
loop2.setloopsz(6,4,8,8)
w=loop2.getloopsz()
print(w)
b.drawloop(loop2,"red")

#testing components
r1=cm.Component()
r1.setchar(100,.000000001,.000000001)
r1.setpos(b,19.999999,20.034567)
posr1=r1.getpos()
print(posr1[0],posr1[1])
cr1=r1.getchar()
print(cr1[0],cr1[1],cr1[2])

#testing loop
V1=cm.VoltageSource()
V1.setvsinu(2,"cos",60)
V1.setpos(b,5,5)

r2=cm.Resistor()
r2.setpmax(10)
r2.setpos(b,10,10)
r2.setR(10)

c1=cm.Capacitor()
c1.setvmax(30)
c1.setpos(b,15,15)
c1.setC(10e-6)

l1=cm.Inductor()
l1.setpos(b,20,20)
l1.setL(10e-3)

wire1=cm.Wire()
wire1.setwiresz(8,15,10,"horz")
wire1.addcomp(V1,b,10,15)
wire1.addcomp(r2,b,9,15)
wire1.addcomp(l1,b,11,15)
wire1.addcomp(c1,b,17,15)
b.drawwire(wire1,"horz","red")

#testing oscilloscope
scope=osc.Oscilloscope()
f=[np.cos(2*3.14/500*i) for i in range(1000)]
g=[.5*np.sin(2*3.14/500*i) for i in range(1000)]
h=[0 for i in range(1000)]
a=[1 for i in range(1000)]
b=[np.exp(-.01*i) for i in range(1000)]
scope.setprobe(1,f)
scope.settrig(1,h)
scope.setprobe(2,g)
scope.settrig(2,f)
scope.setprobe(3,a)
scope.settrig(3,h)
scope.setprobe(4,b)
scope.settrig(4,h)
trig=[True,True,True,True]
color=["yellow","cyan","green","red"]
linetype=["--","-.","-",":"]
chon=[True,True,True,True]
scope.setscreen("us","mV",1.5, trig,color,linetype,chon)
scope.getscreen()

#testing the redrawing capability

#b=pb.Protoboard()
#b.regrid(n,m)
#b.setboard()
#b.drawloop(loop1,"black")
#b.drawwire(14,20,12,0,"horz","green")
#scope.getscreen()






