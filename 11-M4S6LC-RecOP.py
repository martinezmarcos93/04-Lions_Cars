import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog
from PyQt5.QtGui import QIcon 


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras - Recibos y Ordenes de Pago ")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))
        
        # Botones para los registros
        self.receipts_button = QPushButton("Recibos")
        self.receipts_button.clicked.connect(self.open_receipts_window)
        
        self.op_button = QPushButton("OP")
        self.op_button.clicked.connect(self.open_op_window)
        
        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.receipts_button)
        layout.addWidget(self.op_button)
        self.setLayout(layout)
    
    def open_receipts_window(self):
        receipts_window = ReceiptsWindow()
        receipts_window.exec_()
    
    def open_op_window(self):
        op_window = OPWindow()
        op_window.exec_()


class ReceiptsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recibos")
        # Aquí puedes agregar los elementos y la lógica necesaria para la ventana de recibos


class OPWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ordenes de Pago")
        # Aquí puedes agregar los elementos y la lógica necesaria para la ventana de OP


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
