from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap ,QColor
import matplotlib.pyplot as plt

class HistogramDialog(QDialog):
    def __init__(self,main_window , image , modified_image):
        super().__init__(main_window)
        histogram_original = self.make_histogram(image)
        histogram_original.title('Imagem normal')
        histogram_modified = self.make_histogram(modified_image)
        histogram_modified.title("Imagem modificada")

    def make_histogram(self, image):
        qimage = image.pixmap().toImage()
        dict_gray_scale = {} 
        for x in qimage.height():
            for y in qimage.width():
                current_pixel = qimage.pixel(x,y)
                #como é cinza poderia ser qualquer uma das cores
                current_color = QColor(current_color).red() 
                dict_gray_scale[current_color] = dict_gray_scale.get(current_color,0) + 1
        plt.hist(x=dict_gray_scale,bins=10,color= "#607c8e" , rwidth = 0.9 )
        plt.xlabel("frequencia de pixels")
        plot = plt.ylabel("escala de cinza")
        return plot