from settings import BOARD_LENGTH,VICTORY_STRIKE
from list_utils import *

class LinearBoard():
    """
    Clase que respresenta un tablero de una  sola columna
    x un jugador 
    o otro jugador
    None un espacio vacio
    """
    def __init__(self):
        """
        Una lista de None
        """
        self._column =[None for i in range(BOARD_LENGTH)]
        self.count_x = 0
        self.count_o = 0

    def add(self,char):
        """
        Juega en la priemra posición disponible
        """
        # Siempre y cuadno no este lleno...
        if not self.is_full():
            #bucamos la primera posición disponible
            i = self._column.index(None)
            
            #Sutituir el none por el char
            self._column[i] = char

        



        
    def is_full(self):
        #comprobar que ni esté vacío el array ni todo sean nones
        return self._column[-1]!= None
        
        """ 
        Mi versión:

        column = self._column
        
        for i in column:
            if i == None:
                return False
            else:
                return True
        """
    def is_victory(self,char):
        return find_streak(self._column,char,VICTORY_STRIKE)
       

        


        """
        for i in column:
        #contar el número de o y de x
            if i == char:
                x += 1
                # y ver quien llega antes al VICTORY_STRIKE seguidas
                if x == 3:
                    return True
                
            elif i == char:
                o += 1
                if o == 3:
                    # retornar el ganador 
                    return True

        """
       
        

        

    def is_tie(self,char1,char2):
        """No hay victoria ni e char ni de char 2"""
        return (self.is_victory("x")== False and (self.is_victory("o")== False))
