import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLabel   
import time
import os


class LoadingWindows(QWidget) :
    
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #0ea1bf;")
    
        # Main Layout Loading Window 
        self.main_loyut_LW = QVBoxLayout(self)
        # Text test
        self.label_text_test = QLabel("PANTALLA DE CARGA",self)
        self.label_text_test.setStyleSheet("font-size: 30px; background-color: #84D8FF; color: black;")
        self.main_loyut_LW.addWidget(self.label_text_test)
        
        #--------------------------------------------------------
        # Separador 
        self.Layout1V = QVBoxLayout(self)
        self.main_loyut_LW.addLayout(self.Layout1V)
        # Separador
        self.Layout2V = QVBoxLayout(self)
        self.main_loyut_LW.addLayout(self.Layout2V)
        # Separador
        self.Layout3V = QVBoxLayout(self)
        self.main_loyut_LW.addLayout(self.Layout3V)
        # Separador
        self.Layout4V = QVBoxLayout(self)
        self.main_loyut_LW.addLayout(self.Layout4V)
        # Separador Label 
        self.labeltestL1V = QLabel("",self)
        self.Layout1V.addWidget(self.labeltestL1V)        
        # Separador Label
        self.labeltest2V = QLabel("", self)
        self.Layout2V.addWidget(self.labeltest2V)        
        # Separador Label
        self.labeltest3V = QLabel("", self)
        self.Layout2V.addWidget(self.labeltest3V)        
        # Separador Label
        self.labeltest4V = QLabel("", self)
        self.Layout2V.addWidget(self.labeltest4V)
        #--------------------------------------------------------
    
        self.cosas_por_cargar = 1 
        
    def check_list(self) -> int :
        
        valor_return = 0 #Minimo o
        
        
        
        return valor_return   
        

        
        
        
        