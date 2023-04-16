# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import assets.icons_rc

class Ui_TelaDownload(object):
    def setupUi(self, TelaDownload):
        if not TelaDownload.objectName():
            TelaDownload.setObjectName(u"TelaDownload")
        TelaDownload.resize(620, 480)
        TelaDownload.setMinimumSize(QSize(620, 480))
        TelaDownload.setMaximumSize(QSize(700, 500))
        TelaDownload.setStyleSheet(u"\n"
"#centralwidget{\n"
"  	background-color: rgb(0, 95, 95);\n"
"    border-style: outset;\n"
"    border-width:3px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 172, 172);\n"
"    min-width: 10em;\n"
"    padding: 10px;\n"
"	\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(TelaDownload)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(186, 450))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 310))
        self.frame_5.setStyleSheet(u"#lb_titulo{\n"
"    border-style: outset;\n"
"    border-width:8px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 172, 172);\n"
"    min-width: 10em;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width:3px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(0, 172, 172);\n"
" 	font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 18, 10, 0)
        self.lb_titulo = QLabel(self.frame_5)
        self.lb_titulo.setObjectName(u"lb_titulo")

        self.verticalLayout_4.addWidget(self.lb_titulo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.txt_link = QLineEdit(self.frame_5)
        self.txt_link.setObjectName(u"txt_link")

        self.verticalLayout_4.addWidget(self.txt_link)

        self.qf_rbtn = QFrame(self.frame_5)
        self.qf_rbtn.setObjectName(u"qf_rbtn")
        self.qf_rbtn.setMinimumSize(QSize(184, 100))
        self.qf_rbtn.setMaximumSize(QSize(184, 105))
        self.qf_rbtn.setStyleSheet(u"#qf_rbtn{\n"
"    border-style: outset;\n"
"    border-width:2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 172, 172);\n"
"    min-width: 10em;\n"
"    padding: 10px;\n"
"}\n"
"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 12px;\n"
"}")
        self.qf_rbtn.setFrameShape(QFrame.StyledPanel)
        self.qf_rbtn.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.qf_rbtn)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.rbtn_mp3 = QRadioButton(self.qf_rbtn)
        self.rbtn_mp3.setObjectName(u"rbtn_mp3")
        self.rbtn_mp3.setMinimumSize(QSize(0, 0))
        self.rbtn_mp3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.rbtn_mp3, 1, 0, 1, 1)

        self.rbtn_mp4 = QRadioButton(self.qf_rbtn)
        self.rbtn_mp4.setObjectName(u"rbtn_mp4")
        self.rbtn_mp4.setMinimumSize(QSize(0, 0))
        self.rbtn_mp4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.rbtn_mp4, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.qf_rbtn)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chb_baixar_playlist = QCheckBox(self.frame_4)
        self.chb_baixar_playlist.setObjectName(u"chb_baixar_playlist")
        self.chb_baixar_playlist.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: bold 12px;")

        self.horizontalLayout_3.addWidget(self.chb_baixar_playlist, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 2)

        self.lb_rbtn = QLabel(self.qf_rbtn)
        self.lb_rbtn.setObjectName(u"lb_rbtn")
        self.lb_rbtn.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_rbtn, 0, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.qf_rbtn, 0, Qt.AlignHCenter)

        self.btn_link = QPushButton(self.frame_5)
        self.btn_link.setObjectName(u"btn_link")
        font = QFont()
        font.setFamilies([u"11px"])
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        self.btn_link.setFont(font)
        self.btn_link.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 0px;\n"
