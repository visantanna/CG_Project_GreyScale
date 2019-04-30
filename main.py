# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QMainWindow , QFileDialog , QLabel ,QGridLayout , QSpinBox
from PyQt5.QtGui import QPixmap ,QColor
from histogram_dialog import HistogramDialog
from PyQt5.QtWidgets import QComboBox
from noise_reduction_methods.factory_noise_reduction_methods import FactoryNoiseReductionMethods

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500,385)
        self.imported_image = QLabel(self)
        self.modified_image = QLabel(self)
        self.search_image_button = QPushButton("Selecione a Imagem",self)
        self.search_image_button.move(20,340)
        self.search_image_button.setMinimumSize(160,30)
        self.bright_button = QPushButton("ajustar brilho",self)
        self.bright_button.setVisible(False)
        self.bright_button.move(200,340)
        self.reduction_combobox = QComboBox(self)
        self.reduction_combobox.move(140 ,385)
        self.spinner_brightness = QSpinBox(self)
        self.reduction_combobox.setVisible(False)
        self.spinner_brightness.setMinimumSize(80,30)
        self.spinner_brightness.setMaximum(255)
        self.spinner_brightness.setMinimum(-255)
        self.spinner_brightness.setMinimumSize(60,30)
        self.spinner_brightness.move(370, 340)
        self.spinner_brightness.setVisible(False)
        self.spinner_label = QLabel("brilho: ",self)
        self.spinner_label.move(320,340)
        self.spinner_label.setMinimumSize(60 ,30)
        self.spinner_label.setVisible(False)
        self.histogram_generator = QPushButton("Gerar histograma de cinza",self)
        self.histogram_generator.setVisible(False)
        self.histogram_generator.setMinimumSize(215 ,30)
        self.histogram_generator.move(260, 385)
        self.label_noise_reduction = QLabel("Tipo Suavização:",self)
        self.label_noise_reduction.setMinimumSize(110 ,30)
        self.label_noise_reduction.move(20 ,385)
        self.setWindowTitle("GreyScale Project")
        self.search_image_button.clicked.connect(self.search_image_clicked)
        self.bright_button.clicked.connect(self.bright_button_clicked)
        self.histogram_generator.clicked.connect(self.generate_histogram)
        self.reduction_combobox.currentTextChanged.connect(self.combobox_action)
        self.show()

    def search_image_clicked(self):
        file_name,_ = QFileDialog.getOpenFileName(self, 'Open file', './', 'Image Files(*.png *.jpg *.jpeg *.bmp )' )
        if file_name:
            image = QPixmap(file_name)
            image = image.scaledToHeight(300)
            self.imported_image.setPixmap(image)
            self.imported_image.show()
            self.imported_image.resize(image.width(), image.height())
            self.imported_image.move(20,20)
            if not self.bright_button.isVisible():
                self.bright_button.setVisible(True)
            self.setMinimumSize(image.width() * 2 + 60 , 425)
            self.setMaximumSize(image.width() * 2 + 60 , 425)
            self.modified_image.setPixmap(image)
            self.modified_image.resize(image.width(), image.height())
            self.modified_image.move(image.width()+40,20)
            self.modified_image.show()
            self.spinner_brightness.show()
            self.spinner_label.show()
            self.histogram_generator.show()
            self.reduction_combobox.show()
            if(self.reduction_combobox.count() <= 0 ):
                self.add_combo_itens(self.reduction_combobox)


    def bright_button_clicked(self):
        constant = self.spinner_brightness.value()
        qimage = self.imported_image.pixmap().toImage()
        for x in range(0 , qimage.width()):
            for y in  range(0 , qimage.height()):
                current_pixel =  qimage.pixel(x,y)
                cur_color = QColor(current_pixel)
                red = self.adjust_to_limit(cur_color.red() + constant)
                green = self.adjust_to_limit(cur_color.green() + constant)
                blue = self.adjust_to_limit(cur_color.blue() + constant)
                value = QColor(red,green,blue)
                qimage.setPixel(x,y,value.rgb())
        new_pixmap = QPixmap.fromImage(qimage)
        self.modified_image.setPixmap(new_pixmap)

    def combobox_action(self ):
        method = None 
        new_pixmap = None
        item_selected = self.reduction_combobox.currentText()
        valid_arguments = ["média" , "mediana", "quantificação", "máscara"]
        argument = item_selected.lower()
        if argument in valid_arguments:
            method =FactoryNoiseReductionMethods().get_method_class(argument , self.imported_image.pixmap().toImage())
            new_reducted_image = method.execute_noise_reduction()
            new_pixmap = QPixmap.fromImage(new_reducted_image)
            self.modified_image.setPixmap(new_pixmap)
        print("pronto")

    def generate_histogram(self):
        dialog = HistogramDialog(self, self.imported_image ,self.modified_image) 
        dialog.show()

    def adjust_to_limit(self, value ):
        if value > 255:
            return 255
        elif value < 0:
            return 0
        else:
            return value

    def add_combo_itens(self, combo):
        combo.addItem("Selecione")
        combo.addItem("Média")
        combo.addItem("Mediana")
        combo.addItem("Quantificação")
        combo.addItem("Máscara")
        combo.setCurrentIndex(0)

if __name__ == "__main__":
    application = QApplication([])
    main = Main()
    main.show()
    sys.exit(application.exec_())