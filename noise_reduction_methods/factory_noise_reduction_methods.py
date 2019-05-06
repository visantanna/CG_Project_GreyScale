# -*- coding: utf-8 -*-
from noise_reduction_methods.base_reduction_method import BaseReductionMethod
from noise_reduction_methods.average_reduction_method import AverageReductionMethod
from noise_reduction_methods.median_reduction_method import MedianReductionMethod
from noise_reduction_methods.quantification_reduction_method import QuantificationReductionMethod
from noise_reduction_methods.mask_reduction_method import MaskReductionMethod
import numpy as np
import entities.mask_entity import MaskEntity
class FactoryNoiseReductionMethods():
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
            mask_passa_alta = MaskReductionMethod( MaskEntity(passa_alta_matrix))
            base = BaseReductionMethod(original_image  , mask_passa_alta )
        elif(method_name == "sobel vertical"):
            sobel_vertical_matrix = [[-1,2,1],[0,0,0],[-1,-2,-1]]
            mask_sobel_vertical = MaskReductionMethod(MaskEntity(sobel_vertical_matrix))
            base = BaseReductionMethod(original_image  , mask_sobel_vertical )
        elif(method_name == "sobel horizontal"):
            sobel_horizontal_matrix = [[1,0,-1],[2,0,-2],[1,0,-1]]
            mask_sobel_horizontal = MaskReductionMethod(MaskEntity(sobel_horizontal_matrix))
            base = BaseReductionMethod(original_image  , mask_sobel_horizontal )
        elif(method_name == "gradiente horizontal"):
            gradient_operator_horizontal = [[-1,-1], [1,1] ]
            mask_gradient_horizontal = MaskReductionMethod(MaskEntity(gradient_operator_horizontal))
            base = BaseReductionMethod(original_image  , mask_gradient_horizontal )
        elif(method_name == "gradiente horizontal"):
            gradient_operator_vertical = [[-1 , 1], [-1,1] ]
            mask_gradient_vertical = MaskReductionMethod(MaskEntity(gradient_operator_vertical))
            base = BaseReductionMethod(original_image  , mask_gradient_vertical )
        elif(method_name == "duplo sobel"):
            
        else:
            base = None
        return base