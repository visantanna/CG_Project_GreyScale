from PyQt5.QtGui import qRgb

class MedianReductionMethod():
    def __init__(self):
        self.list_of_pixels = []
    
    def set_current_pixel(self , pixel):  
        self.list_of_pixels.append(pixel)
    
    def get_transformed_pixel(self ):
        red_list , green_list ,blue_list  = [] , [] , []
        for pixel in self.list_of_pixels:
            red_list.append(pixel.red())
            green_list.append(pixel.green())
            blue_list.append(pixel.blue())
        red_list = sorted(red_list)
        green_list = sorted(green_list)
        blue_list = sorted(blue_list)
        index = int(len(self.list_of_pixels)/2)
        self.list_of_pixels = []
        new_pixel = qRgb(red_list[index],green_list[index] , blue_list[index])
        return new_pixel