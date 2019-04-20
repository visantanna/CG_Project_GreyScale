from noise_reduction_methods.base_reduction_method import BaseReductionMethod
from noise_reduction_methods.average_reduction_method import AverageReductionMethod
from noise_reduction_methods.median_reduction_method import MedianReductionMethod
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
        else: 
            base = None
        return base