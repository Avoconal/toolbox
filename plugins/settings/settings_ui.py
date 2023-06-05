# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (CheckBox, ComboBox, PrimaryPushButton, RadioButton)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(400, 150)
        self.verticalLayout = QVBoxLayout(settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_theme = QLabel(settings)
        self.label_theme.setObjectName(u"label_theme")

        self.horizontalLayout.addWidget(self.label_theme)

        self.radio_auto = RadioButton(settings)
        self.btn_group_theme = QButtonGroup(settings)
        self.btn_group_theme.setObjectName(u"btn_group_theme")
        self.btn_group_theme.addButton(self.radio_auto)
        self.radio_auto.setObjectName(u"radio_auto")
        self.radio_auto.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_auto)

        self.radio_light = RadioButton(settings)
        self.btn_group_theme.addButton(self.radio_light)
        self.radio_light.setObjectName(u"radio_light")

        self.horizontalLayout.addWidget(self.radio_light)

        self.radio_dark = RadioButton(settings)
        self.btn_group_theme.addButton(self.radio_dark)
        self.radio_dark.setObjectName(u"radio_dark")

        self.horizontalLayout.addWidget(self.radio_dark)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_animation = QLabel(settings)
        self.label_animation.setObjectName(u"label_animation")

        self.horizontalLayout_2.addWidget(self.label_animation)

        self.ckb_enable_animation = CheckBox(settings)
        self.ckb_enable_animation.setObjectName(u"ckb_enable_animation")
        self.ckb_enable_animation.setChecked(True)

        self.horizontalLayout_2.addWidget(self.ckb_enable_animation)

        self.cmb_animation = ComboBox(settings)
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.addItem("")
        self.cmb_animation.setObjectName(u"cmb_animation")

        self.horizontalLayout_2.addWidget(self.cmb_animation)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget = QWidget(settings)
        self.widget.setObjectName(u"widget")
        self.btn_animation_example = PrimaryPushButton(self.widget)
        self.btn_animation_example.setObjectName(u"btn_animation_example")
        self.btn_animation_example.setGeometry(QRect(10, 10, 24, 22))

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(settings)

        self.cmb_animation.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Form", None))
        self.label_theme.setText(QCoreApplication.translate("settings", u"\u4e3b\u9898\uff1a", None))
        self.radio_auto.setText(QCoreApplication.translate("settings", u"\u8ddf\u968f\u7cfb\u7edf", None))
        self.radio_light.setText(QCoreApplication.translate("settings", u"\u6d45\u8272", None))
        self.radio_dark.setText(QCoreApplication.translate("settings", u"\u6df1\u8272", None))
        self.label_animation.setText(QCoreApplication.translate("settings", u"\u52a8\u753b\uff1a", None))
        self.ckb_enable_animation.setText(QCoreApplication.translate("settings", u"\u5f00\u542f\u52a8\u753b", None))
        self.cmb_animation.setItemText(0, QCoreApplication.translate("settings", u"Linear", None))
        self.cmb_animation.setItemText(1, QCoreApplication.translate("settings", u"InOutQuad", None))
        self.cmb_animation.setItemText(2, QCoreApplication.translate("settings", u"InOutCubic", None))
        self.cmb_animation.setItemText(3, QCoreApplication.translate("settings", u"InOutSine", None))
        self.cmb_animation.setItemText(4, QCoreApplication.translate("settings", u"InOutElastic", None))
        self.cmb_animation.setItemText(5, QCoreApplication.translate("settings", u"InOutBack", None))
        self.cmb_animation.setItemText(6, QCoreApplication.translate("settings", u"InOutBounce", None))

        self.btn_animation_example.setText(QCoreApplication.translate("settings", u"-", None))
    # retranslateUi

