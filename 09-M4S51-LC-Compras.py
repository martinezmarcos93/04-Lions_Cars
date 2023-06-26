import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
import sqlite3

# Conexión a la base de datos
connection = sqlite3.connect("compras.db")
cursor = connection.cursor()

# Crear la tabla "compras" si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS compras (
        Fecha TEXT,
        Proveedor TEXT,
        Factura TEXT,
        Tipo TEXT,
        Importe REAL
    )
""")

# Cerrar la conexión a la base de datos
cursor.close()
connection.close()



class ComprasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras - Registro de Facturación - Compras")
        self.resize(800, 600)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Botones para Añadir, Modificar y Eliminar Compra
        self.add_button = QPushButton("Añadir Compra")
        self.modify_button = QPushButton("Modificar Compra")
        self.delete_button = QPushButton("Eliminar Compra")
        self.add_button.clicked.connect(self.add_compra)
        self.modify_button.clicked.connect(self.modify_compra)
        self.delete_button.clicked.connect(self.delete_compra)

        # Tabla para mostrar las compras
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Fecha", "Proveedor", "Factura", "Tipo", "Importe"])
        self.load_compras()

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.modify_button)
        buttons_layout.addWidget(self.delete_button)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def load_compras(self):
        # Conexión a la base de datos
        connection = sqlite3.connect("compras.db")
        cursor = connection.cursor()

        # Obtener los datos de las compras
        cursor.execute("SELECT * FROM compras")
        compras = cursor.fetchall()

        # Establecer el número de filas en la tabla
        self.table.setRowCount(len(compras))

        # Mostrar los datos de las compras en la tabla
        for row, compra in enumerate(compras):
            for col, data in enumerate(compra):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row, col, item)

        # Cerrar la conexión a la base de datos
        cursor.close()
        connection.close()

    def add_compra(self):
        # Implementar la lógica para añadir una compra aquí
        QMessageBox.information(self, "Añadir Compra", "Funcionalidad no implementada.")

    def modify_compra(self):
        # Implementar la lógica para modificar una compra aquí
        QMessageBox.information(self, "Modificar Compra", "Funcionalidad no implementada.")

    def delete_compra(self):
        # Implementar la lógica para eliminar una compra aquí
        QMessageBox.information(self, "Eliminar Compra", "Funcionalidad no implementada.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    compras_window = ComprasWindow()
    compras_window.show()
    sys.exit(app.exec_())
