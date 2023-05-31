import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QCheckBox


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lions Cars - Inicio de Sesión")
        
        # Logo de la empresa
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap("logo.jpeg"))  # Asegúrate de tener el archivo "logo.jpeg" en el directorio
        
        # Campos de entrada de usuario y contraseña
        self.username_label = QLabel("Usuario:")
        self.username_edit = QLineEdit()
        self.password_label = QLabel("Contraseña:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        # Botón de inicio de sesión
        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.login)
        
        # Checkbox para recordar contraseña
        self.remember_checkbox = QCheckBox("Recordar contraseña")
        
        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.remember_checkbox)
        layout.addWidget(self.login_button)
        self.setLayout(layout)
    
    def login(self):
        
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Verificar el usuario y contraseña
        if username == "30715088527" and password == "lionscars2023":
            if self.remember_checkbox.isChecked():
                self.remember_password(username, password)
            self.close()  # Cierra la ventana de inicio de sesión
        else:
            QMessageBox.warning(self, "Inicio de Sesión", "Usuario o contraseña incorrectos.")

    
    def remember_password(self, username, password):
        # Guardar el usuario y contraseña en un archivo
        with open("credenciales.txt", "w") as file:
            file.write(f"{username}\n{password}")

    def load_remembered_password(self):
    # Cargar el usuario y contraseña recordados desde el archivo
        try:
            with open("credenciales.txt", "r") as file:
                lines = file.readlines()
                username = lines[0].strip()
                password = lines[1].strip()
                self.username_edit.setText(username)
                self.password_edit.setText(password)
                self.remember_checkbox.setChecked(True)
        except FileNotFoundError:
            pass





if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.load_remembered_password()  # Cargar los datos recordados
    login_window.show()
    sys.exit(app.exec_())

