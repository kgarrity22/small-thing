
from pylab import *
import random
def create_matrix(n):

    #creating an empty list with n nested lists
    matrix = []
    for k in range(n+1):
        row = []
        matrix.append(row)
    
    #appending probabilities 
    for i in range(0, n+1):
        for j in range(0, n+1):
            if i == 0:
                if j == 1:
                    matrix[i].append(1)
                else:
                    matrix[i].append(0)
            elif j == 1 and i != n:
                matrix[i].append(0.5)
            elif i + 1 == j:
                matrix[i].append(0.5)
            elif i == n and j == n:
                matrix[i].append(1)
            else:
                matrix[i].append(0)

    final = array(matrix)
    return final

##create_matrix(6)
##create_matrix(7)



def transition(m, n):
    if m == 1:
        return n
    else:
        return n.dot(transition(m-1, n))
        
##n = create_matrix(7)
##print(transition(200, n))

def expected_tosses(n):
    matrix = create_matrix(n)
    I = array(eye(n))

    Q = []
    temp = []
    for i in range(len(matrix)):
        row = matrix[i][:n]
        temp.append(row)
    for j in range(0, len(temp)-1):
        Q.append(temp[j])

    Q = array(Q)
    
    N = inv(I - Q)
    print("first row of n: ", N[1])
    expected = sum(N[1])

    return expected

##print(expected_tosses(6))
##print(expected_tosses(7))

    

def tosses_until_N(n):

    flips = []
    toss = random.randint(0, 1)
    flips.append(toss)

    i = 1
    iterations = 0

    while i < n:
        new_toss = random.randint(0, 1)
        flips.append(new_toss)
        if new_toss == flips[iterations]:
            i += 1
        elif new_toss != flips[iterations]:
            i = 1
        iterations +=1
    
    return iterations

##x = 0
##for i in range(10000):
##    x = x + tosses_until_N(6)
##print("avg: ", x/10000)
##x = 0
##for i in range(10000):
##    x = x + tosses_until_N(7)
##print("avg: ", x/10000)


    
# function for creating the matrix for number 7 
def new_create_matrix(n):
    
    matrix = []
    for k in range(1, n+1):
        row = []
        matrix.append(row)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == 1:
                matrix[i-1].append(0.5)
            elif i + 1 == j:
                matrix[i-1].append(0.5)
            elif i == n and j == n:
                matrix[i-1].append(0.5)
            else:
                matrix[i-1].append(0)
    
    final = array(matrix)
    return final

##x = new_create_matrix(6)
##print(transition(5, x))

def state_proportions(n):

    flips = []
    toss = random.randint(0, 1)
    flips.append(toss)

    counter = []
    for k in range(n):
        counter.append(0)
        # now we will add 1 to the i-1 index

    i = 1
    iterations = 0

    while i <= n:
        new_toss = random.randint(0, 1)
        flips.append(new_toss)
        if new_toss == flips[iterations]:
            counter[i-1] +=1
            i += 1
        elif new_toss != flips[iterations]:
            counter[i-1] +=1
            i = 1
        iterations +=1

    return counter


# number 8 calculations
row1 = 0
row2 = 0
row3 = 0
row4 = 0
row5 = 0
row6 = 0
for i in range(1000):
    row1 = row1 + (state_proportions(6))[0]
    row2 = row2 + (state_proportions(6))[1]
    row3 = row3 + (state_proportions(6))[2]
    row4 = row4 + (state_proportions(6))[3]
    row5 = row5 + (state_proportions(6))[4]
    row6 = row6 + (state_proportions(6))[5]


print("avg for row1", row1/1000)
print("avg for row2", row2/1000)
print("avg for row3", row3/1000)
print("avg for row4", row4/1000)
print("avg for row5", row5/1000)
print("avg for row6", row6/1000)
    
x = row1/1000 + row2/1000 + row3/1000 + row4/1000 + row5/1000 + row6/1000
print("probabilities: ")
print("row1:", (row1/1000)/x)
print("row2:", (row2/1000)/x)
print("row3:", (row3/1000)/x)
print("row4:", (row4/1000)/x)
print("row5:", (row5/1000)/x)
print("row6:", (row6/1000)/x)

   
