from PyQt5.QtGui import qRgb , QColor
class ColorHelper():
    @staticmethod
    #value can be a int or a list[3] int
    def limit_color(value):
        if isinstance(value , int):
            return ColorHelper.__get_limited_color__(value)
        elif isinstance(value , list):
            new_list = [ColorHelper.__get_limited_color__(color) for color in value]
            return new_list
        else:
            raise("Invalid argument for value in ColorLimiter:" + str(value))

    @staticmethod
    def __get_limited_color__(color):
        if(color > 255):
            return 255
        elif(color < 0):
            return 0
        else: 
            return color
    @staticmethod
    def sum_pixels(pixel1,pixel2):
        pixel1_rgb = QColor(pixel1)
        pixel2_rgb = QColor(pixel2)
        new_rgb = [pixel1_rgb.red() + pixel2_rgb.red(),
                   pixel1_rgb.green() + pixel2_rgb.green() ,
                   pixel1_rgb.blue() + pixel2_rgb.blue() ]
        red , green , blue = ColorHelper.limit_color(new_rgb)
        return qRgb(red , green , blue)