import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        
        # Botones para los registros
        self.clients_button = QPushButton("Registro de Clientes")
        
        self.patents_button = QPushButton("Registro de Patentes")
        
        self.sales_button = QPushButton("Registro de Ventas")
        
        
        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.clients_button)
        layout.addWidget(self.patents_button)
        layout.addWidget(self.sales_button)
        self.setLayout(layout)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
