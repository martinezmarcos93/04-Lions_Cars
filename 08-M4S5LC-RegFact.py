import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon


class FacturacionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras - Registro de Facturación")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Botones para Compras y Ventas
        self.compras_button = QPushButton("Compras")
        self.compras_button.clicked.connect(self.open_compras_window)

        self.ventas_button = QPushButton("Ventas")
        self.ventas_button.clicked.connect(self.open_ventas_window)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.compras_button)
        layout.addWidget(self.ventas_button)
        self.setLayout(layout)

    def open_compras_window(self):
        compras_window = ComprasWindow()
        compras_window.show()

    def open_ventas_window(self):
        ventas_window = VentasWindow()
        ventas_window.show()


class ComprasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Compras")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        # Implementar la funcionalidad de Registro de Compras aquí


class VentasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Ventas")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        # Implementar la funcionalidad de Registro de Ventas aquí


if __name__ == "__main__":
    app = QApplication(sys.argv)
    facturacion_window = FacturacionWindow()
    facturacion_window.show()
    sys.exit(app.exec_())
