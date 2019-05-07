from noise_reduction_methods.mask_reduction_method import MaskReductionMethod
from entities.mask_entity import MaskEntity
from color_helper import ColorHelper
class DoubleSobelMethod():
    def __init__(self ):
        self.matrix_sobel_vertical = [[-1,2,1],[0,0,0],[-1,-2,-1]]
        self.matrix_sobel_horizontal = [[1,0,-1],[2,0,-2],[1,0,-1]]
        self.mask_sobel_vertical = MaskReductionMethod(MaskEntity(self.matrix_sobel_vertical))
        self.mask_sobel_horizontal = MaskReductionMethod(MaskEntity(self.matrix_sobel_horizontal))
    
    def set_current_pixel(self , pixel):
        self.mask_sobel_vertical.set_current_pixel(pixel)
        self.mask_sobel_horizontal.set_current_pixel(pixel)
    
    def get_transformed_pixel(self):
        vertical_sobel_pixel =  self.mask_sobel_vertical.get_transformed_pixel()
        horizontal_sobel_pixel = self.mask_sobel_horizontal.get_transformed_pixel()
        pixel = ColorHelper.sum_pixels(vertical_sobel_pixel , horizontal_sobel_pixel)
        return pixel