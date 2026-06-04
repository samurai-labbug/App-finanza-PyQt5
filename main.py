import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, 
                             QTableWidgetItem, QDoubleSpinBox, QAbstractItemView, 
                             QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from datetime import date

# --- Configuración global ---
ANCHO, ALTO = 800, 500 
WIN_TITLE = 'App de Finanzas Personales'
cabeceras = ["Fecha", "Descripción", "Monto"]

# --- Estilos para los botones (CSS) ---
ESTILO_BOTON = """
    QPushButton {
        background-color: #0078D7;
        color: white;
        border-radius: 5px;
        padding: 8px;
        font-weight: bold;
        font-size: 12px;
    }
    QPushButton:hover {
        background-color: #005a9e;
    }
    QPushButton:pressed {
        background-color: #004275;
    }
"""

ESTILO_BOTON_EDITAR = """
    QPushButton {
        background-color: #F57C00;
        color: white;
        border-radius: 5px;
        padding: 8px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #ef6c00;
    }
    QPushButton:disabled {
        background-color: #BDBDBD;
        color: #757575;
    }
"""

ESTILO_BOTON_BORRAR = """
    QPushButton {
        background-color: #D32F2F;
        color: white;
        border-radius: 5px;
        padding: 8px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #b71c1c;
    }
"""

# --- Clase simple para el registro ---
class RegistroFinanza:
    def __init__(self, fecha, descripcion, monto):
        self.fecha = fecha
        self.descripcion = descripcion
        self.monto = monto

