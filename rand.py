#!/usr/bin/env python3
import sys
import random
import pandas as pd

argv = sys.argv 

def makeRows(columns):
    row = []
    for i in range(columns):
        row.append(None)
    return row

def makeMatrix(rows,columns):
    matrix =[]
    row =[]
    for i in range(rows):
        row=makeRows(columns)
        matrix.append(row)
    return matrix
            
if argv[1] == "--n" and argv[2] == "--i":
    minimun = int(argv[3])
    maximun = int(argv[4])
    print("your random number is: \n",random.randint(minimun,maximun),"\n")
elif argv[1] =="--n" and argv[2] == "--f":
    minimun = float(argv[3])
    maximun = float(argv[4])
    print("your random number is: \n",random.uniform(minimun,maximun),"\n")
elif argv[1] =="--csv" and argv[2] =="--i":

    minimum = int(argv[3])
    maximum = int(argv[4])
    
    randomIntMatrix = makeMatrix(int(argv[5]),int(argv[6]))

    name = argv[7].strip()
    save = argv[8].strip()

    saving =save+"/"+name+".csv"

    for i in range(len(randomIntMatrix)):
        for j in range(len(randomIntMatrix[0])):
            randomIntMatrix[i][j] = random.randint(minimum,maximum)
    df = pd.DataFrame(randomIntMatrix)
    df.to_csv(saving,index=False,header=False)
    
elif argv[1] =="--csv" and argv[2] =="--f":

    minimum = float(argv[3])
    maximum = float(argv[4])
    
    randomFloatMatrix = makeMatrix(int(argv[5]),int(argv[6]))

    name = argv[7].strip()
    save = argv[8].strip()

    saving =save+"/"+name+".csv"

    for i in range(len(randomFloatMatrix)):
        for j in range(len(randomFloatMatrix[0])):
            randomFloatMatrix[i][j] = random.uniform(minimum,maximum)
    
    df = pd.DataFrame(randomFloatMatrix)
    df.to_csv(saving,index=False,header=False)
    
elif argv[1] =="--json" and argv[2] =="--i":

    minimum = int(argv[3])
    maximum = int(argv[4])
    
    randomIntMatrix = makeMatrix(int(argv[5]),int(argv[6]))

    name = argv[7].strip()
    save = argv[8].strip()

    saving =save+"/"+name+".json"

    for i in range(len(randomIntMatrix)):
        for j in range(len(randomIntMatrix[0])):
            randomIntMatrix[i][j] = random.randint(minimum,maximum)
    df = pd.DataFrame(randomIntMatrix)
    df.to_json(saving)
elif argv[1] =="--json" and argv[2] =="--f":

    minimum = float(argv[3])
    maximum = float(argv[4])
    
    randomFloatMatrix = makeMatrix(int(argv[5]),int(argv[6]))

    name = argv[7].strip()
    save = argv[8].strip()

    saving =save+"/"+name+".json"

    for i in range(len(randomFloatMatrix)):
        for j in range(len(randomFloatMatrix[0])):
            randomFloatMatrix[i][j] = random.uniform(minimum,maximum)
    
    df = pd.DataFrame(randomFloatMatrix)
    df.to_json(saving)
elif argv[1] =="--excel" and argv[2] =="--i":

    minimum = int(argv[3])
    maximum = int(argv[4])
    
    randomIntMatrix = makeMatrix(int(argv[5]),int(argv[6]))

    name = argv[7].strip()
    save = argv[8].strip()

    saving =save+"/"+name+".xlsx"

    for i in range(len(randomIntMatrix)):
        for j in range(len(randomIntMatrix[0])):
            randomIntMatrix[i][j] = random.randint(minimum,maximum)
    df = pd.DataFrame(randomIntMatrix)
    df.to_excel(saving,index=False,header=False)

elif argv[1] =="--excel" and argv[2] =="--f":

    minimum = float(argv[3])
    maximum = float(argv[4])
    
    randomFloatMatrix = makeMatrix(int(argv[5]),int(argv[6]))

    name = argv[7].strip()
    save = argv[8].strip()

    saving =save+"/"+name+".xlsx"

    for i in range(len(randomFloatMatrix)):
        for j in range(len(randomFloatMatrix[0])):
            randomFloatMatrix[i][j] = random.uniform(minimum,maximum)
    
    df = pd.DataFrame(randomFloatMatrix)
    df.to_excel(saving,header=False,index=False)

