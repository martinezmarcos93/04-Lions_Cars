import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon

class DocumentarExpedienteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Documentar Expedientes - Expediente")
        self.resize(400, 600)
        self.setWindowIcon(QIcon("logo.jpeg"))
        
        #Siniestros:
        self.fecha_adjudicacion = QLineEdit()
        self.fecha_ingreso = QLineEdit()
        self.num_siniestro = QLineEdit()
        self.liquidador = QLineEdit()
        self.asegurado = QLineEdit()
        self.telefono = QLineEdit()
        self.tipo_siniestro = QLineEdit()
        self.observaciones = QTextEdit()
        self.carpeta = QLineEdit()
        self.compania = QLineEdit()

        #Transporte:
        self.direccion = QLineEdit()
        self.num_orden_retiro = QLineEdit()
        self.libro_policial = QLineEdit()
        self.titulo = QLineEdit()
        self.cedula_verde = QLineEdit()
        self.costo = QLineEdit()
        self.localidad = QLineEdit()
        self.transportista = QLineEdit()
        self.fecha_ingreso_transporte = QLineEdit()
        self.placas = QLineEdit()
        self.dni_titular = QLineEdit()

        #Pericia:
        self.form_04d = QLineEdit()
        self.form_04 = QLineEdit()
        self.form_131 = QLineEdit()
        self.form_02 = QLineEdit()
        self.baja_destr_total = QLineEdit()
        self.baja_desarme = QLineEdit()
        self.ubicacion_legajo = QLineEdit()
        self.retiro_chapas = QLineEdit()
        self.adeuda_patentes = QLineEdit()
        self.fotos = QLineEdit()

        #Sistemas 1:
        self.pagina = QLineEdit()
        self.sss = QLineEdit()
        self.baja_siniestrado_num = QLineEdit()
        self.siniestro_id = QLineEdit()

        #Depósito:
        self.fecha_deposito_responsable = QLineEdit()

        #Gestoría:
        self.form_381 = QLineEdit()
        self.gestoria_baja_desarme = QLineEdit()
        self.prenda = QLineEdit()
        self.form_04d_lfa_aseg = QLineEdit()
        self.gestor = QLineEdit()
        self.gestoria_telefono = QLineEdit()
        self.fecha_entrega = QLineEdit()
        self.finalizacion = QLineEdit()
        self.obleas = QLineEdit()
        self.gestoria_02 = QLineEdit()
        self.costo_04 = QLineEdit()
        self.costo_08 = QLineEdit()
        self.transf_cliente = QLineEdit()

        #Sistemas 2:
        self.datos_cargados = QLineEdit()
        self.sistemas_02 = QLineEdit()
        self.sistemas_13b = QLineEdit()
        self.sistemas_04 = QLineEdit()
        self.sistemas_04d = QLineEdit()
        self.bd = QLineEdit()
        self.plana = QLineEdit()
        self.factura = QLineEdit()
        self.compact = QLineEdit()
        self.email_enviado_a = QLineEdit()
        self.con_copia_a = QLineEdit()
        self.sistemas_fecha = QLineEdit()
        self.sistemas_titulo = QLineEdit()
        self.sistemas_cedula = QLineEdit()
        self.form_08 = QLineEdit()
        self.ld_patentes = QLineEdit()
        self.ld_infracciones = QLineEdit()
        self.form_02_sistemas = QLineEdit()

        #Envío de Trámite:
        self.envio_tramite_fecha = QLineEdit()
        self.contacto = QLineEdit()
        self.mensajero = QLineEdit()
        self.coria = QLineEdit()
        self.envio_tramite_costo = QLineEdit()

        #Compactación:
        self.compactacion_fecha = QLineEdit()
        self.certif_num = QLineEdit()
        self.compactacion_costo = QLineEdit()

        #Liquidación:
        self.liquidacion_fecha = QLineEdit()
        self.liquidacion_compania = QLineEdit()
        self.liquidacion_banco = QLineEdit()
        self.num_factura = QLineEdit()
        self.asegurado = QLineEdit()
        self.num_comprobante = QLineEdit()
        self.cuenta = QLineEdit()

        #Comprador:
        self.comprador_apellido_nombre = QLineEdit()
        self.fact_num = QLineEdit()

        #Venta 08:
        self.estado = QLineEdit()
        self.gestor_venta = QLineEdit()
        self.transf = QLineEdit()
        self.transferido = QLineEdit()

        #Escaneos:
        self.escaneos_ingresar = QLineEdit()


        # # Botones
        # self.crear_expediente_button = QPushButton("Crear Expediente")
        # self.modificar_expediente_button = QPushButton("Modificar Expediente")
        # self.eliminar_expediente_button = QPushButton("Eliminar Expediente")

        # # Conectar los botones a sus respectivas funciones
        # # Conectar los botones a sus respectivas funciones
        # self.crear_expediente_button.clicked.connect(self.crear_expediente)
        # self.modificar_expediente_button.clicked.connect(self.modificar_expediente)
        # self.eliminar_expediente_button.clicked.connect(self.eliminar_expediente)


        # Diseño de la interfaz
        layout = QVBoxLayout()

        # Sección de Siniestros
        layout.addWidget(QLabel("Siniestros"))
        layout.addWidget(QLabel("Fecha Adjudicación"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Fecha Ingreso"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("N° de Siniestro"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Liquidador"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Asegurado/a"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Tel"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Tipo de siniestro"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Observaciones"))
        layout.addWidget(QTextEdit())
        layout.addWidget(QLabel("Carpeta"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Compañia"))
        layout.addWidget(QLineEdit())

        # Sección de Transporte
        layout.addWidget(QLabel("Transporte"))
        layout.addWidget(QLabel("Direccion"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("N° Orden Retiro"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Libro Policial"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Cargado"))
        # Agregar elementos para cargar archivos y guardarlos en la carpeta "Transporte"
        layout.addWidget(QLabel("Titulo"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Cedula Verde"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Costo"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Localidad"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Transportista"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Fecha Ingreso"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Placas"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("DNI Titular"))
        # Agregar elementos para ingresar archivos y guardarlos en la carpeta "Documentos de identidad"

        # Sección de Pericia
        layout.addWidget(QLabel("Pericia"))
        layout.addWidget(QLabel("Form 04D"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Form 04"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Form 131"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Form 02"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Baja destr. total"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Baja y desarme"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Ubicacion del Legajo"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Retiro Chapas"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Adeuda Patentes"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Fotos"))
        layout.addWidget(QLineEdit())

        # Sección de Sistemas 1
        layout.addWidget(QLabel("Sistemas 1"))
        layout.addWidget(QLabel("Pagina"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("S,S,S"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Baja/Siniestrado N°"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Siniestro ID"))
        layout.addWidget(QLineEdit())

        # Sección de Deposito
        layout.addWidget(QLabel("Deposito"))
        layout.addWidget(QLabel("FECHA DEPOSITO RESPONSABLE"))
        layout.addWidget(QLineEdit())

        # Sección de Gestoria
        layout.addWidget(QLabel("Gestoria"))
        layout.addWidget(QLabel("Form 381"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Baja y desarme"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Prenda"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("04D LFA ASEG"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Gestor"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Telefono"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Fecha Entrega"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Finalizacion"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("OBLEAS"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("02"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Costo 04"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Costo 08"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Transf Cliente"))
        layout.addWidget(QLineEdit())

        # Sección de Sistemas 2
        layout.addWidget(QLabel("Sistemas 2"))
        layout.addWidget(QLabel("Datos Cargados"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("02"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("13 B"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("04"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("04 D"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("B D"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Plana"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Factura"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Compact"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Email enviado a"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Con copia A"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Fecha"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Titulo"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Cedula"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Form 08"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("L/D Patentes"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("L/D Infracciones"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Form 02"))
        layout.addWidget(QLineEdit())

        # Sección de Envio de Tramite
        layout.addWidget(QLabel("Envio de Tramite"))
        layout.addWidget(QLabel("Fecha"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Contacto"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Mensajero"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Coria"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Costo"))
        layout.addWidget(QLineEdit())

        # Sección de Compactacion
        layout.addWidget(QLabel("Compactacion"))
        layout.addWidget(QLabel("Fecha"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Certif N°"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Costo"))
        layout.addWidget(QLineEdit())

        # Sección de Liquidacion
        layout.addWidget(QLabel("Liquidacion"))
        layout.addWidget(QLabel("Fecha"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Compañia"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Banco"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("N° Factura"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Asegurado"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("N° Comprob"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Cuenta"))
        layout.addWidget(QLineEdit())

        # Sección de Comprador
        layout.addWidget(QLabel("Comprador"))
        layout.addWidget(QLabel("Apellido y Nombre"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Fact N°"))
        layout.addWidget(QLineEdit())

        # Sección de Venta 08
        layout.addWidget(QLabel("Venta 08"))
        layout.addWidget(QLabel("Estado"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Gestor"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Transf"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Transferido"))
        layout.addWidget(QLineEdit())

        # Sección de Escaneos
        layout.addWidget(QLabel("Escaneos"))
        layout.addWidget(QLineEdit())
        
        layout.addWidget(self.crear_expediente_button)
        layout.addWidget(self.modificar_expediente_button)
        layout.addWidget(self.eliminar_expediente_button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    documentar_expediente_window = DocumentarExpedienteWindow()
    documentar_expediente_window.show()
    sys.exit(app.exec_())
