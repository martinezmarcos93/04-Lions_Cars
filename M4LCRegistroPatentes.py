import sys
import sqlite3
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QFileDialog, QInputDialog


class PatentsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Registro de Patentes")
        self.setWindowIcon(QIcon("logo.jpeg"))  # Asegúrate de tener el archivo "logo.jpeg" en el directorio

        # Conexión a la base de datos
        self.conn = sqlite3.connect("patentes.db")
        self.cursor = self.conn.cursor()

        # Crear la tabla de patentes en la base de datos si no existe
        self.create_table()

        # Diseño de la interfaz
        self.layout = QVBoxLayout()

        # Botones
        self.add_button = QPushButton("Agregar Patente")
        self.add_button.clicked.connect(self.add_patent)
        self.layout.addWidget(self.add_button)

        # Tabla de patentes
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Patente", "Titular"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Botón "Ver Más"
        self.details_button = QPushButton("Ver Más")
        self.details_button.clicked.connect(self.show_details)
        self.layout.addWidget(self.details_button)

        # Cargar datos
        self.load_data()

        # Setear el diseño de la ventana
        self.setLayout(self.layout)

    def create_table(self):
        # Crear la tabla de patentes en la base de datos si no existe
        query = """CREATE TABLE IF NOT EXISTS patentes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patente TEXT,
                    titular TEXT,
                    dominio TEXT,
                    procedencia TEXT,
                    n_chasis TEXT,
                    n_motor TEXT,
                    anio TEXT,
                    modelo TEXT,
                    tipo TEXT
                )"""
        self.cursor.execute(query)
        self.conn.commit()

    def load_data(self):
        # Cargar datos de la base de datos y mostrar en la tabla
        query = "SELECT * FROM patentes"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data[0:3]):
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)

    def add_patent(self):
        # Agregar una nueva patente a la base de datos y actualizar la tabla
        patent_data, ok = self.get_patent_data()
        if ok:
            query = """INSERT INTO patentes (patente, titular) VALUES (?, ?)"""
            self.cursor.execute(query, patent_data)
            self.conn.commit()

            self.load_data()

    def show_details(self):
        # Mostrar la ventana de detalles de una patente seleccionada
        selected_items = self.table.selectedItems()
        if len(selected_items) == 0:
            return

        row_idx = selected_items[0].row()
        patent_id = self.table.item(row_idx, 0).text()

        query = "SELECT * FROM patentes WHERE id = ?"
        self.cursor.execute(query, (patent_id,))
        data = self.cursor.fetchone()

        details_dialog = DetailsDialog(data)
        details_dialog.exec_()

    def get_patent_data(self):
        # Obtener los datos de una nueva patente
        patent_data = []

        fields = [
            ("Patente:", QLineEdit()),
            ("Titular:", QLineEdit())
        ]

        for field_name, field_widget in fields:
            value, ok = QInputDialog.getText(self, "Agregar Patente", field_name, QLineEdit.Normal)
            if not ok:
                return [], False
            field_widget.setText(value)
            patent_data.append(value)

        return patent_data, True


class DetailsDialog(QWidget):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Detalles de Patente")
        self.setWindowIcon(QIcon("logo.jpeg"))  # Asegúrate de tener el archivo "logo.jpeg" en el directorio

        # Diseño de la interfaz
        layout = QVBoxLayout()

        labels = ["Dominio:", "Procedencia:", "Nº Chasis:", "Nº Motor:", "Año:", "Modelo:", "Tipo:", "Titular:"]
        values = data[3:]

        for label, value in zip(labels, values):
            label_widget = QLabel(label)
            value_widget = QLabel(value)
            layout.addWidget(label_widget)
            layout.addWidget(value_widget)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    patents_window = PatentsWindow()
    patents_window.show()
    sys.exit(app.exec_())
