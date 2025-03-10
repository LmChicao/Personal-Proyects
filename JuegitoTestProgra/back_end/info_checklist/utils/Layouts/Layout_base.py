
class Layout :
    
    def __init__(self):
        
        self.texturas = [] # lista de  "Nombre_Textura" 
        self.audios = [] # Lista de "Nombre_Audio"
        
        self.type = "small"
        '''
        small = 5x5 (0 -> 4 index)
        medium = 8x8 (0 -> 7 index)
        large = 10x10 (0 -> 9 index)
        '''
        
        self.posicion_objects = {# key = object / value = posicion
        
            "rock" : -1
            
            } 
        
        self.verificacion_items()
        
    def verificacion_items(self) :
        
        lista_cosas_to_delete = []
        
        if self.type == "small" :                            
            for i in self.posicion_objects :                
                if self.posicion_objects[i] < 0 :                                        
                    lista_cosas_to_delete.append([i, self.posicion_objects[i]])                                                       
                elif self.posicion_objects[i] > 4 :                    
                    lista_cosas_to_delete.append([i, self.posicion_objects[i]])
                    
        elif self.type == "medium" :                            
            for i in self.posicion_objects :                
                if self.posicion_objects[i] < 0 :                    
                    del self.posicion_objects[i]                
                elif self.posicion_objects[i] > 7 :                    
                    del self.posicion_objects[i]
                    
        elif self.type == "large" :                            
            for i in self.posicion_objects :                
                if self.posicion_objects[i] < 0 :                    
                    del self.posicion_objects[i]                
                elif self.posicion_objects[i] > 9 :                    
                    del self.posicion_objects[i]                
                   
        if lista_cosas_to_delete != [] :                        
            for i in lista_cosas_to_delete :
                print(i)
                
                del self.posicion_objects[i[0]]
        


Layout()