# -*- coding: utf-8 -*-
from noise_reduction_methods.base_reduction_method import BaseReductionMethod
from noise_reduction_methods.average_reduction_method import AverageReductionMethod
from noise_reduction_methods.median_reduction_method import MedianReductionMethod
from noise_reduction_methods.quantification_reduction_method import QuantificationReductionMethod
from noise_reduction_methods.mask_reduction_method import MaskReductionMethod
import numpy as np
class FactoryNoiseReductionMethods():
    @staticmethod
    def get_method_class(method_name , original_image):
        base = BaseReductionMethod(original_image , 4  )
        if(method_name == "média"):
            average_method = AverageReductionMethod()
            base.reduction_method = average_method
        elif(method_name == "mediana"):
            median_method = MedianReductionMethod()
            base.reduction_method =  median_method
        elif(method_name == "quantificação"):
            base = BaseReductionMethod(original_image , 0  )
            quantification_method = QuantificationReductionMethod(3)
            base.reduction_method = quantification_method
        elif(method_name == "máscara"):
            base = BaseReductionMethod(original_image , 1  )
            #mask_passa_alta = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
            #mask_sobel_vertical = [[-1,2,1],[0,0,0],[-1,-2,-1]]
            #mask_sobel_horizontal = [[1,0,-1],[2,0,-2],[1,0,-1]]
            #mask_gradient_operator_horizontal = [[0,-1,-1], [0,1,1] , [0,0,0] ]
            mask_gradient_operator_vertical = [[0,-1 , 1], [0,-1,1] , [0,0,0]]
            mask_method = MaskReductionMethod(mask_gradient_operator_vertical)
            base.reduction_method = mask_method
        elif(method_name == "intregral de borda"):
            base = BaseReductionMethod(original_image , 1  )
            mask_method = MaskReductionMethod(mask_sobel_horizontal)
        else:
            base = None
        return base