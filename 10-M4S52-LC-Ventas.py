import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon



class VentasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras - Registro de Facturación - Ventas")
        self.resize(600, 400)
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Botones de acciones
        self.add_button = QPushButton("Añadir Venta")
        self.modify_button = QPushButton("Modificar Venta")
        self.delete_button = QPushButton("Eliminar Venta")

        # Tabla para mostrar los datos
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Fecha", "Proveedor", "Factura", "Tipo", "Importe"])

        # Cargar los datos de la base de datos
        self.load_ventas()

        # Conectar los botones a sus funciones correspondientes
        self.add_button.clicked.connect(self.add_venta)
        self.modify_button.clicked.connect(self.modify_venta)
        self.delete_button.clicked.connect(self.delete_venta)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.modify_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_ventas(self):
        # Conexión a la base de datos
        connection = sqlite3.connect("ventas.db")
        cursor = connection.cursor()

        # Obtener los registros de la tabla
        cursor.execute("SELECT * FROM ventas")
        rows = cursor.fetchall()

        # Mostrar los registros en la tabla
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)

        # Cerrar la conexión a la base de datos
        cursor.close()
        connection.close()

    def add_venta(self):
        # Ventana de diálogo para ingresar los datos de la venta
        dialog = QDialog(self)
        dialog.setWindowTitle("Añadir Venta")
        dialog.resize(300, 200)

        # Campos de entrada de datos
        fecha_label = QLabel("Fecha:")
        fecha_edit = QLineEdit()

        proveedor_label = QLabel("Proveedor:")
        proveedor_edit = QLineEdit()

        factura_label = QLabel("Factura:")
        factura_edit = QLineEdit()

        tipo_label = QLabel("Tipo:")
        tipo_edit = QLineEdit()

        importe_label = QLabel("Importe:")
        importe_edit = QLineEdit()

        # Botón de confirmación
        confirm_button = QPushButton("Confirmar")

        def confirm():
            fecha = fecha_edit.text()
            proveedor = proveedor_edit.text()
            factura = factura_edit.text()
            tipo = tipo_edit.text()
            importe = importe_edit.text()

            # Conexión a la base de datos
            connection = sqlite3.connect("ventas.db")
            cursor = connection.cursor()

            # Insertar el nuevo registro en la tabla
            cursor.execute("INSERT INTO ventas VALUES (?, ?, ?, ?, ?)",
                           (fecha, proveedor, factura, tipo, importe))
            connection.commit()

            # Cerrar la conexión a la base de datos
            cursor.close()
            connection.close()

            # Cerrar la ventana de diálogo
            dialog.close()

            # Actualizar la tabla de ventas
            self.load_ventas()

            # Mostrar mensaje de éxito
            QMessageBox.information(self, "Añadir Venta", "La venta se ha añadido correctamente.")

        # Conectar el botón de confirmación a la función de confirmación
        confirm_button.clicked.connect(confirm)

        # Diseño de la ventana de diálogo
        layout = QVBoxLayout()
        layout.addWidget(fecha_label)
        layout.addWidget(fecha_edit)
        layout.addWidget(proveedor_label)
        layout.addWidget(proveedor_edit)
        layout.addWidget(factura_label)
        layout.addWidget(factura_edit)
        layout.addWidget(tipo_label)
        layout.addWidget(tipo_edit)
        layout.addWidget(importe_label)
        layout.addWidget(importe_edit)
        layout.addWidget(confirm_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def modify_venta(self):
        # Obtener la fila seleccionada
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Modificar Venta", "No se ha seleccionado ninguna venta.")
            return

        # Obtener los datos de la venta seleccionada
        fecha = self.table.item(selected_row, 0).text()
        proveedor = self.table.item(selected_row, 1).text()
        factura = self.table.item(selected_row, 2).text()
        tipo = self.table.item(selected_row, 3).text()
        importe = self.table.item(selected_row, 4).text()

        # Ventana de diálogo para modificar los datos de la venta
        dialog = QDialog(self)
        dialog.setWindowTitle("Modificar Venta")
        dialog.resize(300, 200)

        # Campos de entrada de datos pre-llenados
        fecha_label = QLabel("Fecha:")
        fecha_edit = QLineEdit(fecha)

        proveedor_label = QLabel("Proveedor:")
        proveedor_edit = QLineEdit(proveedor)

        factura_label = QLabel("Factura:")
        factura_edit = QLineEdit(factura)

        tipo_label = QLabel("Tipo:")
        tipo_edit = QLineEdit(tipo)

        importe_label = QLabel("Importe:")
        importe_edit = QLineEdit(importe)

        # Botón de confirmación
        confirm_button = QPushButton("Confirmar")

        def confirm():
            new_fecha = fecha_edit.text()
            new_proveedor = proveedor_edit.text()
            new_factura = factura_edit.text()
            new_tipo = tipo_edit.text()
            new_importe = importe_edit.text()

            # Conexión a la base de datos
            connection = sqlite3.connect("ventas.db")
            cursor = connection.cursor()

            # Actualizar el registro en la tabla
            cursor.execute("UPDATE ventas SET Fecha = ?, Proveedor = ?, Factura = ?, Tipo = ?, Importe = ? "
                           "WHERE Fecha = ? AND Proveedor = ? AND Factura = ? AND Tipo = ? AND Importe = ?",
                           (new_fecha, new_proveedor, new_factura, new_tipo, new_importe,
                            fecha, proveedor, factura, tipo, importe))
            connection.commit()

            # Cerrar la conexión a la base de datos
            cursor.close()
            connection.close()

            # Cerrar la ventana de diálogo
            dialog.close()

            # Actualizar la tabla de ventas
            self.load_ventas()

            # Mostrar mensaje de éxito
            QMessageBox.information(self, "Modificar Venta", "La venta se ha modificado correctamente.")

        # Conectar el botón de confirmación a la función de confirmación
        confirm_button.clicked.connect(confirm)

        # Diseño de la ventana de diálogo
        layout = QVBoxLayout()
        layout.addWidget(fecha_label)
        layout.addWidget(fecha_edit)
        layout.addWidget(proveedor_label)
        layout.addWidget(proveedor_edit)
        layout.addWidget(factura_label)
        layout.addWidget(factura_edit)
        layout.addWidget(tipo_label)
        layout.addWidget(tipo_edit)
        layout.addWidget(importe_label)
        layout.addWidget(importe_edit)
        layout.addWidget(confirm_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def delete_venta(self):
        # Obtener la fila seleccionada
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Eliminar Venta", "No se ha seleccionado ninguna venta.")
            return

        # Obtener los datos de la venta seleccionada
        fecha = self.table.item(selected_row, 0).text()
        proveedor = self.table.item(selected_row, 1).text()
        factura = self.table.item(selected_row, 2).text()
        tipo = self.table.item(selected_row, 3).text()
        importe = self.table.item(selected_row, 4).text()

        # Ventana de confirmación de eliminación
        confirmation = QMessageBox.question(self, "Eliminar Venta",
                                            f"¿Estás seguro de que quieres eliminar la venta:\n"
                                            f"Fecha: {fecha}\nProveedor: {proveedor}\n"
                                            f"Factura: {factura}\nTipo: {tipo}\nImporte: {importe}?",
                                            QMessageBox.Yes | QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            # Conexión a la base de datos
            connection = sqlite3.connect("ventas.db")
            cursor = connection.cursor()

            # Eliminar el registro de la tabla
            cursor.execute("DELETE FROM ventas WHERE Fecha = ? AND Proveedor = ? AND Factura = ? AND Tipo = ? AND Importe = ?",
                           (fecha, proveedor, factura, tipo, importe))
            connection.commit()

            # Cerrar la conexión a la base de datos
            cursor.close()
            connection.close()

            # Actualizar la tabla de ventas
            self.load_ventas()

            # Mostrar mensaje de éxito
            QMessageBox.information(self, "Eliminar Venta", "La venta se ha eliminado correctamente.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventas_window = VentasWindow()
    ventas_window.show()
    sys.exit(app.exec_())
