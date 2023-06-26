import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
import sqlite3

# Crear la conexión a la base de datos
connection = sqlite3.connect("proveedores.db")
cursor = connection.cursor()

# Crear la tabla proveedores si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS proveedores (
        Nombre TEXT,
        Tipo TEXT,
        Cel TEXT,
        Mail TEXT,
        Direccion TEXT,
        Banco TEXT,
        Alias_CBU TEXT
    )
""")

connection.commit()
connection.close()


class ProveedoresWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras - Registro de Proveedores")
        self.setWindowIcon(QIcon("logo.jpeg"))
        
        self.nombre_label = QLabel("Nombre:")
        self.nombre_edit = QLineEdit()
        
        self.tipo_label = QLabel("Tipo:")
        self.tipo_edit = QLineEdit()
        
        self.cel_label = QLabel("Cel:")
        self.cel_edit = QLineEdit()
        
        self.mail_label = QLabel("Mail:")
        self.mail_edit = QLineEdit()
        
        self.direccion_label = QLabel("Dirección:")
        self.direccion_edit = QLineEdit()
        
        self.banco_label = QLabel("Banco:")
        self.banco_edit = QLineEdit()
        
        self.alias_cbu_label = QLabel("Alias/CBU:")
        self.alias_cbu_edit = QLineEdit()
        
        self.add_button = QPushButton("Añadir Proveedor")
        self.modify_button = QPushButton("Modificar Proveedor")
        self.delete_button = QPushButton("Eliminar Proveedor")
        
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Nombre", "Tipo", "Cel", "Mail", "Dirección", "Banco", "Alias/CBU"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # Deshabilitar la edición de celdas
        self.load_proveedores()
        
        self.add_button.clicked.connect(self.add_proveedor)
        self.modify_button.clicked.connect(self.modify_proveedor)
        self.delete_button.clicked.connect(self.delete_proveedor)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.nombre_label)
        form_layout.addWidget(self.nombre_edit)
        form_layout.addWidget(self.tipo_label)
        form_layout.addWidget(self.tipo_edit)
        form_layout.addWidget(self.cel_label)
        form_layout.addWidget(self.cel_edit)
        form_layout.addWidget(self.mail_label)
        form_layout.addWidget(self.mail_edit)
        form_layout.addWidget(self.direccion_label)
        form_layout.addWidget(self.direccion_edit)
        form_layout.addWidget(self.banco_label)
        form_layout.addWidget(self.banco_edit)
        form_layout.addWidget(self.alias_cbu_label)
        form_layout.addWidget(self.alias_cbu_edit)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.modify_button)
        button_layout.addWidget(self.delete_button)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)
        
        self.setLayout(main_layout)
    
    def load_proveedores(self):
        connection = sqlite3.connect("proveedores.db")
        cursor = connection.cursor()
        
        # Obtener los datos de los proveedores
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        
        # Configurar el número de filas en la tabla
        self.table.setRowCount(len(proveedores))
        
        # Rellenar la tabla con los datos de los proveedores
        for row, proveedor in enumerate(proveedores):
            for col, value in enumerate(proveedor):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)
        
        connection.close()
    
    def add_proveedor(self):
        nombre = self.nombre_edit.text()
        tipo = self.tipo_edit.text()
        cel = self.cel_edit.text()
        mail = self.mail_edit.text()
        direccion = self.direccion_edit.text()
        banco = self.banco_edit.text()
        alias_cbu = self.alias_cbu_edit.text()
        
        connection = sqlite3.connect("proveedores.db")
        cursor = connection.cursor()
        
        # Insertar el nuevo proveedor en la base de datos
        cursor.execute("INSERT INTO proveedores VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (nombre, tipo, cel, mail, direccion, banco, alias_cbu))
        connection.commit()
        
        connection.close()
        
        self.load_proveedores()
        self.clear_inputs()
    
    def modify_proveedor(self):
        # Obtener la fila seleccionada
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Modificar Proveedor", "No se ha seleccionado un proveedor.")
            return
        
        nombre = self.nombre_edit.text()
        tipo = self.tipo_edit.text()
        cel = self.cel_edit.text()
        mail = self.mail_edit.text()
        direccion = self.direccion_edit.text()
        banco = self.banco_edit.text()
        alias_cbu = self.alias_cbu_edit.text()
        
        connection = sqlite3.connect("proveedores.db")
        cursor = connection.cursor()
        
        # Modificar el proveedor seleccionado en la base de datos
        cursor.execute("UPDATE proveedores SET Nombre = ?, Tipo = ?, Cel = ?, Mail = ?, Direccion = ?, Banco = ?, Alias_CBU = ? WHERE rowid = ?",
                       (nombre, tipo, cel, mail, direccion, banco, alias_cbu, selected_row + 1))
        connection.commit()
        
        connection.close()
        
        self.load_proveedores()
        self.clear_inputs()
    
    def delete_proveedor(self):
        # Obtener la fila seleccionada
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Eliminar Proveedor", "No se ha seleccionado un proveedor.")
            return
        
        connection = sqlite3.connect("proveedores.db")
        cursor = connection.cursor()
        
        # Eliminar el proveedor seleccionado de la base de datos
        cursor.execute("DELETE FROM proveedores WHERE rowid = ?", (selected_row + 1,))
        connection.commit()
        
        connection.close()
        
        self.load_proveedores()
        self.clear_inputs()
    
    def clear_inputs(self):
        self.nombre_edit.clear()
        self.tipo_edit.clear()
        self.cel_edit.clear()
        self.mail_edit.clear()
        self.direccion_edit.clear()
        self.banco_edit.clear()
        self.alias_cbu_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    proveedores_window = ProveedoresWindow()
    proveedores_window.show()
    sys.exit(app.exec_())
