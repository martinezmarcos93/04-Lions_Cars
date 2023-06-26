import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class ProductosServiciosWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Productos y servicios")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))
        
        # Botones para las funcionalidades de productos y servicios
        self.inventario_button = QPushButton("Inventario")
        self.presupuestos_button = QPushButton("Presupuestos")
        
        # Conexiones de los botones a las funciones correspondientes
        self.inventario_button.clicked.connect(self.open_inventario_window)
        self.presupuestos_button.clicked.connect(self.open_presupuestos_window)
        
        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.inventario_button)
        layout.addWidget(self.presupuestos_button)
        self.setLayout(layout)
    
    def open_inventario_window(self):
        inventario_window = InventarioWindow()
        inventario_window.exec_()
    
    def open_presupuestos_window(self):
        presupuestos_window = PresupuestosWindow()
        presupuestos_window.exec_()


class InventarioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Inventario")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        
        # Implementa la funcionalidad de Inventario aquí
        
        layout = QVBoxLayout()
        # Agrega los widgets y diseño necesario
        self.setLayout(layout)


class PresupuestosWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Presupuestos")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        
        # Implementa la funcionalidad de Presupuestos aquí
        
        layout = QVBoxLayout()
        # Agrega los widgets y diseño necesario
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    productos_servicios_window = ProductosServiciosWindow()
    productos_servicios_window.show()
    sys.exit(app.exec_())
