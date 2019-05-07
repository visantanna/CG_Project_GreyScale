# -*- coding: utf-8 -*-
from noise_reduction_methods.base_reduction_method import BaseReductionMethod
from noise_reduction_methods.average_reduction_method import AverageReductionMethod
from noise_reduction_methods.median_reduction_method import MedianReductionMethod
from noise_reduction_methods.quantification_reduction_method import QuantificationReductionMethod
from noise_reduction_methods.mask_reduction_method import MaskReductionMethod
from noise_reduction_methods.double_sobel_method import DoubleSobelMethod
import numpy as np
from entities.mask_entity import MaskEntity
#import pdb
#from PyQt5.QtCore import pyqtRemoveInputHook
class FactoryNoiseReductionMethods():
    @staticmethod
    def instanciate_base_reduction(original_image , matrix ):
        mask = MaskEntity(matrix)
        reduction_method = MaskReductionMethod(mask)
        base = BaseReductionMethod(original_image  , mask , reduction_method)
        return base
    @staticmethod
    def get_method_class(method_name , original_image):
        base = BaseReductionMethod(original_image , MaskEntity(4)  )
        if(method_name == "média"):
            average_method = AverageReductionMethod()
            base.reduction_method = average_method
        elif(method_name == "mediana"):
            median_method = MedianReductionMethod()
            base.reduction_method =  median_method
        elif(method_name == "quantificação"):
            base = BaseReductionMethod(original_image , MaskEntity(0)  )
            quantification_method = QuantificationReductionMethod(3)
            base.reduction_method = quantification_method
        elif(method_name == "passa alta"):
            passa_alta_matrix = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
            base = FactoryNoiseReductionMethods.instanciate_base_reduction(original_image,passa_alta_matrix)
        elif(method_name == "sobel vertical"):
            sobel_vertical_matrix = [[-1,2,1],[0,0,0],[-1,-2,-1]]
            base = FactoryNoiseReductionMethods.instanciate_base_reduction(original_image,sobel_vertical_matrix)
        elif(method_name == "sobel horizontal"):
            sobel_horizontal_matrix = [[1,0,-1],[2,0,-2],[1,0,-1]]
            base = FactoryNoiseReductionMethods.instanciate_base_reduction(original_image,sobel_horizontal_matrix)
        elif(method_name == "gradiente horizontal"):
            gradient_operator_horizontal = [[-1,-1], [1,1] ]
            base = FactoryNoiseReductionMethods.instanciate_base_reduction(original_image,gradient_operator_horizontal)
        elif(method_name == "gradiente vertical"):
            gradient_operator_vertical = [[-1 , 1], [-1,1] ]
            base = FactoryNoiseReductionMethods.instanciate_base_reduction(original_image,gradient_operator_vertical)
        elif(method_name == "duplo sobel"):
            mask3x3= MaskEntity(1)
            base = BaseReductionMethod(original_image ,mask3x3 , DoubleSobelMethod() )
        else:
            base = None
        return base

       