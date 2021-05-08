import numpy as np
import argparse

def choleskyDecomp(a):
    a = np.array(a,float)
    L = np.zeros_like(a)
    n,_ = np.shape(a)
    for j in range(n):
        for i in range(j,n):
            if(i == j):
                L[i,j] = np.sqrt(a[i,j] - np.sum(L[i,:j]** 2))
            else:
                L[i,j] = (a[i,j] - np.sum(L[i,:j]*L[j,:j])) / L[j,j]
    return L


def LUSol(L,U,b):
    L = np.array(L,float)
    U = np.array(U,float)
    b = np.array(b,float)
    n,_ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    for i in range(n):
        y[i] = (b[i] - np.sum(L[i,:i] *y[:i]))/L[i,i]
    
    for i in range(n-1,-1,-1):
        x[i] = (y[i] - np.sum(U[i,i+1:n] * x[i+1:n]))/U[i,i]

    return x

def solver():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", required=True, # var is named i 
	help="path to matrix file")
    parser.add_argument("-v", required=True, # var is named i 
	help="path to vector file")
    arg = vars(parser.parse_args())
    a = np.loadtxt(arg["m"])
    b = np.loadtxt(arg["v"])
    print(a)
    L = choleskyDecomp(a)
    print(b)
    x = LUSol(L, np.transpose(L), b)

    print(x)
    print()

if __name__ == "__main__":
    solver()

    