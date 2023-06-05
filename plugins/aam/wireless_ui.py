# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wireless.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QWidget)

from qfluentwidgets import LineEdit

class Ui_wireless(object):
    def setupUi(self, wireless):
        if not wireless.objectName():
            wireless.setObjectName(u"wireless")
        wireless.resize(300, 100)
        wireless.setMinimumSize(QSize(300, 100))
        wireless.setMaximumSize(QSize(300, 100))
        self.centralwidget = QWidget(wireless)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_ip = QLabel(self.centralwidget)
        self.label_ip.setObjectName(u"label_ip")

        self.gridLayout.addWidget(self.label_ip, 0, 0, 1, 1)

        self.lineedit_ip = LineEdit(self.centralwidget)
        self.lineedit_ip.setObjectName(u"lineedit_ip")
        self.lineedit_ip.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_ip, 0, 1, 1, 1)

        self.label_port = QLabel(self.centralwidget)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout.addWidget(self.label_port, 1, 0, 1, 1)

        self.lineedit_port = LineEdit(self.centralwidget)
        self.lineedit_port.setObjectName(u"lineedit_port")
        self.lineedit_port.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_port, 1, 1, 1, 1)

        wireless.setCentralWidget(self.centralwidget)

        self.retranslateUi(wireless)

        QMetaObject.connectSlotsByName(wireless)
    # setupUi

    def retranslateUi(self, wireless):
        wireless.setWindowTitle(QCoreApplication.translate("wireless", u"\u65e0\u7ebf\u8c03\u8bd5", None))
        self.label_ip.setText(QCoreApplication.translate("wireless", u"ip\u5730\u5740\uff1a", None))
        self.lineedit_ip.setText(QCoreApplication.translate("wireless", u"127.0.0.1", None))
        self.label_port.setText(QCoreApplication.translate("wireless", u"\u7aef\u53e3\uff1a", None))
        self.lineedit_port.setText(QCoreApplication.translate("wireless", u"5555", None))
    # retranslateUi

