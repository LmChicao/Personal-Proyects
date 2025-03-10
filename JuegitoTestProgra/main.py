import sys
import os 
import datetime
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
import threading
import time 

from back_end.loading_window import LoadingWindows

def f_current_time() :
    
    current_time = (datetime.datetime.now())
    time_in_format = current_time.strftime("%H:%M:%S.%f")[:-3]
    return time_in_format

class MainWindow(QWidget) :
    
    contador = 0
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 150, 1600, 900)
        self.setStyleSheet("background-color: #0ea1bf;")

        self.setWindowTitle('Testing')
        
        #Main Layout        
        self.MainLayout = QVBoxLayout(self)
        self.pantalla_carga = LoadingWindows()
        self.thread_pantalla_carga =  QThread(self.pantalla_carga)     
          
        self.MainLayout.addWidget(self.pantalla_carga)
        
        
    '''
    
    # qlabel contaor test
        
        
        self.QLabelcontador = QLabel(f"contaor : {self.contador}",self)
        self.botontest = QPushButton(self)
        self.botontest.clicked.connect(self.actualizar_contador)
        
        self.MainLayout.addWidget(self.QLabelcontador)
        self.MainLayout.addWidget(self.botontest)
        
    def actualizar_contador(self) :
        self.contador += 1 
        
        self.QLabelcontador.setText(f"contaor : {self.contador}")
    
    '''
        
    
        
        
        
        
        
    def change_interface(self, nueva_interfaz):
        '''
        This function deletes all the widgets that are in the LayoutPrincipal and directly deletes them.
        directly deletes them, the question for when it arrives to 0
        
        the takeAt takes the element that is placed inside in this case the first one
        the deleteLater deletes directly the existing widget and frees memory uwu
        
        Finally the new widget or assigned menu is added
        '''
        while self.MainLayout.count() > 0:
            item_widget = self.MainLayout.takeAt(0)
            widget = item_widget.widget()
            print(f"\n{f_current_time()} Interface : A widget of type {widget} has been deleted.")
            if widget:
                widget.deleteLater()
     
if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])  
    ventana = MainWindow()  
    ventana.show() 
    sys.exit(app.exec())
