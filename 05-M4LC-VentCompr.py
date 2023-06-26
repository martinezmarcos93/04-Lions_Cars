import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon


class VentasComprasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras")
        self.setWindowIcon(QIcon("logo.jpeg"))
        
        self.gestores_button = QPushButton("Registro de Gestores")
        self.clientes_button = QPushButton("Registro de Clientes")
        self.facturacion_button = QPushButton("Registro de Facturación")
        self.recibos_button = QPushButton("Elaboración de recibos y Órdenes de Pago")
        
        layout = QVBoxLayout()
        layout.addWidget(self.gestores_button)
        layout.addWidget(self.clientes_button)
        layout.addWidget(self.facturacion_button)
        layout.addWidget(self.recibos_button)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventas_compras_window = VentasComprasWindow()
    ventas_compras_window.show()
    sys.exit(app.exec_())
