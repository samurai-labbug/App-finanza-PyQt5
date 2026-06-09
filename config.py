
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

ESTILO_BOTON_EGRESO = """
    QPushButton {
        background-color: #e0b402;
        color: white;
        border-radius: 5px;
        padding: 8px;
        font-weight: bold;
        font-size: 12px;
    }
    QPushButton:hover {
        background-color: #e08002;
    }
    QPushButton:pressed {
        background-color: #b36b00;
    }
"""

# --- Estilo para inputs ---
ESTILO_INPUT = """
    QLineEdit {
        color: #000000;
        background-color: #FFFFFF;
        padding: 5px;
        font-size: 12px;
        border-radius: 3px;
        border: 1px solid #CCCCCC;
    }
    QLineEdit:focus {
        border: 2px solid #0078D7;
    }
"""

ESTILO_SPINBOX = """
    QDoubleSpinBox {
        color: #000000;
        background-color: #FFFFFF;
        padding: 5px;
        font-size: 12px;
        border: 1px solid #CCCCCC;
        border-radius: 3px;
    }
    QDoubleSpinBox:focus {
        border: 2px solid #0078D7;
    }
"""

# --- Estilo para los mensajes (QMessageBox) ---
ESTILO_MENSAJE = """
    QMessageBox {
        background-color: #2E3A1F;
        color: #FFFFFF;
    }
    QMessageBox QLabel {
        color: #FFFFFF;
        font-size: 12px;
    }
    QMessageBox QPushButton {
        background-color: #0078D7;
        color: white;
        border-radius: 5px;
        padding: 8px 20px;
        min-width: 60px;
    }
    QMessageBox QPushButton:hover {
        background-color: #005a9e;
    }
"""

ESTILO_TABLA= """
            QTableWidget {
                background-color: #FFFFFF;
                gridline-color: #CCCCCC;
                font-size: 12px;
            }
            QTableWidget::item {
                padding: 5px;
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
                border: none;
            }
            QTableWidget QTableCornerButton::section {
                background-color: #6B8E23;
                border: none;
            }
        """