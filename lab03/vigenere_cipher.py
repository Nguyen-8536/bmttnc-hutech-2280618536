import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.txt_ciphertext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(150, 290, 361, 111))
        self.txt_ciphertext.setObjectName("txt_ciphertext")

        self.txt_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(150, 230, 361, 31))
        self.txt_key.setObjectName("txt_key")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 60, 191, 21))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 61, 16))
        self.label_3.setObjectName("label_3")

        self.txt_plaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(150, 120, 361, 91))
        self.txt_plaintext.setObjectName("txt_plaintext")

        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(420, 470, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 280, 61, 16))
        self.label_5.setObjectName("label_5")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 91, 31))
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 230, 61, 16))
        self.label_4.setObjectName("label_4")

        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(150, 470, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")

        # Thêm label hiển thị trạng thái dưới ô Cipher Text
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(150, 410, 361, 20))
        self.label_status.setObjectName("label_status")
        self.label_status.setStyleSheet("color: green;")  # màu xanh cho thành công
        self.label_status.setText("")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vigenere Cipher"))
        self.label_2.setText(_translate("MainWindow", "TRƯƠNG ĐẠT NGUYÊN - 2280618536"))
        self.label_3.setText(_translate("MainWindow", "Plain Text"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_5.setText(_translate("MainWindow", "Cipher Text"))
        self.label.setText(_translate("MainWindow", "VIGENERE CIPHER"))
        self.label_4.setText(_translate("MainWindow", "Key"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label_status.setText("")  # lúc đầu để trống

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        plain_text = self.ui.txt_plaintext.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        self.ui.label_status.setText("")  # reset trạng thái

        if not plain_text or not key:
            QMessageBox.warning(self, "Input Error", "Plain Text and Key must not be empty.")
            return

        payload = {
            "plain_text": plain_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_ciphertext.setPlainText(data.get("encrypted_message", ""))
                self.ui.label_status.setStyleSheet("color: green;")
                self.ui.label_status.setText("Mã hóa thành công")
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                self.ui.label_status.setStyleSheet("color: red;")
                self.ui.label_status.setText(f"Lỗi khi gọi API: Status code {response.status_code}")
                QMessageBox.warning(self, "API Error", f"Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.ui.label_status.setStyleSheet("color: red;")
            self.ui.label_status.setText("Lỗi kết nối API")
            QMessageBox.warning(self, "Request Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        cipher_text = self.ui.txt_ciphertext.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        self.ui.label_status.setText("")  # reset trạng thái

        if not cipher_text or not key:
            QMessageBox.warning(self, "Input Error", "Cipher Text and Key must not be empty.")
            return

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setPlainText(data.get("decrypted_message", ""))
                self.ui.label_status.setStyleSheet("color: green;")
                self.ui.label_status.setText("Giải mã thành công")
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                self.ui.label_status.setStyleSheet("color: red;")
                self.ui.label_status.setText(f"Lỗi khi gọi API: Status code {response.status_code}")
                QMessageBox.warning(self, "API Error", f"Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.ui.label_status.setStyleSheet("color: red;")
            self.ui.label_status.setText("Lỗi kết nối API")
            QMessageBox.warning(self, "Request Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
