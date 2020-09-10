import numpy as np

def predict(row,weights,bk):
    activation = bk
    for i in range(len(row)):
            activation += weights[i]*row[i]
    return 1 if activation >=0 else 0

'Question a'
dataset = [[0,0],[1,0],[0,1],[1,1]]
w = [1,1]
for row in dataset:
    AND=predict(row,w,-2)
    OR=predict(row,w,-1)
    print("Input:{0}   And:{1}      OR:{2}".format(row,AND,OR))

 'Question b'
from itertools import product
x5 = list(product([0,1],repeat = 5))
w5=[1,1,1,1,1]
for row in x5:
    AND=predict(row,w5,-2)
    OR=predict(row,w5,-1)
    print("Input:{0}   And:{1}      OR:{2}".format(row,AND,OR))
    
'Question c'
print("Number of inputs:")
n=input()
from itertools import product
xn = list(product([0,1],repeat = int(n)))
wn=np.ones(int(n))
for row in xn:
    AND=predict(row,wn,-2)
    OR=predict(row,wn,-1)
    print("Input:{0}   And:{1}      OR:{2}".format(row,AND,OR))
'Question d'
'''
Comment: according to the result from question b and c, I found out that the AND 
gate is only true when there is 2 inputs, otherwise it false. In order to work well with n inputs, bk must be equal -n.
For the OR gate, the bias does not need to be changed to be true in any number of input.
'''
