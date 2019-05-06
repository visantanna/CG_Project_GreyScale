import math
import numpy as np
class MaskEntity():
    #receives a 2 dimension array and returns a mask
    def __init__( args ):
        self.left = None
        self.right = None
        self.up = None
        self down = None
        if type(args) is int:
            dimension_size = args*2 + 1
            matrix = np.zeros((dimension_size , dimension_size) , dtype = numpy.int8 ).tolist() 
            self.left , self.right , self.up , self down = [dimension_size]*4
        elif type(matrix) is list:
            if type(matrix[0]) is list:
                self.matrix = args
                vertical_length = len(matrix)
                horizontal_length = len(matrix[0])
                self.left , self.right = self.break_into_two(horizontal_length)
                self.up , self down = self.break_into_two(vertical_length)
            else: 
                raise Exception(" Atributo para classe 'Mask' precisa ser uma matrix (2D array:  list[list]) ou um inteiro ")    
        else:
            raise Exception(" Atributo para classe 'Mask' precisa ser uma matrix (2D array:  list[list]) ou um inteiro")

    def break_into_two(size_of_line):
        value1, value2 = 0, 0
        size_without_central_pixel
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
        return value1 , value2
