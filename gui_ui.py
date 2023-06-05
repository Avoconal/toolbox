# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidgetItem, QMainWindow, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

from qfluentwidgets import Pivot

class Ui_gui(object):
    def setupUi(self, gui):
        if not gui.objectName():
            gui.setObjectName(u"gui")
        gui.resize(800, 500)
        gui.setAcceptDrops(True)
        self.centralwidget = QWidget(gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pivot = Pivot(self.centralwidget)
        self.pivot.setObjectName(u"pivot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pivot.sizePolicy().hasHeightForWidth())
        self.pivot.setSizePolicy(sizePolicy)
        self.pivot.setMinimumSize(QSize(0, 30))
        self.pivot.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.pivot)

        self.tabWidget = QStackedWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tabWidget.addWidget(self.tab_1)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addWidget(self.tab_2)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addWidget(self.tab_3)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addWidget(self.tab_4)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addWidget(self.tab_5)

        self.verticalLayout.addWidget(self.tabWidget)

        gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(gui)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"\u795e\u9f99\u5de5\u5177\u7bb1", None))
    # retranslateUi

