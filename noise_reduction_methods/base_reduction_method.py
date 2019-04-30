from PyQt5.QtGui import QColor , qRgb
import numpy as np
import time
import pdb
from PyQt5.QtCore import pyqtRemoveInputHook

class BaseReductionMethod():
    def __init__(self ,original_image , mask , reduction_method = None):
        self.original_image = original_image
        self.mask =  mask
        self.reduction_method = reduction_method

    def execute_noise_reduction(self ):
        start_time = time.time()
        cloned_image = self.original_image.copy()
        for x in range(0 , self.original_image.width()):
            for y in range(0 , self.original_image.height()):
                x_start_mask =  self.get_valid_x(x-self.mask)
                #range is exclusive in the end , so a got a "plus one" on the end_masks
                x_end_mask = self.get_valid_x(x+self.mask+1)
                y_start_mask = self.get_valid_y(y-self.mask)
                y_end_mask = self.get_valid_y(y+self.mask+1)
                for x_mask in range(x_start_mask , x_end_mask ):
                    for y_mask in range(y_start_mask, y_end_mask): 
                        current_pixel = self.original_image.pixelColor(x_mask, y_mask)
                        self.reduction_method.set_current_pixel(current_pixel)
                new_pixel = self.reduction_method.get_transformed_pixel()
                cloned_image.setPixel(x,y, new_pixel)
        print("Tempo de execução:" +  str(time.time()- start_time))
        return cloned_image

    def get_valid_x(self, x):
        if x > self.original_image.width():
            return self.original_image.width()
        elif x < 0:
            return 0
        else: 
            return x    
    def get_valid_y(self , y):
        if y > self.original_image.height():
            return self.original_image.height()
        elif y < 0:
            return 0
        else: 
            return y