import os

def counting() : # Falta terminarlo
    
    '''
    Falta terminar, porque si agrego layouts estos tendran su textura asignada, audio asignado y npc
    entonces tengo que hacerlo en base a los layouts, ademas de que, deberia tener una lista de los layouts creados y organizados
    
    '''
    
    
    actual_dir = os.path.dirname(os.path.abspath(__file__))
    dict_dummy = {}
    
    utils_dir = os.path.join(actual_dir, "utils")

    for item in os.listdir(utils_dir) :        
        item_dir = os.path.join(utils_dir, item) 
        
        dict_dummy[item] = []        
        
        if os.listdir(item_dir) == [] :             
            dict_dummy[item] = []
        
        else :            
            for item2 in os.listdir(item_dir) :                  
                
                dict_dummy[item].append(item2)
    
    for i in dict_dummy :
        print(i,  dict_dummy[i])
                



        
counting()