import numpy as np
from PyQt5.QtGui import qRgb
#import pdb
#from PyQt5.QtCore import pyqtRemoveInputHook
from color_helper  import ColorHelper
class MaskReductionMethod():
    def __init__(self , mask):
        self.mask = mask
        self.linhas = self.mask.lines
        self.colunas = self.mask.columns
        self.actual_pixel_list = np.array([])
    def set_current_pixel(self , pixel): 
        self.actual_pixel_list = np.append( self.actual_pixel_list , [pixel])
    def get_transformed_pixel(self ):
        try:
            self.actual_pixel_list = self.actual_pixel_list.reshape(self.linhas , self.colunas)
        except ValueError as error:
            index = int(len(self.actual_pixel_list)/2)
            result = self.actual_pixel_list[index].rgb()
            self.actual_pixel_list = np.array([])
            return result
        red_sum , green_sum , blue_sum = 0,0,0
        for x in range(0 , len(self.actual_pixel_list )):
            for y in range(0 , len(self.actual_pixel_list[0] )):
                red_sum += self.actual_pixel_list[x][y].red()* self.mask.matrix[x][y]
                green_sum += self.actual_pixel_list[x][y].green()* self.mask.matrix[x][y]
                blue_sum += self.actual_pixel_list[x][y].blue()* self.mask.matrix[x][y]
        red_sum ,green_sum , blue_sum = ColorHelper.limit_color([red_sum ,green_sum , blue_sum])
        result = qRgb(red_sum , green_sum , blue_sum)
        self.actual_pixel_list = np.array([])
        return result 