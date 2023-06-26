import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from reportlab.pdfgen import canvas


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Ventas y Compras - Recibos y Ordenes de Pago - Recibos")
        self.resize(400, 300)  # Establecer el tamaño de la ventana
        self.setWindowIcon(QIcon("logo.jpeg"))

        # Botones para los submódulos
        self.receipts_button = QPushButton("Recibos")
        self.receipts_button.clicked.connect(self.open_receipts_window)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.receipts_button)
        self.setLayout(layout)

    def open_receipts_window(self):
        receipts_window = ReceiptsWindow()
        receipts_window.exec_()


class ReceiptsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recibos")
        self.resize(400, 300)

        # Botones para seleccionar el tipo de factura
        self.compras_button = QPushButton("Compras")
        self.compras_button.clicked.connect(lambda: self.generate_receipts("compras"))
        self.ventas_button = QPushButton("Ventas")
        self.ventas_button.clicked.connect(lambda: self.generate_receipts("ventas"))

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.compras_button)
        layout.addWidget(self.ventas_button)
        self.setLayout(layout)

    def generate_receipts(self, tipo_factura):
        # Obtener la información de las facturas desde la base de datos según el tipo especificado
        facturas = self.get_facturas_from_database(tipo_factura)

        # Verificar si hay facturas disponibles
        if not facturas:
            QMessageBox.warning(self, "No hay facturas",
                                "No se encontraron facturas del tipo especificado en la base de datos.")
            return

        # Generar el documento PDF con los recibos
        self.generate_pdf_recibos(facturas)

        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Recibos generados",
                                "Se han generado los recibos exitosamente.")

    def get_facturas_from_database(self, tipo_factura):
        # Aquí iría el código para obtener las facturas desde la base de datos según el tipo especificado
        # Retorna una lista de facturas o un objeto que contenga la información necesaria para generar los recibos
        # Por ejemplo:
        if tipo_factura == "compras":
            facturas = [
                {"fecha": "2023-06-01", "proveedor": "Proveedor 1", "factura": "1234", "importe": 100.0},
                {"fecha": "2023-06-02", "proveedor": "Proveedor 2", "factura": "5678", "importe": 200.0},
            ]
        elif tipo_factura == "ventas":
            facturas = [
                {"fecha": "2023-06-01", "cliente": "Cliente 1", "factura": "9876", "importe": 300.0},
                {"fecha": "2023-06-02", "cliente": "Cliente 2", "factura": "5432", "importe": 400.0},
            ]
        else:
            facturas = []

        return facturas

    def generate_pdf_recibos(self, facturas):
        # Crear el documento PDF
        c = canvas.Canvas("recibo_Lions_Cars.pdf")

        # Configuración de la fuente y el tamaño del texto
        c.setFont("Helvetica", 12)

        # Encabezado del recibo
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 750, "Recibo Lions Cars")
        c.setFont("Helvetica", 12)
        c.drawString(50, 720, "Fecha: 2023-06-07")
        c.drawString(50, 700, "-----------------------------------------------------------")

        # Contenido del recibo
        y = 650
        for factura in facturas:
            c.drawString(50, y, "Factura: {}".format(factura["factura"]))
            c.drawString(50, y - 20, "Fecha: {}".format(factura["fecha"]))
            c.drawString(50, y - 40, "Proveedor: {}".format(factura["proveedor"]))
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
