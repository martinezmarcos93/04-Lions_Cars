import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# from modulo3_inventario import InventarioWindow
# from modulo3_presupuestos import PresupuestosWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars-Panel de Trabajo")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))
        
        # Botones para las secciones
        self.productos_button = QPushButton("Productos y servicios")
        self.ventas_compras_button = QPushButton("Ventas y compras")
        self.expedientes_button = QPushButton("Expedientes")
        
        # Conexiones de los botones a las funciones correspondientes
        self.productos_button.clicked.connect(self.open_productos_window)
        self.ventas_compras_button.clicked.connect(self.open_ventas_compras_window)
        self.expedientes_button.clicked.connect(self.open_expedientes_window)
        
        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.productos_button)
        layout.addWidget(self.ventas_compras_button)
        layout.addWidget(self.expedientes_button)
        self.setLayout(layout)
    
    def open_productos_window(self):
        productos_window = ProductosWindow()
        productos_window.exec_()
    
    def open_ventas_compras_window(self):
        ventas_compras_window = VentasComprasWindow()
        ventas_compras_window.exec_()
    
    def open_expedientes_window(self):
        expedientes_window = ExpedientesWindow()
        expedientes_window.exec_()


class ProductosWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Productos y servicios")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        
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
    
    # def open_inventario_window(self):
    #     inventario_window = InventarioWindow()
    #     inventario_window.exec_()
    
    # def open_presupuestos_window(self):
    #     presupuestos_window = PresupuestosWindow()
    #     presupuestos_window.exec_()


class VentasComprasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y compras")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        
        # Implementa la funcionalidad de Ventas y compras aquí
        
        layout = QVBoxLayout()
        # Agrega los widgets y diseño necesario
        self.setLayout(layout)


class ExpedientesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Expedientes")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        
        # Implementa la funcionalidad de Expedientes aquí
        
        layout = QVBoxLayout()
        # Agrega los widgets y diseño necesario
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