# --- Ventana Principal ---
class FinanzasApp(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):  # <-- Corregido aquí
        super().__init__(parent=parent, flags=flags)

        self.lista_registros = [] 
        self.fila_seleccionada = -1 

        self.config_window()
        self.UI_setup()
        self.show()

    def config_window(self):
        self.setWindowTitle(WIN_TITLE)
        self.resize(ANCHO, ALTO)
        self.setStyleSheet("background-color: #2E3A1F;")

    def UI_setup(self):
        # --- 1. Inputs (Arriba) ---
        self.lbl_descripcion = QLabel("Descripción:")
        self.lbl_descripcion.setStyleSheet("color: #FFFFE0; font-family: Comic Sans MS; font-size: 14px; font-weight: bold;")
        self.lbl_descripcion.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        
        self.input_desc = QLineEdit()
        self.input_desc.setPlaceholderText('Ej: Compra Supermercado')
        self.input_desc.setStyleSheet("padding: 5px; font-size: 12px; border-radius: 3px;")
        
        self.lbl_monto = QLabel("Monto:")
        self.lbl_monto.setStyleSheet("color: #FFFFE0; font-family: Comic Sans MS; font-size: 14px; font-weight: bold;")
        self.lbl_monto.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        
        self.input_monto = QDoubleSpinBox()
        self.input_monto.setPrefix("$ ")
        self.input_monto.setRange(-9999999.99, 9999999.99)
        self.input_monto.setDecimals(2)
        self.input_monto.setStyleSheet("padding: 5px; font-size: 12px; border-radius: 3px;")
        
        # Botones
        self.btn_registrar = QPushButton("REGISTRAR")
        self.btn_registrar.setStyleSheet(ESTILO_BOTON)
        self.btn_registrar.clicked.connect(self.gestionar_click_registrar)

        self.btn_editar = QPushButton("✎ EDITAR")
        self.btn_editar.setStyleSheet(ESTILO_BOTON_EDITAR)
        self.btn_editar.setEnabled(False) 
        self.btn_editar.clicked.connect(self.cargar_datos_en_inputs)

        self.btn_limpiar = QPushButton("LIMPIAR")
        self.btn_limpiar.setStyleSheet("QPushButton { background-color: #606060; color: white; border-radius: 5px; padding: 8px; }")
        self.btn_limpiar.clicked.connect(self.gestionar_click_limpiar)

        # Layout Superior
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.lbl_descripcion)
        top_layout.addWidget(self.input_desc, stretch=2)
        top_layout.addWidget(self.lbl_monto)
        top_layout.addWidget(self.input_monto, stretch=1)
        top_layout.addWidget(self.btn_registrar)
        top_layout.addWidget(self.btn_editar)
        top_layout.addWidget(self.btn_limpiar)

        # --- 2. Tabla (Centro) ---
        self.tabla = QTableWidget(0, 3)
        self.tabla.setHorizontalHeaderLabels(cabeceras)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla.setAlternatingRowColors(True)
        
        self.tabla.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                gridline-color: #333333;
                font-size: 12px;
            }
            QTableWidget::item:selected {
                background-color: #6B8E23;
                color: white;
            }
            QHeaderView::section {
                background-color: #6B8E23;
                color: white;
                padding: 5px;
                font-weight: bold;
            }
        """)
        
        self.tabla.horizontalHeader().setSectionResizeMode(1)
        
        self.tabla.clicked.connect(self.on_tabla_clicada)

        # --- Layout Principal ---
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.tabla)
        
        self.setLayout(main_layout)

    # --- Funciones auxiliares ---
    def es_fila_total(self, fila):
        if fila < 0 or self.tabla.rowCount() == 0:
            return False
        item = self.tabla.item(fila, 1)
        return item is not None and item.text() == "TOTAL"

    # --- Lógica ---

    def gestionar_click_registrar(self):
        if self.fila_seleccionada >= 0 and not self.es_fila_total(self.fila_seleccionada):
            self.actualizar_registro()
        else:
            self.agregar_nuevo_registro()

    def gestionar_click_limpiar(self):
        if self.fila_seleccionada >= 0 and not self.es_fila_total(self.fila_seleccionada):
            self.borrar_registro()
        else:
            self.limpiar_formulario()

    def agregar_nuevo_registro(self):
        desc = self.input_desc.text().strip()
        monto = self.input_monto.value()

        if not desc:
            QMessageBox.warning(self, "Advertencia", "Por favor ingrese una descripción.")
            return
            
        if monto == 0:
            QMessageBox.warning(self, "Advertencia", "El monto no puede ser 0. Ingrese un valor positivo o negativo.")
            return

        fecha_hoy = date.today().strftime("%Y-%m-%d")
        nuevo_reg = RegistroFinanza(fecha_hoy, desc, monto)
        self.lista_registros.append(nuevo_reg)

        fila_index = self.tabla.rowCount()
        if self.es_fila_total(self.tabla.rowCount() - 1):
            fila_index = self.tabla.rowCount() - 1
            
        self.tabla.insertRow(fila_index)
        self.set_celda(fila_index, 0, fecha_hoy)
        self.set_celda(fila_index, 1, desc)
        self.set_celda(fila_index, 2, f"{monto:.2f}")

        self.actualizar_total()
        self.limpiar_formulario()

    def on_tabla_clicada(self):
        fila_actual = self.tabla.currentRow()
        
        if self.es_fila_total(fila_actual):
            self.btn_editar.setEnabled(False)
            self.btn_editar.setText("✎ EDITAR")
            self.btn_limpiar.setText("LIMPIAR")
            self.btn_limpiar.setStyleSheet("QPushButton { background-color: #606060; color: white; border-radius: 5px; padding: 8px; }")
            self.fila_seleccionada = -1
        else:
            self.fila_seleccionada = fila_actual
            self.btn_editar.setEnabled(True)
            self.btn_editar.setText("✎ EDITAR SELECCIÓN")
            self.btn_limpiar.setText("🗑️ BORRAR")
            self.btn_limpiar.setStyleSheet(ESTILO_BOTON_BORRAR)
        
    def cargar_datos_en_inputs(self):
        if self.fila_seleccionada < 0 or self.es_fila_total(self.fila_seleccionada):
            return

        reg = self.lista_registros[self.fila_seleccionada]
        self.input_desc.setText(reg.descripcion)
        self.input_monto.setValue(reg.monto)

        self.btn_registrar.setText("GUARDAR CAMBIOS")
        self.btn_registrar.setStyleSheet("""
            QPushButton { background-color: #388E3C; color: white; border-radius: 5px; padding: 8px; font-weight: bold; }
            QPushButton:hover { background-color: #2E7D32; }
        """)

    def actualizar_registro(self):
        if self.fila_seleccionada < 0 or self.es_fila_total(self.fila_seleccionada):
            return
            
        desc = self.input_desc.text().strip()
        monto = self.input_monto.value()

        if not desc:
            return
            
        if monto == 0:
            QMessageBox.warning(self, "Advertencia", "El monto no puede ser 0. Ingrese un valor positivo o negativo.")
            return

        self.lista_registros[self.fila_seleccionada].descripcion = desc
        self.lista_registros[self.fila_seleccionada].monto = monto

        self.set_celda(self.fila_seleccionada, 1, desc)
        self.set_celda(self.fila_seleccionada, 2, f"{monto:.2f}")

        self.actualizar_total()
        self.limpiar_formulario()

    def borrar_registro(self):
        if self.fila_seleccionada < 0:
            return
            
        if self.fila_seleccionada >= len(self.lista_registros):
            return
            
        respuesta = QMessageBox.question(
            self, 
            "Confirmar Borrar", 
            "¿Está seguro de que desea eliminar este registro?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            indice = self.fila_seleccionada
            
            self.lista_registros.pop(indice)
            self.tabla.removeRow(indice)
            
            self.actualizar_total()
            
            self.limpiar_formulario()

    def limpiar_formulario(self):
        self.input_desc.clear()
        self.input_monto.setValue(0.0)
        
        self.btn_registrar.setText("REGISTRAR")
        self.btn_registrar.setStyleSheet(ESTILO_BOTON)
        
        self.btn_editar.setEnabled(False)
        self.btn_editar.setText("✎ EDITAR")
        
        self.btn_limpiar.setText("LIMPIAR")
        self.btn_limpiar.setStyleSheet("QPushButton { background-color: #606060; color: white; border-radius: 5px; padding: 8px; }")
        
        self.tabla.clearSelection()
        self.fila_seleccionada = -1

    def set_celda(self, fila, columna, texto):
        item = QTableWidgetItem(str(texto))
        item.setTextAlignment(Qt.AlignCenter)
        self.tabla.setItem(fila, columna, item)

    def actualizar_total(self):
        if self.tabla.rowCount() > 0 and self.es_fila_total(self.tabla.rowCount() - 1):
            self.tabla.removeRow(self.tabla.rowCount() - 1)

        total = sum(reg.monto for reg in self.lista_registros)
        
        fila_total = self.tabla.rowCount()
        self.tabla.insertRow(fila_total)
        
        self.set_celda(fila_total, 0, "")
        
        item_total = QTableWidgetItem("TOTAL")
        item_total.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        item_total.setFont(QFont("Arial", 10, QFont.Bold))
        self.tabla.setItem(fila_total, 1, item_total)
        
        texto_total = f"{total:.2f}"
        item_monto = QTableWidgetItem(texto_total)
        item_monto.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        if total >= 0:
            item_monto.setForeground(QColor(0, 200, 0))
        else:
            item_monto.setForeground(QColor(220, 50, 50))
            
        item_monto.setFont(QFont("Arial", 10, QFont.Bold))
        self.tabla.setItem(fila_total, 2, item_monto)
        
        self.tabla.setRowHeight(fila_total, 25)

# --- Función Main ---
def run():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True) 
    window = FinanzasApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()