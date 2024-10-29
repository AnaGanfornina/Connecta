def find_one_2(list,needle):
    """
    Devuelve True si detecta la presencia de una  o mas
    isntancia del elemento needle dentro de una lista en 
    cualquier posición
    """
    result = False
    if list == []:
        return result
    
    for item in list:
        if item == needle:
            result = True
            return result 
        
    return result
"""
Mio:
def find_n(list,needle,num):
"""
"""
    Devuelve True si encuentra n o más ocurrencias de needle indicado en list
    False si  hay menos o si el n<0
    """
"""
    found = False
    index = 0
    count = 0

    while not found and index < len(list): 
        if needle == list[index]:
            count += 1

            if count >= num:
                found = True 

        index += 1
    

    return found 
"""

def find_n(list,needle,n):
    """
    Devuelve True si en lista hay n o más ocurrenciasd e needle
    False si hay menos o si n<0
    """
    #si n > 0 ...
    if n >= 0:
        
    #Inicializamos el índice y el contador
        index = 0
        count = 0

        #mientra no hayamos encontrado al elemento n veces o no hayamos terminado la lista...
        while count < n and index < len(list):
            #si lo encontramos, acutalizamos contador
            if needle == list[index]:
                count += 1
            #avanzamos al siguiente elemento
            index += 1
        #Devolvemos el resultado de comparar  contador con n
        return count >= n
    else:
        return False


def find_one(list,needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle en list
    """
    return find_n(list,needle,1)

def find_streak(list,needle,n):
    """
    Devuelve true si existe el needle n veces seguidas.
    """
    if n >= 0:
        index = 0
        count = 0
        streak = False

        #cuando count < n and index < len(list):
        while count < n and index < len(list):
        #Si encuentra un needle en la lista..
            if needle == list[index]:
                
                #pone el streak en True
                streak = True
                count += 1
                
            else:
                #si no lo encuentra..
                #el steak pasa a false y el count a 0
                streak = False
                count = 0
            index += 1
        return count >= n and streak == True
    else:
        return False

        



