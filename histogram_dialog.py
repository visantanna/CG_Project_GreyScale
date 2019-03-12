from PyQt5.QtWidgets import QDialog , QLabel
from PyQt5.QtGui import QPixmap ,QColor , QImage
import matplotlib.pyplot as plt

class HistogramDialog(QDialog):
    def __init__(self,main_window , image , modified_image):
        super().__init__(main_window)
        self.setMinimumSize(1000,400)
        hist_original = QLabel(self)
        hist_modified = QLabel(self)
        label_hist_original = QLabel("Original",self)
        label_hist_original.move(220,20)
        label_hist_modified = QLabel("Modificado",self)
        label_hist_modified.move(700,20)
        hist_original.resize(450,360)
        hist_modified.resize(450,360)
        hist_original.move(20,50)
        hist_modified.move(500,50)
        self.make_histogram(image, True)
        self.make_histogram(modified_image, False)
        hist_original.setPixmap(QPixmap("original.png").scaledToHeight(350))
        hist_modified.setPixmap(QPixmap("modified.png").scaledToHeight(350))
        self.show()

    def make_histogram(self, image , original):
        qimage = image.pixmap().toImage()
        dict_gray_scale = {} 
        for x in range(0,qimage.width()):
            for y in range(0, qimage.height()):
                current_pixel = qimage.pixel(x,y)
                #como é cinza poderia ser qualquer uma das cores
                current_color = QColor(current_pixel).red() 
                dict_gray_scale[current_color] = dict_gray_scale.get(current_color,0) + 1
        plt.hist(x=list(dict_gray_scale.keys()),weights =list(dict_gray_scale.values()),bins=20 ,range = [0,256] )
        plt.xlabel("escala de cinza")
        plt.ylabel("frequencia de pixels")
        if original:
            plt.savefig('original.png')
        else:
            plt.savefig('modified.png')
        plt.clf()
        plt.cla()
        plt.close()
        return 