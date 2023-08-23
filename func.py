import os
import numpy as np
import math


def createB(A, B0, nRes):
    B = []

    for i in range(0, nRes):
        B.append([])
        for j in range(0, nRes):
            B[i].append(A[i][B0[j]-1])

    return B

def createCB(C, B0, nRes):
    CB = []

    for i in range(0, nRes):
        CB.append(C[B0[i] - 1])

    return CB

def calculateRelativeCosts(C, p, A, N, nVar, nRes):
    s = math.inf
    k = -1

    si = 0
    for i in range(0, nVar-nRes):

        Ai = []
        for j in range(0, nRes):
            Ai.append(A[j][N[i]-1])

        si = C[N[i]-1] - np.matmul(p,Ai)

        if si < s:
            s = si
            k = i

    if s >= 0:
        return -1

    return k

def ratioTest(B1, A, XB, N, k, nRes):
    Ak = []
    for i in range(0, nRes):
        Ak.append(A[i][N[k] - 1])

    y = np.matmul(B1,Ak)

    min = math.inf
    l = -1

    r = 0
    for i in range(0, nRes):
        if y[i] > 0:
            r = XB[i] / y[i]
            if r < min:
                min = r
                l = i

    return l

def printAnswer(B0, XB, C, nRes, nVar):
    X = []

    for i in  range(0, nVar):
        X.append(0)

    for i in range(0, nRes):
        X[B0[i]-1] = XB[i]

    FX = np.matmul(C,X)

    print("Variables values -> ", X)
    print("Great result     -> " ,FX)

def Simplex(C, A, b, B0, N, nVar, nRes):
    while 1:
        B = createB(A, B0, nRes)

        CB = createCB(C, B0, nRes)

        B1 = np.linalg.inv(B)

        XB = np.matmul(B1, b)

        FX = np.matmul(CB, XB)

        p = np.matmul(CB, B1)

        k = calculateRelativeCosts(C, p, A, N, nVar, nRes)
        if k == -1:
            break
        l = ratioTest(B1, A, XB, N, k, nRes)
        if l == -1:
            break
        aux = B0[l]
        B0[l] = N[k]
        N[k] = aux

    printAnswer(B0, XB, C, nRes, nVar)




