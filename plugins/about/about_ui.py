# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)

from qfluentwidgets import (PrimaryPushButton, PushButton, TextEdit)

class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(400, 300)
        self.gridLayout = QGridLayout(about)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = TextEdit(about)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 3)

        self.btn_github = PrimaryPushButton(about)
        self.btn_github.setObjectName(u"btn_github")

        self.gridLayout.addWidget(self.btn_github, 1, 0, 1, 1)

        self.btn_bilibili = PushButton(about)
        self.btn_bilibili.setObjectName(u"btn_bilibili")

        self.gridLayout.addWidget(self.btn_bilibili, 1, 1, 1, 1)

        self.btn_tour = PushButton(about)
        self.btn_tour.setObjectName(u"btn_tour")

        self.gridLayout.addWidget(self.btn_tour, 1, 2, 1, 1)


        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"Form", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("about", u"# v1.0\n"
"\n"
"- \u5b89\u5353\u5e94\u7528\u6570\u636e\u5907\u4efd\n"
"- \u6587\u4ef6\u8f6f\u94fe\u63a5\n"
"\n"
"# v1.1\n"
"\n"
"- *~~\u5b89\u5353\u5e94\u7528\u6570\u636e\u5907\u4efd*~~ --> \u5b89\u5353\u5e94\u7528\u7ba1\u7406\n"
"- \u65b0\u589e\u5b89\u88c5\u3001\u5378\u8f7d\u3001\u51bb\u7ed3\u3001\u89e3\u51bb\u3001\u547d\u4ee4\u884c\u7b49\u529f\u80fd\n"
"- \u66f4\u6539\u4e86 ***\u6697\u9ed1\u4e3b\u9898*** `qdarkstyle`\n"
"\n"
"# v1.2\n"
"\n"
"- \u65b0\u589e\u6587\u4ef6\u6821\u9a8c\u529f\u80fd\n"
"- \u65b0\u589e\u8bbe\u7f6e\uff0c\u652f\u6301\u672c\u5730\u4fdd\u5b58\n"
"- \u5141\u8bb8\u81ea\u5b9a\u4e49\u4e3b\u9898\u548c\u52a8\u753b\n"
"- \u65b0\u589e\u6587\u4ef6\u62d6\u62fd\u6821\u9a8c\n"
"- \u65b0\u589eapk\u62d6\u62fd\u5b89\u88c5\n"
"\n"
"# v2.0\n"
"\n"
"- \u66f4\u6362\u8bbe\u8ba1\u98ce\u683c\u4e3a `fluent design`\n"
"- \u4fee\u590d [v1.2\u7248\u672c](#v12) \u4e2d [fhc\u7ec4\u4ef6](#\u63d2\u4ef6\u540d\u79f0\u5bf9\u5e94\u8868) \u62d6\u62fd\u6587\u4ef6\u53d8\u4e3a `file:///` \u7684bug\n"
"- \u5c06\u5404\u7a97\u53e3"
                        "\u72ec\u7acb\u4e3aplugins,\u51cf\u5c11 [main.py](main.py) \u4e2d\u7684\u4ee3\u7801\n"
"- [csl\u7ec4\u4ef6](#\u63d2\u4ef6\u540d\u79f0\u5bf9\u5e94\u8868) \u652f\u6301\u62d6\u62fd\u6587\u4ef6\u5939\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">v1.0</span></h1>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5b89\u5353\u5e94\u7528\u6570\u636e\u5907\u4efd</li>\n"
"<li style=\" margin-top:6"
                        "px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6587\u4ef6\u8f6f\u94fe\u63a5</li></ul>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">v1.1</span></h1>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">~~\u5b89\u5353\u5e94\u7528\u6570\u636e\u5907\u4efd</span>~~ --&gt; \u5b89\u5353\u5e94\u7528\u7ba1\u7406</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65b0\u589e\u5b89\u88c5\u3001\u5378\u8f7d\u3001\u51bb\u7ed3\u3001\u89e3\u51bb\u3001\u547d\u4ee4\u884c\u7b49\u529f\u80fd</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u66f4\u6539\u4e86 <span style=\" font-weight:700; font-style:italic;\">\u6697\u9ed1\u4e3b\u9898</span> <span style=\" font-family:'Courier New';\">qdarkstyle</span></li></ul>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">v1.2</span></h1>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65b0\u589e\u6587\u4ef6\u6821\u9a8c\u529f\u80fd</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65b0\u589e\u8bbe\u7f6e\uff0c\u652f\u6301\u672c\u5730\u4fdd\u5b58</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px;\">\u5141\u8bb8\u81ea\u5b9a\u4e49\u4e3b\u9898\u548c\u52a8\u753b</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65b0\u589e\u6587\u4ef6\u62d6\u62fd\u6821\u9a8c</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65b0\u589eapk\u62d6\u62fd\u5b89\u88c5</li></ul>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">v2.0</span></h1>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u66f4\u6362\u8bbe\u8ba1\u98ce\u683c\u4e3a <span style=\" font-family:'Courier New';\">fluent design</span></li>\n"
"<li style=\" "
                        "margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4fee\u590d <a href=\"#v12\"><span style=\" text-decoration: underline; color:#0000ff;\">v1.2\u7248\u672c</span></a> \u4e2d <a href=\"#\u63d2\u4ef6\u540d\u79f0\u5bf9\u5e94\u8868\"><span style=\" text-decoration: underline; color:#0000ff;\">fhc\u7ec4\u4ef6</span></a> \u62d6\u62fd\u6587\u4ef6\u53d8\u4e3a <span style=\" font-family:'Courier New';\">file:///</span> \u7684bug</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5c06\u5404\u7a97\u53e3\u72ec\u7acb\u4e3aplugins,\u51cf\u5c11 <a href=\"main.py\"><span style=\" text-decoration: underline; color:#0000ff;\">main.py</span></a> \u4e2d\u7684\u4ee3\u7801</li>\n"
"<li style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#\u63d2\u4ef6\u540d\u79f0\u5bf9\u5e94\u8868\"><span style=\" text-decoration: unde"
                        "rline; color:#0000ff;\">csl\u7ec4\u4ef6</span></a> \u652f\u6301\u62d6\u62fd\u6587\u4ef6\u5939</li></ul></body></html>", None))
        self.btn_github.setText(QCoreApplication.translate("about", u"GitHub\u4ed3\u5e93", None))
        self.btn_bilibili.setText(QCoreApplication.translate("about", u"B\u7ad9\u4e3b\u9875", None))
        self.btn_tour.setText(QCoreApplication.translate("about", u"\u89c6\u9891\u4ecb\u7ecd", None))
    # retranslateUi

