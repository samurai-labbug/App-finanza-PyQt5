from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem, QDoubleSpinBox, QAbstractItemView
from PyQt5.QtCore import Qt
from datetime import date

# Constantes
ANCHO, ALTO = 700, 400 
WIN_TITLE = 'Project Finanzas pyqt5'
text_btn = 'Registrar'
text_input = ''
cabeceras = ["Fecha", "Descripción", "Monto"]
Informacion=[]
hoy=date.today()

# Calse Principal

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.config_window()
        self.set_window()
        self.show()

    def config_window(self):

        self.setWindowTitle(WIN_TITLE)
        self.resize(ANCHO, ALTO)

    def set_window(self):
        self.input_descripcion = QLineEdit()
        self.input_descripcion.setPlaceholderText('Descripción ')
        
        self.input_monto = QDoubleSpinBox()
        self.input_monto.setPrefix("$ ")
        self.input_monto.setRange(-9999999.9, 999999.0)
        self.input_monto.setDecimals(1)
        
        self.btn = QPushButton(text_btn, self)
        
        
        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.input_descripcion, stretch=1)
        self.top_layout.addWidget(self.input_monto, stretch=1)
        self.top_layout.addWidget(self.btn)
        

        self.tabla = QTableWidget(0, 3)
        
        
        self.tabla.setHorizontalHeaderLabels(cabeceras)
        
        # Comportamiento y restricciones de la tabla
        header = self.tabla.horizontalHeader()
        header.setSectionResizeMode(header.stretchGlue if hasattr(header, 'stretchGlue') else 1) 
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows) 
        
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.tabla)      

        
        self.setLayout(self.main_layout)

class Datos():
    def __init__(self, fecha, descripcion, monto):
        super().__init__()
        self.fecha= fecha
        self.descripcion = descripcion
        self.monto = monto
    
    def fecha(self):
        self.fecha= date.hoy()

def run():
    app = QApplication([])
    window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    run()
