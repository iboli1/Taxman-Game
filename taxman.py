def getDividers(num):
    div_list = list()
    for i in range (1, int(num/2+1)):
        if num % i == 0:
            div_list.append(i)
    return div_list

def hasDividersInList(num, lista):
    dividers = getDividers(num)
    hasDividers = False
    i = 0
    while not hasDividers and i<len(dividers): 
        if dividers[i] in lista:
            hasDividers = True
        else: 
            i+=1    
    return hasDividers

def delete_numbers(num, lista):
    dividers = getDividers(num)
    lista.remove(num)
    for d in dividers: 
        if d in lista: 
            lista.remove(d)
    return lista

def anyLegal(lista):
    legal = False
    i = 0
    while i<len(lista) and not legal: 
        legal = hasDividersInList(lista[i], lista)
        i+=1
    return legal  

def isPrime(num):
    if len(getDividers(num))==1:
        return True
    else: 
        return False

def getBiggestPrime(lista):
    found = 0
    num = len(lista)
    while found==0:
        if isPrime(num):
            found = num
        else: 
            num -=1
    return found

def firstSolution(lista):
    n = len(lista)
    binaryList = [0]*n
    biggestPrime = getBiggestPrime(lista)
    lista = delete_numbers(biggestPrime, lista)
    binaryList[biggestPrime-1]=1
    while anyLegal(lista):
        if n in lista and hasDividersInList(n, lista):
            binaryList[n-1]=1
            lista = delete_numbers(n, lista)
        n -= 1
    return binaryList

def convertToTaken(binaryList):
    takenList = list()
    for i in range(len(binaryList)):
        if binaryList[i]==1:
            takenList.append(i+1)
    return takenList

def getScore(takenList):
    return sum(takenList)

def getRemadeList(lista, forbidden):
    n = len(lista)
    binaryList = [0]*n
    if forbidden!=getBiggestPrime(lista):
        biggestPrime = getBiggestPrime(lista)
        lista = delete_numbers(biggestPrime, lista)
        binaryList[biggestPrime-1]=1
    while anyLegal(lista) and n>1:
        if n!=forbidden and n in lista and hasDividersInList(n, lista):
            binaryList[n-1]=1
            lista = delete_numbers(n, lista)
        n -= 1
    return binaryList
    

def calcBestScore(binaryList, nlist, score):
    bestBinary = binaryList
    i = len(binaryList)
    while i>=1:
        if binaryList[i-1]==1:
            newBinary = getRemadeList(nlist.copy(), i)
            takenList = convertToTaken(newBinary)
            if score<getScore(takenList):
                score = getScore(takenList)
                bestBinary = newBinary
        i -= 1  
    return bestBinary


# Get all numbers from 1 to n
n = int(input("Select a number to play!\n"))
num_vector = list()
num_vectorStatic = list()
for i in range(1,n+1):
    num_vector.append(i)
    num_vectorStatic.append(i)
print(num_vector)

total_sum = 0
option = int(input("Do you want to play(1) or simulate the best game(2)? "))

if option == 1:

    while len(num_vector)>0 and anyLegal(num_vector):
        
        num = int(input("Select a number\n"))
        if hasDividersInList(num, num_vector):
            num_vector = delete_numbers(num, num_vector)
            total_sum += num
        else: 
            print("Not a legal number!")
        print(num_vector)
    print("Game finished! Score: " + str(total_sum))

if option == 2:
    best_combination = list()
    best_sum = 0
    binaryList = firstSolution(num_vector)
    takenList = convertToTaken(binaryList)
    bestScore = calcBestScore(binaryList, num_vectorStatic.copy(), getScore(takenList))
    takenList = convertToTaken(bestScore)
    print("Last solution: " + str(takenList))
    score = getScore(takenList)
    print("Bot's score: " + str(score))
    print("Taxman's score: " + str(sum(num_vectorStatic)-score))
