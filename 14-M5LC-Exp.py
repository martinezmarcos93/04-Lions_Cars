import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon 


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Expedientes ")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Botones para los submódulos
        self.documentar_button = QPushButton("Documentar Expediente")
        self.documentar_button.clicked.connect(self.open_documentar_window)

        self.consultar_button = QPushButton("Consultar Expediente")
        self.consultar_button.clicked.connect(self.open_consultar_window)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.documentar_button)
        layout.addWidget(self.consultar_button)
        self.setLayout(layout)

    def open_documentar_window(self):
        documentar_window = DocumentarWindow()
        documentar_window.exec_()

    def open_consultar_window(self):
        consultar_window = ConsultarWindow()
        consultar_window.exec_()


class DocumentarWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Documentar Expediente")
        self.resize(400, 300)
        # Diseño de la ventana de Documentar Expediente
        # ...


class ConsultarWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consultar Expediente")
        self.resize(400, 300)
        # Diseño de la ventana de Consultar Expediente
        # ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
