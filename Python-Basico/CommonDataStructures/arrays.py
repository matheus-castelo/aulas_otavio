import array
# Arrays (Listas) são DINÂMICOS por default, então podemos usar como STACK.

def printArray(arr):
    print(arr)

def appendValue(arr, value):
    arr.append(value)
    print(arr)

def popValue(arr):
    arr.pop()
    print(arr)

def insertAtStart(arr, value):
    arr.insert(0, value)
    print(arr)

def changeFirstElement(arr, value):
    arr[0] = value  # Não reclama 
    print(arr)

def printLength(arr):
    print(len(arr))

def createArrayWithZeros(n):
    arrayZero = [0] * n
    print(arrayZero)
    print(len(arrayZero))
    return arrayZero

def slicingExample(arrayZero):
    # Slicing
    print("SLICING")
    arrayZero[4] = "TESTE"
    print(arrayZero)
    print(arrayZero[0:4])  # Começa do 0 e não inclui o 4

####################################### Looping Arrays
# With index
def printArrayWithIndex(arr):
    for i in range(len(arr)):
        print(arr[i])

# Without index
def printArrayWithoutIndex(arr):
    for item in arr:
        print(item)

# With index and value
def printArrayWithIndexAndValue(arr):
    for i, n in enumerate(arr):
        print(i, n)


#######################################################################################################
print("--- ARRAYS - MÉTODOS BÁSICOS --- ")
arr = [1, 2, 3]
printArray(arr)

appendValue(arr, 4)
popValue(arr)

insertAtStart(arr, 0)
changeFirstElement(arr, "Teste")  # Não reclama

printLength(arr)

n = 100
arrayZero = createArrayWithZeros(n)
print("--- Slicing Array Example --- ")
slicingExample(arrayZero)

print("--- Slicing Array With Index --- ")
printArrayWithIndex(arr)

print("--- Slicing Array Without Index --- ")
printArrayWithoutIndex(arr)

print("--- Slicing Array With Index and Values (Enumerate)--- ")
printArrayWithIndexAndValue(arr)

########################################## UNPACKING and ZIP ############################################
num1 = [1,2,3]
num2 = [4,5,6]
def zipArrays(num1, num2):
    for n1,n2 in zip(num1,num2):
        print(n1,n2)

print("--- Ziping Arrays --- ")
zipArrays(num1,num2)

# You also have REVERSE and SORT methods
arrayNomes = ["Nome muito grande AAA", "Otavio", "Joao", "Cirineu", "Joao Claudio", "A", "Z", "B", "Y"]
print(arrayNomes)
arrayNomes.sort(key=lambda x:len(x))
print(arrayNomes)

arrayNomes.sort()
print(arrayNomes)

arrayNomes.sort(reverse=True)
print(arrayNomes)


###################3######### LIST COMPREHENSIONS ################################################
print("--- List Comprehensions ---")
arrayCrescente = [i for i in range(100)]
print(arrayCrescente)

# 2-D Lists
print("--- 2-D Arrays w/ List Comprehensions ---")
arrayDoisD = [[0] *4 for i in range(5)]
print(arrayDoisD)

