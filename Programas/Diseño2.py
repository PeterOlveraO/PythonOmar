import sys
import os

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

usuario_correcto="admin"
contrasena_correcta="1234"

class VentanaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), r"C:\Users\compr\PycharmProjects\PythonOmar\Qt\Qt.2.ui") # Asegurar la ruta correcta
        loadUi(ruta_ui, self) # Cargar la interfaz
        # conectar el boton a la funcion de login
        self.btnInicioSesion.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario= self.campo_usuario.text()
        contraseña= self.campo_contrasena.text()
        if usuario == usuario_correcto and contraseña== contrasena_correcta:
            QMessageBox.information(self,"Acceso permitido", "¡Entraste!")
        else:
            QMessageBox.warning(self,"Error","Usuario o contraseña incorrecta")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec())