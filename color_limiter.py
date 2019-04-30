class ColorLimiter():
    @staticmethod
    #value can be a int or a list[3] int
    def limit_color(value):
        if isinstance(value , int):
            return ColorLimiter.__get_limited_color__(value)
        elif isinstance(value , list):
            new_list = [ColorLimiter.__get_limited_color__(color) for color in value]
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