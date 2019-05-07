import math
import numpy as np
class MaskEntity():
    #receives a 2 dimension array and returns a mask
    def __init__( self , args ):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.lines = None 
        self.columns = None
        if type(args) is int:
            dimension_size = args*2 + 1
            self.lines = dimension_size
            self.columns = dimension_size
            matrix = np.zeros((dimension_size , dimension_size) , dtype = np.int8 ).tolist() 
            self.left , self.right , self.up , self.down = [dimension_size]*4
        elif type(args) is list:
            if type(args[0]) is list:
                self.matrix = args
                vertical_length = len(self.matrix)
                horizontal_length = len(self.matrix[0])
                self.columns = horizontal_length
                self.lines  = vertical_length
                self.left , self.right = self.break_into_two(horizontal_length)
                self.up , self.down = self.break_into_two(vertical_length)
                print("valor left: " + str(self.left ))
            else: 
                raise Exception(" Atributo para classe 'Mask' precisa ser uma matrix (2D array:  list[list]) ou um inteiro ")    
        else:
            raise Exception(" Atributo para classe 'Mask' precisa ser uma matrix (2D array:  list[list]) ou um inteiro")

    def break_into_two(self, size_of_line):
        value1, value2 = 0, 0
        size_without_central_pixel = size_of_line -1
        if size_without_central_pixel % 2 == 0:
            if (size_of_line == 1 ): 
                value1 = 0
                value2 = 0
            else:
                value1 = size_without_central_pixel/2
                value2 = size_without_central_pixel/2
        else:
            value1 = math.floor(size_without_central_pixel/2)
            value2 = math.ceil(size_without_central_pixel/2)
        return int(value1) , int(value2)
