from PyQt5.QtGui import qRgb
import pdb
from PyQt5.QtCore import pyqtRemoveInputHook
class QuantificationReductionMethod():
    def __init__(self , qtd_color_levels):
        self.qtd_color_levels = qtd_color_levels
        self.ranges = self.create_ranges(self.qtd_color_levels)
        self.current_pixel = None

    def set_current_pixel(self , pixel): 
        red = pixel.red()
        green = pixel.green()
        blue = pixel.blue()
        self.current_pixel = qRgb(self.ranges[round(red/self.interval)]
            ,self.ranges[round(green/self.interval)] 
            ,self.ranges[round(blue/self.interval)])

    def get_transformed_pixel(self):
        return self.current_pixel

    def create_ranges(self, qtd_color_levels):
        qtd_intervals = qtd_color_levels-1
        self.interval = 255/qtd_intervals
        list_ranges = [0,255]
        for value in range(1 , qtd_intervals):
            list_ranges.append(int(self.interval*value))
        list_ranges = sorted(list_ranges)
        return list_ranges
