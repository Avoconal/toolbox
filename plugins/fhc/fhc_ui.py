# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fhc.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QSizePolicy, QTableWidgetItem, QWidget)

from qfluentwidgets import (PlainTextEdit, PrimaryPushButton, TableWidget)

class Ui_fhc(object):
    def setupUi(self, fhc):
        if not fhc.objectName():
            fhc.setObjectName(u"fhc")
        fhc.resize(400, 300)
        self.gridLayout = QGridLayout(fhc)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(fhc)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)

        self.lineedit_A = PlainTextEdit(fhc)
        self.lineedit_A.setObjectName(u"lineedit_A")
        self.lineedit_A.setAcceptDrops(False)

        self.gridLayout.addWidget(self.lineedit_A, 1, 0, 1, 1)

        self.btn_A = PrimaryPushButton(fhc)
        self.btn_A.setObjectName(u"btn_A")

        self.gridLayout.addWidget(self.btn_A, 0, 0, 1, 1)

        self.tablewidget = TableWidget(fhc)
        if (self.tablewidget.columnCount() < 3):
            self.tablewidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tablewidget.rowCount() < 8):
            self.tablewidget.setRowCount(8)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        self.tablewidget.setObjectName(u"tablewidget")
        self.tablewidget.setColumnCount(3)
        self.tablewidget.horizontalHeader().setStretchLastSection(True)
        self.tablewidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tablewidget, 2, 0, 1, 3)

        self.lineedit_B = PlainTextEdit(fhc)
        self.lineedit_B.setObjectName(u"lineedit_B")
        self.lineedit_B.setAcceptDrops(False)

        self.gridLayout.addWidget(self.lineedit_B, 1, 2, 1, 1)

        self.btn_B = PrimaryPushButton(fhc)
        self.btn_B.setObjectName(u"btn_B")

        self.gridLayout.addWidget(self.btn_B, 0, 2, 1, 1)

        QWidget.setTabOrder(self.btn_A, self.lineedit_A)
        QWidget.setTabOrder(self.lineedit_A, self.btn_B)
        QWidget.setTabOrder(self.btn_B, self.lineedit_B)
        QWidget.setTabOrder(self.lineedit_B, self.tablewidget)

        self.retranslateUi(fhc)

        QMetaObject.connectSlotsByName(fhc)
    # setupUi

    def retranslateUi(self, fhc):
        fhc.setWindowTitle(QCoreApplication.translate("fhc", u"Form", None))
        self.btn_A.setText(QCoreApplication.translate("fhc", u"\u9009\u62e9\u6587\u4ef6", None))
        ___qtablewidgetitem = self.tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("fhc", u"A\u533a\u54c8\u5e0c\u503c", None));
        ___qtablewidgetitem1 = self.tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("fhc", u"\u6bd4\u8f83\u7ed3\u679c", None));
        ___qtablewidgetitem2 = self.tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("fhc", u"B\u533a\u54c8\u5e0c\u503c", None));
        ___qtablewidgetitem3 = self.tablewidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("fhc", u"\u5b57\u7b26\u6570", None));
        ___qtablewidgetitem4 = self.tablewidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("fhc", u"\u6587\u4ef6\u5927\u5c0f", None));
        ___qtablewidgetitem5 = self.tablewidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("fhc", u"md5", None));
        ___qtablewidgetitem6 = self.tablewidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("fhc", u"sha1", None));
        ___qtablewidgetitem7 = self.tablewidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("fhc", u"sha224", None));
        ___qtablewidgetitem8 = self.tablewidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("fhc", u"sha256", None));
        ___qtablewidgetitem9 = self.tablewidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("fhc", u"sha384", None));
        ___qtablewidgetitem10 = self.tablewidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("fhc", u"sha512", None));
        self.btn_B.setText(QCoreApplication.translate("fhc", u"\u9009\u62e9\u6587\u4ef6", None))
    # retranslateUi

