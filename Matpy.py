import cmath as c
import numpy as np

class Matpy(object):

     #initialize an empty array
     def __init__(self):
          self.array = [[1,2,3],[4,5,6],[7,8,9]]
     #end __init__
     
     #makes an nxm 2D array of zeros
     def zeros(self, n, m):
          A=[[0 for j in range(m)]]
          for i in range(n-1):
               A.append([0 for j in range(m)])
          #end for
          return A
     #end zeros
        
     #makes an nxm 2D array of ones
     def ones(self, n, m):
          A=[[1 for j in range(m)]]
          for i in range(n-1):
               A.append([1 for j in range(m)])
          #end for
          return A
     #end ones
     
     #makes an nxm identity matrix
     def identity(self, n, m):
          I=self.zeros(n,m)
          for i in range(n):
               for j in range(m):
                    if i==j:
                         I[i][j]=1
                    else:
                         I[i][j]=0
                    #end if
               #end for
          #end for
          return I
     #end identity
     
     #scalar multiplication
     def smul(self, a, A=[], *args):
          B=self.zeros(len(A[0]),len(A[:]))
          for i in range(len(A[:])):
               for j in range(len(A[0])):
                    B[i][j]=a*A[i][j]
               #end for
          #end for
          return B
     #end smul
     
     #transposes the given matrix
     def tran(self, A=[], *args):
          B=self.zeros(len(A[0]),len(A[:]))
          for i in range(len(A[0])):
               for j in range(len(A[:])):
                    B[i][j]=A[j][i]
               #end for
          #end for
          return B
     #end t
     
     #defines matrix multiplication: multiplies AB, not BA
     def mul(self, A=[], B=[], *args):
          if len(A[0])==len(B[:]):
               C=self.zeros(len(A[:]),len(B[0]))
               for i in range(len(A[:])):
                    for j in range(len(B[0])):
                         sum=0
                         for k in range(len(A[0])):
                              sum=sum+A[i][k]*B[k][j]
                         #end for
                         C[i][j]=sum
                    #end for
               #end for
               return C
          #end if
          else:
               print("Dimensions do not match")
               return None
          #end if
     #end mul
     
     #create a domain
     def domain(self, x0, dx, xn):
          x=[x0]
          i=0
          while x[i]<xn:
             x.insert(i+1,x[i]+dx)
             i=i+1
          return x
     #end domain   
     
     #fast fourier transform
     #def FFT(self, dx, fx=[], *args):
          #N=int(len(fx)/2)
          #M=mp.Matpy()
          #k=M.domain(-N,1,N-1)
          #fk=[0 for i in range(len(fx)]
          #for l in range(len(fx)):
               
          
     #end FFT
     
     #Calculates the determinant of the matrix
     #def det(self, A=[], *args):
          #for l in range(len(A[:])):
               #for m in range(len(A[0])):
                   
     #end det
     
