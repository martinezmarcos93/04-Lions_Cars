import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon

class ConsultarExpedienteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Documentar Expedientes - Consultar Expediente")
        self.resize(400, 600)
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Elementos de la interfaz
        self.expediente_label = QLabel("Expediente:")
        self.expediente_text = QLineEdit()
        self.consultar_button = QPushButton("Consultar")
        self.resultado_text = QTextEdit()

        # Conectar el botón de consultar a la función correspondiente
        self.consultar_button.clicked.connect(self.consultar_expediente)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.expediente_label)
        layout.addWidget(self.expediente_text)
        layout.addWidget(self.consultar_button)
        layout.addWidget(self.resultado_text)
        self.setLayout(layout)

    def consultar_expediente(self):
        expediente = self.expediente_text.text()

        # Lógica para consultar el expediente
        # ...

        # Mostrar el resultado en el cuadro de texto
        resultado = f"Expediente consultado: {expediente}\n"
        resultado += "Información del expediente:\n"
        # Aquí puedes agregar la información del expediente obtenida durante la consulta
        self.resultado_text.setPlainText(resultado)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    consultar_expediente_window = ConsultarExpedienteWindow()
    consultar_expediente_window.show()
    sys.exit(app.exec_())
