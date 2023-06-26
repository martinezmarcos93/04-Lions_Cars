import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sqlite3


class InventarioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Productos y servicios - Inventario")
        self.resize(600, 400)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Conexión a la base de datos SQLite
        self.connection = sqlite3.connect("Inventario.db")
        self.cursor = self.connection.cursor()

        # Crear la tabla "Productos" si no existe
        self.create_table()

        # Widgets
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Nombre", "Marca", "Modelo", "Estado", "Valor"])

        self.refresh_button = QPushButton("Actualizar")
        self.add_button = QPushButton("Añadir Producto")
        self.modify_button = QPushButton("Modificar Producto")
        self.delete_button = QPushButton("Eliminar Producto")

        # Conexiones de los botones a las funciones correspondientes
        self.refresh_button.clicked.connect(self.refresh_table)
        self.add_button.clicked.connect(self.add_product)
        self.modify_button.clicked.connect(self.modify_product)
        self.delete_button.clicked.connect(self.delete_product)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.modify_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Cargar los datos del inventario en la tabla
        self.refresh_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Productos (
                Nombre TEXT,
                Marca TEXT,
                Modelo TEXT,
                Estado TEXT,
                Valor REAL
            )
        """)
        self.connection.commit()

    def refresh_table(self):
        # Vaciar la tabla
        self.table.setRowCount(0)

        # Obtener los datos del inventario
        self.cursor.execute("SELECT * FROM Productos")
        productos = self.cursor.fetchall()

        # Llenar la tabla con los datos del inventario
        for row_number, row_data in enumerate(productos):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(row_number, column_number, item)

    def add_product(self):
        dialog = AddProductDialog()
        if dialog.exec_() == dialog.Accepted:
            nombre = dialog.nombre_edit.text()
            marca = dialog.marca_edit.text()
            modelo = dialog.modelo_edit.text()
            estado = dialog.estado_edit.text()
            valor = dialog.valor_edit.text()

            # Insertar el nuevo producto en la base de datos
            self.cursor.execute("INSERT INTO Productos VALUES (?, ?, ?, ?, ?)",
                                (nombre, marca, modelo, estado, valor))
            self.connection.commit()

            # Actualizar la tabla
            self.refresh_table()

    def modify_product(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if len(selected_rows) != 1:
            QMessageBox.warning(self, "Modificar Producto", "Selecciona un solo producto para modificar.")
            return

        row = selected_rows[0].row()

        nombre = self.table.item(row, 0).text()
        marca = self.table.item(row, 1).text()
        modelo = self.table.item(row, 2).text()
        estado = self.table.item(row, 3).text()
        valor = self.table.item(row, 4).text()

        dialog = ModifyProductDialog(nombre, marca, modelo, estado, valor)
        if dialog.exec_() == dialog.Accepted:
            new_nombre = dialog.nombre_edit.text()
            new_marca = dialog.marca_edit.text()
            new_modelo = dialog.modelo_edit.text()
            new_estado = dialog.estado_edit.text()
            new_valor = dialog.valor_edit.text()

            # Actualizar los datos del producto en la base de datos
            self.cursor.execute("""
                UPDATE Productos
                SET Nombre = ?, Marca = ?, Modelo = ?, Estado = ?, Valor = ?
                WHERE Nombre = ? AND Marca = ? AND Modelo = ? AND Estado = ? AND Valor = ?
            """, (new_nombre, new_marca, new_modelo, new_estado, new_valor,
                  nombre, marca, modelo, estado, valor))
            self.connection.commit()

            # Actualizar la tabla
            self.refresh_table()

    def delete_product(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if len(selected_rows) == 0:
            QMessageBox.warning(self, "Eliminar Producto", "Selecciona al menos un producto para eliminar.")
            return

        confirm = QMessageBox.question(self, "Eliminar Producto",
                                       "¿Estás seguro de que quieres eliminar los productos seleccionados?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            for row in selected_rows:
                nombre = self.table.item(row.row(), 0).text()
                marca = self.table.item(row.row(), 1).text()
                modelo = self.table.item(row.row(), 2).text()
                estado = self.table.item(row.row(), 3).text()
                valor = self.table.item(row.row(), 4).text()

                # Eliminar el producto de la base de datos
                self.cursor.execute("""
                    DELETE FROM Productos
                    WHERE Nombre = ? AND Marca = ? AND Modelo = ? AND Estado = ? AND Valor = ?
                """, (nombre, marca, modelo, estado, valor))
                self.connection.commit()

            # Actualizar la tabla
            self.refresh_table()

    def closeEvent(self, event):
        self.connection.close()
        event.accept()


class AddProductDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Añadir Producto")
        self.setWindowModality(Qt.ApplicationModal)

        # Widgets
        self.nombre_label = QLabel("Nombre:")
        self.nombre_edit = QLineEdit()
        self.marca_label = QLabel("Marca:")
        self.marca_edit = QLineEdit()
        self.modelo_label = QLabel("Modelo:")
        self.modelo_edit = QLineEdit()
        self.estado_label = QLabel("Estado:")
        self.estado_edit = QLineEdit()
        self.valor_label = QLabel("Valor:")
        self.valor_edit = QLineEdit()

        self.add_button = QPushButton("Añadir")
        self.cancel_button = QPushButton("Cancelar")

        # Conexiones de los botones a las funciones correspondientes
        self.add_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_edit)
        layout.addWidget(self.marca_label)
        layout.addWidget(self.marca_edit)
        layout.addWidget(self.modelo_label)
        layout.addWidget(self.modelo_edit)
        layout.addWidget(self.estado_label)
        layout.addWidget(self.estado_edit)
        layout.addWidget(self.valor_label)
        layout.addWidget(self.valor_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)


class ModifyProductDialog(QWidget):
    def __init__(self, nombre, marca, modelo, estado, valor):
        super().__init__()
        self.setWindowTitle("Modificar Producto")
        self.setWindowModality(Qt.ApplicationModal)

        # Widgets
        self.nombre_label = QLabel("Nombre:")
        self.nombre_edit = QLineEdit(nombre)
        self.marca_label = QLabel("Marca:")
        self.marca_edit = QLineEdit(marca)
        self.modelo_label = QLabel("Modelo:")
        self.modelo_edit = QLineEdit(modelo)
        self.estado_label = QLabel("Estado:")
        self.estado_edit = QLineEdit(estado)
        self.valor_label = QLabel("Valor:")
        self.valor_edit = QLineEdit(valor)

        self.modify_button = QPushButton("Modificar")
        self.cancel_button = QPushButton("Cancelar")

        # Conexiones de los botones a las funciones correspondientes
        self.modify_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_edit)
        layout.addWidget(self.marca_label)
        layout.addWidget(self.marca_edit)
        layout.addWidget(self.modelo_label)
        layout.addWidget(self.modelo_edit)
        layout.addWidget(self.estado_label)
        layout.addWidget(self.estado_edit)
        layout.addWidget(self.valor_label)
        layout.addWidget(self.valor_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.modify_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inventario_window = InventarioWindow()
    inventario_window.show()
    sys.exit(app.exec_())