"	background-color: rgb(0, 95, 95);\n"
"    border-color: rgb(0, 172, 172);\n"
"    font: bold italic underline 11px;\n"
"	color: rgb(255, 255, 255);\n"
"    min-width: 10em;\n"
"    padding: 5px 5px 5px 10px;\n"
"	text-align: left;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_link)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 172, 172);\n"
"    font: bold 14px;\n"
"	color: rgb(255, 255, 255);\n"
"    min-width: 10em;\n"
"    padding: 10px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton#btn_baixar{\n"
"    background-color: rgb(0, 200, 0);\n"
"}\n"
"\n"
"QPushButton#btn_baixar:pressed {\n"
"    background-color: rgb(0, 98, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton#btn_baixar:hover {\n"
"    background-color: rgb(0, 98, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton#btn_baixar:focus {\n"
"    background-color: rgb(0, 98, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton#btn_fechar{\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton#btn_fechar:pressed {\n"
"    background-color: rgb(144, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, 20)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_baixar = QPushButton(self.frame_3)
        self.btn_baixar.setObjectName(u"btn_baixar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_baixar.sizePolicy().hasHeightForWidth())
        self.btn_baixar.setSizePolicy(sizePolicy2)
        self.btn_baixar.setMinimumSize(QSize(216, 50))
        self.btn_baixar.setMaximumSize(QSize(200, 50))
        self.btn_baixar.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-baixar-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_baixar.setIcon(icon)
        self.btn_baixar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_baixar)

        self.btn_fechar = QPushButton(self.frame_3)
        self.btn_fechar.setObjectName(u"btn_fechar")
        sizePolicy2.setHeightForWidth(self.btn_fechar.sizePolicy().hasHeightForWidth())
        self.btn_fechar.setSizePolicy(sizePolicy2)
        self.btn_fechar.setMinimumSize(QSize(216, 50))
        self.btn_fechar.setMaximumSize(QSize(200, 50))
        self.btn_fechar.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-cancelar-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar.setIcon(icon1)
        self.btn_fechar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_fechar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.qf_status_bar = QFrame(self.frame)
        self.qf_status_bar.setObjectName(u"qf_status_bar")
        self.qf_status_bar.setFrameShape(QFrame.StyledPanel)
        self.qf_status_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.qf_status_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_status = QLabel(self.qf_status_bar)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(0, 40))
        self.lb_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lb_status)

        self.lb_status_2 = QLabel(self.qf_status_bar)
        self.lb_status_2.setObjectName(u"lb_status_2")
        self.lb_status_2.setMinimumSize(QSize(0, 40))
        self.lb_status_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lb_status_2)


        self.verticalLayout_2.addWidget(self.qf_status_bar)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: bold 9px;")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame)

        TelaDownload.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaDownload)

        QMetaObject.connectSlotsByName(TelaDownload)
    # setupUi

    def retranslateUi(self, TelaDownload):
        TelaDownload.setWindowTitle(QCoreApplication.translate("TelaDownload", u"MainWindow", None))
        self.lb_titulo.setText(QCoreApplication.translate("TelaDownload", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">YOU</span><span style=\" font-size:16pt; font-weight:700; color:#ff0000;\">TUBE </span><span style=\" font-size:14pt; font-weight:700; color:#00ffff;\">DOWNLOAD</span></p></body></html>", None))
        self.txt_link.setPlaceholderText(QCoreApplication.translate("TelaDownload", u"Informe o Link para Download", None))
        self.rbtn_mp3.setText(QCoreApplication.translate("TelaDownload", u"MP3", None))
        self.rbtn_mp4.setText(QCoreApplication.translate("TelaDownload", u"MP4", None))
        self.chb_baixar_playlist.setText(QCoreApplication.translate("TelaDownload", u"Baixar PlayList", None))
        self.lb_rbtn.setText(QCoreApplication.translate("TelaDownload", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Op\u00e7\u00f5es </span><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Download</span></p></body></html>", None))
        self.btn_link.setText(QCoreApplication.translate("TelaDownload", u"PushButton", None))
        self.btn_baixar.setText(QCoreApplication.translate("TelaDownload", u"BAIXAR", None))
        self.btn_fechar.setText(QCoreApplication.translate("TelaDownload", u"FECHAR", None))
#if QT_CONFIG(whatsthis)
        self.lb_status.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lb_status.setText(QCoreApplication.translate("TelaDownload", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">Download Iniciado.</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.lb_status_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lb_status_2.setText(QCoreApplication.translate("TelaDownload", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; font-style:italic; color:#ffffff;\">AGUARDE . . .</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("TelaDownload", u"Propriedades", None))
    # retranslateUi

