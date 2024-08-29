# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_AUTO = QPushButton(Form)
        self.pushButton_AUTO.setObjectName(u"pushButton_AUTO")

        self.verticalLayout.addWidget(self.pushButton_AUTO)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_scriptpath = QLineEdit(Form)
        self.lineEdit_scriptpath.setObjectName(u"lineEdit_scriptpath")

        self.horizontalLayout.addWidget(self.lineEdit_scriptpath)

        self.pushButton_runscript = QPushButton(Form)
        self.pushButton_runscript.setObjectName(u"pushButton_runscript")

        self.horizontalLayout.addWidget(self.pushButton_runscript)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_startrtab = QPushButton(Form)
        self.pushButton_startrtab.setObjectName(u"pushButton_startrtab")

        self.horizontalLayout_2.addWidget(self.pushButton_startrtab)

        self.pushButton_stoprtab = QPushButton(Form)
        self.pushButton_stoprtab.setObjectName(u"pushButton_stoprtab")

        self.horizontalLayout_2.addWidget(self.pushButton_stoprtab)

        self.pushButton_convertrtab = QPushButton(Form)
        self.pushButton_convertrtab.setObjectName(u"pushButton_convertrtab")

        self.horizontalLayout_2.addWidget(self.pushButton_convertrtab)

        self.pushButton_runpicking = QPushButton(Form)
        self.pushButton_runpicking.setObjectName(u"pushButton_runpicking")

        self.horizontalLayout_2.addWidget(self.pushButton_runpicking)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.message_broswer = QTextBrowser(Form)
        self.message_broswer.setObjectName(u"message_broswer")

        self.verticalLayout.addWidget(self.message_broswer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_AUTO.setText(QCoreApplication.translate("Form", u"Auto Run", None))
        self.label.setText(QCoreApplication.translate("Form", u"Robot Script Path", None))
        self.pushButton_runscript.setText(QCoreApplication.translate("Form", u"Run Robot Scirpt", None))
        self.pushButton_startrtab.setText(QCoreApplication.translate("Form", u"Start RTABmap to reconstruction", None))
        self.pushButton_stoprtab.setText(QCoreApplication.translate("Form", u"Stop Rtabmap SIGINT", None))
        self.pushButton_convertrtab.setText(QCoreApplication.translate("Form", u"Convert RTAB to Pointcloud", None))
        self.pushButton_runpicking.setText(QCoreApplication.translate("Form", u"Run PICKING", None))
        self.message_broswer.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Messages...</p></body></html>", None))
    # retranslateUi

