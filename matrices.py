import numpy as np

mi = np.array([["O","X","X"],["O","X","O"],["X","X","O"]])
#print(mi)
##print(mi[2])
##print("----")


print( (mi[0] == ['X','X','X']) )

for i in range(3):    
    for j in range(3):
       if (mi[i][j] == "X"):
           #print("LO son")
           pass
