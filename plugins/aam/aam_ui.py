# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aam.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, EditableComboBox, LineEdit, PrimaryPushButton,
    PushButton, TextEdit)

class Ui_aam(object):
    def setupUi(self, aam):
        if not aam.objectName():
            aam.setObjectName(u"aam")
        aam.resize(800, 500)
        self.verticalLayout_2 = QVBoxLayout(aam)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.btn_device = PushButton(aam)
        self.btn_device.setObjectName(u"btn_device")
        self.btn_device.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_1.addWidget(self.btn_device)

        self.cmb_device = ComboBox(aam)
        self.cmb_device.setObjectName(u"cmb_device")

        self.horizontalLayout_1.addWidget(self.cmb_device)

        self.btn_wireless = PushButton(aam)
        self.btn_wireless.setObjectName(u"btn_wireless")
        self.btn_wireless.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_1.addWidget(self.btn_wireless)


        self.verticalLayout_2.addLayout(self.horizontalLayout_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_app = QLabel(aam)
        self.label_app.setObjectName(u"label_app")
        self.label_app.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.label_app)

        self.cmb_app = EditableComboBox(aam)
        self.cmb_app.setObjectName(u"cmb_app")

        self.horizontalLayout.addWidget(self.cmb_app)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_app_icon = QLabel(aam)
        self.label_app_icon.setObjectName(u"label_app_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_app_icon.sizePolicy().hasHeightForWidth())
        self.label_app_icon.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_app_icon)

        self.label_app_name = QLabel(aam)
        self.label_app_name.setObjectName(u"label_app_name")
        sizePolicy.setHeightForWidth(self.label_app_name.sizePolicy().hasHeightForWidth())
        self.label_app_name.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_app_name)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.btn_install = PrimaryPushButton(aam)
        self.btn_install.setObjectName(u"btn_install")

        self.gridLayout_1.addWidget(self.btn_install, 1, 4, 1, 1)

        self.btn_extract = PrimaryPushButton(aam)
        self.btn_extract.setObjectName(u"btn_extract")

        self.gridLayout_1.addWidget(self.btn_extract, 2, 0, 1, 1)

        self.btn_backup = PrimaryPushButton(aam)
        self.btn_backup.setObjectName(u"btn_backup")

        self.gridLayout_1.addWidget(self.btn_backup, 1, 7, 1, 1)

        self.btn_unfreeze = PrimaryPushButton(aam)
        self.btn_unfreeze.setObjectName(u"btn_unfreeze")

        self.gridLayout_1.addWidget(self.btn_unfreeze, 2, 6, 1, 1)

        self.btn_getapp_low = PrimaryPushButton(aam)
        self.btn_getapp_low.setObjectName(u"btn_getapp_low")

        self.gridLayout_1.addWidget(self.btn_getapp_low, 1, 10, 1, 1)

        self.btn_launch = PrimaryPushButton(aam)
        self.btn_launch.setObjectName(u"btn_launch")

        self.gridLayout_1.addWidget(self.btn_launch, 1, 0, 1, 1)

        self.btn_getapp_high = PrimaryPushButton(aam)
        self.btn_getapp_high.setObjectName(u"btn_getapp_high")

        self.gridLayout_1.addWidget(self.btn_getapp_high, 2, 10, 1, 1)

        self.btn_restore = PrimaryPushButton(aam)
        self.btn_restore.setObjectName(u"btn_restore")

        self.gridLayout_1.addWidget(self.btn_restore, 2, 7, 1, 1)

        self.btn_uninstall = PrimaryPushButton(aam)
        self.btn_uninstall.setObjectName(u"btn_uninstall")

        self.gridLayout_1.addWidget(self.btn_uninstall, 2, 4, 1, 1)

        self.btn_freeze = PrimaryPushButton(aam)
        self.btn_freeze.setObjectName(u"btn_freeze")

        self.gridLayout_1.addWidget(self.btn_freeze, 1, 6, 1, 1)

        self.btn_clear = PushButton(aam)
        self.btn_clear.setObjectName(u"btn_clear")

        self.gridLayout_1.addWidget(self.btn_clear, 1, 11, 2, 1)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_1, 1, 9, 2, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_1)

        self.textedit_log = TextEdit(aam)
        self.textedit_log.setObjectName(u"textedit_log")
        self.textedit_log.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textedit_log)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_cmd = QLabel(aam)
        self.label_cmd.setObjectName(u"label_cmd")

        self.horizontalLayout_3.addWidget(self.label_cmd)

        self.lineedit_cmd = LineEdit(aam)
        self.lineedit_cmd.setObjectName(u"lineedit_cmd")
        self.lineedit_cmd.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineedit_cmd)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        QWidget.setTabOrder(self.btn_device, self.cmb_device)
        QWidget.setTabOrder(self.cmb_device, self.btn_wireless)
        QWidget.setTabOrder(self.btn_wireless, self.cmb_app)
        QWidget.setTabOrder(self.cmb_app, self.btn_launch)
        QWidget.setTabOrder(self.btn_launch, self.btn_extract)
        QWidget.setTabOrder(self.btn_extract, self.btn_install)
        QWidget.setTabOrder(self.btn_install, self.btn_uninstall)
        QWidget.setTabOrder(self.btn_uninstall, self.btn_freeze)
        QWidget.setTabOrder(self.btn_freeze, self.btn_unfreeze)
        QWidget.setTabOrder(self.btn_unfreeze, self.btn_backup)
        QWidget.setTabOrder(self.btn_backup, self.btn_restore)
        QWidget.setTabOrder(self.btn_restore, self.btn_getapp_low)
        QWidget.setTabOrder(self.btn_getapp_low, self.btn_getapp_high)
        QWidget.setTabOrder(self.btn_getapp_high, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.textedit_log)
        QWidget.setTabOrder(self.textedit_log, self.lineedit_cmd)

        self.retranslateUi(aam)

        QMetaObject.connectSlotsByName(aam)
    # setupUi

    def retranslateUi(self, aam):
        aam.setWindowTitle(QCoreApplication.translate("aam", u"Form", None))
        self.btn_device.setText(QCoreApplication.translate("aam", u"\u5237\u65b0\u8fde\u63a5\u8bbe\u5907", None))
        self.btn_wireless.setText(QCoreApplication.translate("aam", u"\u65e0\u7ebf\u8c03\u8bd5", None))
        self.label_app.setText(QCoreApplication.translate("aam", u"\u5e94\u7528\u5305\u540d\uff1a", None))
        self.label_app_icon.setText("")
        self.label_app_name.setText("")
        self.btn_install.setText(QCoreApplication.translate("aam", u"\u5b89\u88c5", None))
        self.btn_extract.setText(QCoreApplication.translate("aam", u"\u63d0\u53d6", None))
        self.btn_backup.setText(QCoreApplication.translate("aam", u"\u5907\u4efd", None))
        self.btn_unfreeze.setText(QCoreApplication.translate("aam", u"\u89e3\u51bb", None))
        self.btn_getapp_low.setText(QCoreApplication.translate("aam", u"\u83b7\u53d6\u5305\u540d(\u4f4e\u7248\u672c)", None))
        self.btn_launch.setText(QCoreApplication.translate("aam", u"\u542f\u52a8", None))
        self.btn_getapp_high.setText(QCoreApplication.translate("aam", u"\u83b7\u53d6\u5305\u540d(\u9ad8\u7248\u672c)", None))
        self.btn_restore.setText(QCoreApplication.translate("aam", u"\u6062\u590d", None))
        self.btn_uninstall.setText(QCoreApplication.translate("aam", u"\u5378\u8f7d", None))
        self.btn_freeze.setText(QCoreApplication.translate("aam", u"\u51bb\u7ed3", None))
        self.btn_clear.setText(QCoreApplication.translate("aam", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.textedit_log.setHtml(QCoreApplication.translate("aam", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">\u795e\u9f99\u5de5\u5177\u7bb1 v2.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">\u4f5c\u8005\uff1aabcdesteve</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">    _                                   _   ____   ___ ____  _____ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">   / \\__   _____   ___ ___  _ __   __ _| | |___ \\ / _ \\___ \\|___ / </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">  / _ \\ \\ / / _ \\ / __/ _ \\| '_ \\ / _` | |   __) | | | |__) | |_ \\ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\"> / ___ \\ V / (_) | (_| (_) | | | | (_| | |  / __/| |_| / __/ ___) |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">/_/   \\_\\_/ \\___/ \\___\\___/|_| |_|\\__,_|_| |_____|\\___/_____|____/ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">   _   _ _       _      _   _                                       _ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">  /_\\ | | |  _ _(_)__ _| |_| |_ ___  _ _ ___ ___ ___ _ ___ _____ __| |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\"> / _ \\| | | | '_| / _` | ' \\  _(_-&lt; | '_/ -_|_-&lt;/ -_) '_\\ V / -_) _` |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">/_/ \\_\\_|_| |_| |_\\__, |_||_\\__/__/ |_| \\___/__/\\___|_|  \\_/\\___\\__,_|</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FiraCode Nerd Font';\">                  |___/                                               </span></p></body></html>", None))
        self.label_cmd.setText(QCoreApplication.translate("aam", u"\u8fd0\u884c\u547d\u4ee4\uff1a", None))
    # retranslateUi

