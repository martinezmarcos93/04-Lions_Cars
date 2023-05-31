import sys
import sqlite3
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QFileDialog, QInputDialog


class SalesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Registro de Ventas")
        self.setWindowIcon(QIcon("logo.jpeg"))  # Asegúrate de tener el archivo "logo.jpeg" en el directorio

        # Conexión a la base de datos
        self.conn = sqlite3.connect("ventas.db")
        self.cursor = self.conn.cursor()

        # Crear la tabla de ventas en la base de datos si no existe
        self.create_table()

        # Diseño de la interfaz
        self.layout = QVBoxLayout()

        # Botones
        self.add_button = QPushButton("Agregar Venta")
        self.add_button.clicked.connect(self.add_sale)
        self.layout.addWidget(self.add_button)

        self.catalog_button = QPushButton("Catálogo")
        self.catalog_button.clicked.connect(self.open_catalog)
        self.layout.addWidget(self.catalog_button)

        # Tabla de ventas
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Fecha de Venta", "Cliente", "Producto", "Importe", "Cuotas", "Cuotas Abonadas", "Cuotas Adeudadas"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Cargar datos
        self.load_data()

        # Setear el diseño de la ventana
        self.setLayout(self.layout)

    def create_table(self):
        # Crear la tabla de ventas en la base de datos si no existe
        query = """CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT,
                    cliente TEXT,
                    producto TEXT,
                    importe REAL,
                    cuotas INTEGER,
                    cuotas_abonadas INTEGER,
                    cuotas_adeudadas INTEGER
                )"""
        self.cursor.execute(query)
        self.conn.commit()

    def load_data(self):
        # Cargar datos de la base de datos y mostrar en la tabla
        query = "SELECT * FROM ventas"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data[1:]):
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)

    def add_sale(self):
        # Agregar una nueva venta a la base de datos y actualizar la tabla
        sale_data, ok = self.get_sale_data()
        if ok:
            query = """INSERT INTO ventas (fecha, cliente, producto, importe, cuotas, cuotas_abonadas, cuotas_adeudadas) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(query, sale_data)
            self.conn.commit()

            self.load_data()

    def get_sale_data(self):
        # Obtener los datos de una nueva venta
        sale_data = []

        fields = [
            ("Fecha de Venta:", QLineEdit()),
            ("Cliente:", QLineEdit()),
            ("Producto:", QLineEdit()),
            ("Importe:", QLineEdit()),
            ("Cuotas:", QLineEdit()),
            ("Cuotas Abonadas:", QLineEdit()),
            ("Cuotas Adeudadas:", QLineEdit())
        ]

        for field_name, field_widget in fields:
            value, ok = QInputDialog.getText(self, "Agregar Venta", field_name, QLineEdit.Normal)
            if not ok:
                return [], False
            field_widget.setText(value)
            sale_data.append(value)

        return sale_data, True

    def open_catalog(self):
        # Abrir la ventana del catálogo de productos
        catalog_dialog = CatalogDialog(self.conn)
        catalog_dialog.exec_()


class CatalogDialog(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.setWindowTitle("Catálogo de Productos")
        self.setWindowIcon(QIcon("logo.jpeg"))  # Asegúrate de tener el archivo "logo.jpeg" en el directorio

        # Conexión a la base de datos
        self.conn = conn
        self.cursor = self.conn.cursor()

        # Crear la tabla de productos en la base de datos si no existe
        self.create_table()

        # Diseño de la interfaz
        self.layout = QVBoxLayout()

        # Botones
        self.add_button = QPushButton("Agregar Producto")
        self.add_button.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_button)

        self.list_button = QPushButton("Lista de Productos")
        self.list_button.clicked.connect(self.show_products)
        self.layout.addWidget(self.list_button)

        self.details_button = QPushButton("Detalles de Producto")
        self.details_button.clicked.connect(self.show_product_details)
        self.layout.addWidget(self.details_button)

        # Setear el diseño de la ventana
        self.setLayout(self.layout)

    def create_table(self):
        # Crear la tabla de productos en la base de datos si no existe
        query = """CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    descripcion TEXT,
                    precio REAL
                )"""
        self.cursor.execute(query)
        self.conn.commit()

    def add_product(self):
        # Agregar un nuevo producto a la base de datos
        product_data, ok = self.get_product_data()
        if ok:
            query = "INSERT INTO productos (nombre, descripcion, precio) VALUES (?, ?, ?)"
            self.cursor.execute(query, product_data)
            self.conn.commit()

    def get_product_data(self):
        # Obtener los datos de un nuevo producto
        product_data = []

        fields = [
            ("Nombre:", QLineEdit()),
            ("Descripción:", QLineEdit()),
            ("Precio:", QLineEdit())
        ]

        for field_name, field_widget in fields:
            value, ok = QInputDialog.getText(self, "Agregar Producto", field_name, QLineEdit.Normal)
            if not ok:
                return [], False
            field_widget.setText(value)
            product_data.append(value)

        return product_data, True

    def show_products(self):
        # Mostrar la lista de productos en una ventana de diálogo
        query = "SELECT nombre FROM productos"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        products = [row[0] for row in data]
        product_list = "\n".join(products)

        QMessageBox.information(self, "Lista de Productos", product_list)

    def show_product_details(self):
        # Mostrar los detalles de un producto seleccionado en una ventana de diálogo
        query = "SELECT * FROM productos"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        product_names = [row[1] for row in data]
        selected_product, ok = QInputDialog.getItem(self, "Detalles de Producto", "Selecciona un producto:", product_names, 0, False)

        if ok and selected_product:
            selected_product_idx = product_names.index(selected_product)
            selected_product_data = data[selected_product_idx]
            product_details = f"""
            Nombre: {selected_product_data[1]}
            Descripción: {selected_product_data[2]}
            Precio: {selected_product_data[3]}
            """

            QMessageBox.information(self, "Detalles de Producto", product_details)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sales_window = SalesWindow()
    sales_window.show()
    sys.exit(app.exec_())
