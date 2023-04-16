from PySide6.QtWidgets import QMessageBox


def MsgBoxConfirm(self, msg_info):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Question)
    msg.setStandardButtons(QMessageBox.YES | QMessageBox.NO)
    msg.setStyleSheet(u"QWidget {\n "
"   background-color: rgb(0, 95, 95); \n"
"   font: bold 12px;\n"
"	color: rgb(255, 255, 255);\n"
"}"
"   QPushButton {\n"
"   background-color: rgb(0, 70, 70); \n"
"   border-style: outset;\n"
"   border-width: 3px;\n"
"   border-radius: 8px;\n"
"   border-color: rgb(0, 172, 172);\n"
"   font: bold 12px;\n"
"	color: rgb(255, 255, 255);\n"
"   min-width: 3em;\n"
"   padding: 5px;\n"
"	text-align: center;\n"
"}"
"QPushButton:hover {\n"
"    background-color: rgb(0, 50, 50);\n"
"    border-style: inset;\n"
"}"
)
    msg.setWindowTitle('Confirmar')
    msg.setText(msg_info)
    msg.exec_()

def MsgBoxErro(self, msg_info):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Critical)

    msg.setStyleSheet(u"QWidget {\n "
"   background-color: rgb(0, 95, 95); \n"
"   font: bold 12px;\n"
"	color: rgb(255, 255, 255);\n"
"}"
"   QPushButton {\n"
"   background-color: rgb(0, 70, 70); \n"
"   border-style: outset;\n"
"   border-width: 3px;\n"
"   border-radius: 8px;\n"
"   border-color: rgb(0, 172, 172);\n"
"   font: bold 12px;\n"
"	color: rgb(255, 255, 255);\n"
"   min-width: 3em;\n"
"   padding: 5px;\n"
"	text-align: center;\n"
"}"
"QPushButton:hover {\n"
"    background-color: rgb(0, 50, 50);\n"
"    border-style: inset;\n"
"}"
)
    msg.setWindowTitle('Erro')
    msg.setText(msg_info)
    msg.exec_()

def MsgBoxInformation(self,msg_info):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Information)
    msg.setStyleSheet(u"QWidget {\n "
"   background-color: rgb(0, 95, 95); \n"
"   font: bold 12px;\n"
"	color: rgb(255, 255, 255);\n"
"}"
"   QPushButton {\n"
"   background-color: rgb(0, 70, 70); \n"
"   border-style: outset;\n"
"   border-width: 3px;\n"
"   border-radius: 8px;\n"
"   border-color: rgb(0, 172, 172);\n"
"   font: bold 12px;\n"
"	color: rgb(255, 255, 255);\n"
"   min-width: 3em;\n"
"   padding: 5px;\n"
"	text-align: center;\n"
"}"

"QPushButton:hover {\n"
"    background-color: rgb(0, 50, 50);\n"
"    border-style: inset;\n"
"}"
)
    msg.setWindowTitle('Concluido')
    msg.setText(msg_info)
    msg.exec_()