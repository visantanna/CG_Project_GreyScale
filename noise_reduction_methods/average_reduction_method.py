from PyQt5.QtGui import qRgb
import numpy as np
from noise_reduction_methods.base_reduction_method import BaseReductionMethod


class AverageReductionMethod(BaseReductionMethod):
    def __init__(self):
        self.qtd_analized_pixels = 0 
        self.rgb_array = [0,0,0]

    def set_current_pixel(self, current_pixel):
        self.qtd_analized_pixels += 1
        self.rgb_array[0] += current_pixel.red()
        self.rgb_array[1] += current_pixel.green()
        self.rgb_array[2] += current_pixel.blue()

    def get_transformed_pixel(self):
        new_pixel_rgb = np.true_divide(self.rgb_array, self.qtd_analized_pixels)
        self.qtd_analized_pixels = 0 
        self.rgb_array = [0,0,0]
        new_pixel = qRgb(new_pixel_rgb[0] ,new_pixel_rgb[1] , new_pixel_rgb[2])
        return new_pixel
