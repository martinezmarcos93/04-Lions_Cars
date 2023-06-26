import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QIcon 
from PyQt5.QtCore import Qt
from reportlab.pdfgen import canvas


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras - Recibos y Ordenes de Pago - OP")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Botones para los submódulos
        self.op_button = QPushButton("Ordenes de Pago")
        self.op_button.clicked.connect(self.open_op_window)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.op_button)
        self.setLayout(layout)

    def open_op_window(self):
        op_window = OPWindow()
        op_window.exec_()


class OPWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ordenes de Pago")
        self.resize(400, 300)

        # Botón para generar las Ordenes de Pago
        self.generate_op_button = QPushButton("Generar Ordenes de Pago")
        self.generate_op_button.clicked.connect(self.generate_op)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.generate_op_button)
        self.setLayout(layout)

    def generate_op(self):
        # Obtener la información de las facturas desde la base de datos de ventas
        facturas = self.get_facturas_from_database()

        # Verificar si hay facturas disponibles
        if not facturas:
            QMessageBox.warning(self, "No hay facturas",
                                "No se encontraron facturas en la base de datos.")
            return

        # Generar el documento PDF con las Ordenes de Pago
        self.generate_pdf_op(facturas)

        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Ordenes de Pago generadas",
                                "Se han generado las Ordenes de Pago exitosamente.")

    def get_facturas_from_database(self):
        # Aquí iría el código para obtener las facturas desde la base de datos de ventas
        # Retorna una lista de facturas o un objeto que contenga la información necesaria para generar las Ordenes de Pago
        # Por ejemplo:
        facturas = [
            {"fecha": "2023-06-01", "cliente": "Cliente 1", "factura": "9876", "importe": 300.0},
            {"fecha": "2023-06-02", "cliente": "Cliente 2", "factura": "5432", "importe": 400.0},
        ]

        return facturas

    def generate_pdf_op(self, facturas):
        # Crear el documento PDF
        c = canvas.Canvas("orden_pago_Lions_Cars.pdf")

        # Configuración de la fuente y el tamaño del texto
        c.setFont("Helvetica", 12)

        # Encabezado de la Orden de Pago
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 750, "Orden de Pago Lions Cars")
        c.setFont("Helvetica", 12)
        c.drawString(50, 720, "Fecha: 2023-06-07")
        c.drawString(50, 700, "-----------------------------------------------------------")

        # Contenido de la Orden de Pago
        y = 650
        for factura in facturas:
            c.drawString(50, y, "Factura: {}".format(factura["factura"]))
            c.drawString(50, y - 20, "Fecha: {}".format(factura["fecha"]))
            c.drawString(50, y - 40, "Cliente: {}".format(factura["cliente"]))
            c.drawString(50, y - 60, "Importe: {}".format(factura["importe"]))
            c.drawString(50, y - 80, "-----------------------------------------------------------")
            y -= 100

        # Guardar y cerrar el documento
        c.save()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
