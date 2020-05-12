import matplotlib.pyplot as plt

A = B = P = M = S = None 
d = 100

def readABP():
    global A, B, P
    A = []
    B = []
    P = []

    with open('A.txt', 'r') as fd:
        line = fd.readline()
        while line:
            row = line.split(' ')
            for i in range(len(row)):
                row[i] = float(row[i])
            A.append(row)
            line = fd.readline()

    with open('B.txt', 'r') as fd:
        line = fd.readline()
        while line:
            row = line.split(' ')
            for i in range(len(row)):
                row[i] = float(row[i])
            B.append(row)
            line = fd.readline()


    with open('P.txt', 'r') as fd:
        line = fd.readline()
        while line:
            row = line.split(' ')
            for i in range(len(row)):
                row[i] = float(row[i])
            P.append(row)
            line = fd.readline()
       

def getMatricesM():
    global A, B, d, M

    Amax = max([el for row in A for el in row])
    Bmax = max([el for row in B for el in row])
    M = []

    for di in range(d):
        newMatrix = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[i])):
                row.append((di / Amax) * A[i][j] + ((d - di) / Bmax) * B[i][j])
            newMatrix.append(row)
        M.append(newMatrix)

def dotProduct(matrix1, matrix2):
    totalSum = 0

    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            totalSum += matrix1[i][j] * matrix2[i][j]

    return totalSum

def computeS():
    global S
    S = []

    for di in range(d):
        aux1 = dotProduct(M[di], P)
        aux2 = dotProduct(P, P)
        aux3 = dotProduct(M[di], M[di])

        S.append((aux1 * aux1) / (aux2 * aux3))

    plt.plot(S)
    plt.ylabel('Probability')
    plt.xlabel('d')
    plt.show()
    
if __name__ == '__main__':
    readABP()
    getMatricesM()
    computeS()