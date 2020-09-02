#funcion que calcula el minimo comun multiplo de dos numeros

def mcm(num1, num2):
    i = 1
    # Listas que almacenan los multiplos de cada numero
    list1 = list()
    list2 = list()
    
    while (True):
        list1.append(num1*i)
        list2.append(num2*i)
        if ( (num1*i in list2)) :
             return list1[i-1]
        if ( (num2*i in list1)):
            return list2[i-1]
            
        i+=1    


print(mcm(32,50))