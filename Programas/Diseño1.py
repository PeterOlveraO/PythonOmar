import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.uic import loadUi

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), r"C:\Users\compr\PycharmProjects\PythonOmar\Qt\Qt1.ui") # Asegurar la ruta correcta
        loadUi(ruta_ui, self) # Cargar la interfaz


        # Conectar el botón a la función que cambia el texto
        self.boton_cambiar = self.centralwidget.findChild(QPushButton, "boton_cambiar")
        self.mi_label = self.centralwidget.findChild(QLabel, "mi_label")

        if self.boton_cambiar and self.mi_label:
            self.boton_cambiar.clicked.connect(self.cambiar_texto)

    def cambiar_texto(self):
        self.mi_label.setText("¡Hola, mundo!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
