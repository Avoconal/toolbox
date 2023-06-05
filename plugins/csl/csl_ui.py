# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'csl.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton)

class Ui_csl(object):
    def setupUi(self, csl):
        if not csl.objectName():
            csl.setObjectName(u"csl")
        csl.resize(884, 601)
        self.gridLayout = QGridLayout(csl)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_start = PrimaryPushButton(csl)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(100, 0))
        self.btn_start.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.btn_start, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_to = PushButton(csl)
        self.btn_to.setObjectName(u"btn_to")
        self.btn_to.setMaximumSize(QSize(120, 16777215))
        self.btn_to.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.btn_to)

        self.lineedit_to_dir = LineEdit(csl)
        self.lineedit_to_dir.setObjectName(u"lineedit_to_dir")
        self.lineedit_to_dir.setAlignment(Qt.AlignCenter)
        self.lineedit_to_dir.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineedit_to_dir)

        self.label_sep = QLabel(csl)
        self.label_sep.setObjectName(u"label_sep")

        self.horizontalLayout_2.addWidget(self.label_sep)

        self.lineedit_to_name = LineEdit(csl)
        self.lineedit_to_name.setObjectName(u"lineedit_to_name")
        self.lineedit_to_name.setAlignment(Qt.AlignCenter)
        self.lineedit_to_name.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineedit_to_name)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.btn_from = PushButton(csl)
        self.btn_from.setObjectName(u"btn_from")
        self.btn_from.setMaximumSize(QSize(120, 16777215))
        self.btn_from.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_1.addWidget(self.btn_from)

        self.lineedit_from = LineEdit(csl)
        self.lineedit_from.setObjectName(u"lineedit_from")
        self.lineedit_from.setAlignment(Qt.AlignCenter)
        self.lineedit_from.setClearButtonEnabled(True)

        self.horizontalLayout_1.addWidget(self.lineedit_from)


        self.gridLayout.addLayout(self.horizontalLayout_1, 0, 0, 1, 3)

        QWidget.setTabOrder(self.btn_from, self.lineedit_from)
        QWidget.setTabOrder(self.lineedit_from, self.btn_to)
        QWidget.setTabOrder(self.btn_to, self.lineedit_to_dir)
        QWidget.setTabOrder(self.lineedit_to_dir, self.lineedit_to_name)
        QWidget.setTabOrder(self.lineedit_to_name, self.btn_start)

        self.retranslateUi(csl)

        QMetaObject.connectSlotsByName(csl)
    # setupUi

    def retranslateUi(self, csl):
        csl.setWindowTitle(QCoreApplication.translate("csl", u"Form", None))
        self.btn_start.setText(QCoreApplication.translate("csl", u"\u521b\u5efa", None))
        self.btn_to.setText(QCoreApplication.translate("csl", u"\u9009\u62e9\u76ee\u6807\u8def\u5f84", None))
        self.lineedit_to_dir.setPlaceholderText(QCoreApplication.translate("csl", u"\u8bf7\u5148\u9009\u62e9\u76ee\u6807\u7236\u8def\u5f84", None))
        self.label_sep.setText(QCoreApplication.translate("csl", u"\\", None))
        self.lineedit_to_name.setPlaceholderText(QCoreApplication.translate("csl", u"\u76ee\u6807\u540d\u79f0", None))
        self.btn_from.setText(QCoreApplication.translate("csl", u"\u9009\u62e9\u672c\u4f53\u8def\u5f84", None))
        self.lineedit_from.setPlaceholderText(QCoreApplication.translate("csl", u"\u8bf7\u5148\u9009\u62e9\u672c\u4f53\u8def\u5f84", None))
    # retranslateUi

