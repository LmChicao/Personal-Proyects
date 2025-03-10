import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout

import datetime
from PyQt5.QtCore import pyqtSignal, QObject

def f_current_time() :
    
    current_time = (datetime.datetime.now())
    time_in_format = current_time.strftime("%H:%M:%S.%f")[:-3]
    return time_in_format


class MainWindow(QWidget) :
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(-800, 450, 400, 500)
        self.setStyleSheet("background-color: ;")
        self.setWindowTitle('Testing')
        
        #Main Layout        
        self.MainLayout = QVBoxLayout(self)
        
    
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
