from PySide6.QtWidgets import *
from PySide6.QtCore import *

from .csl_ui import Ui_csl

import os

class CSL(QWidget,Ui_csl):
    '''create symbol link'''
    def __init__(self,parent:QWidget):
        super().__init__()
        self.setupUi(parent)
        self.signal_connect()

    def signal_connect(self):
        self.btn_to.clicked.connect(self.csl_select_to)
        self.btn_from.clicked.connect(self.csl_select_from)
        self.btn_start.clicked.connect(self.csl_start)

    def csl_select_from(self):
        path = QFileDialog.getExistingDirectory(self, '请选择本体路径')
        if path:
            self.lineedit_from.setText(path)
            self.lineedit_to_name.setText(os.path.split(path)[1])
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_select_to(self):
        path = QFileDialog.getExistingDirectory(self, '请选择目标路径')
        if path:
            self.lineedit_to_dir.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def csl_start(self):
        if self.lineedit_from.text() and self.lineedit_to_dir.text() and self.lineedit_to_name.text():
            log = os.popen(
                f'mklink /j "{self.lineedit_to_dir.text()}/{self.lineedit_to_name.text()}" "{self.lineedit_from.text()}"').read()
            if 'created' in log:
                QMessageBox.information(self, '成功', '符号链接创建成功')
            elif 'exists' in log:
                QMessageBox.warning(self, '警告', f'请勿选择已存在的目标路径\n{log}')
            elif 'NTFS' in log:
                QMessageBox.warning(self, '警告', f'请确保路径所在驱动盘为NTFS文件格式\n{log}')
            else:
                QMessageBox.warning(self, '警告', f'未知错误\n{log}')
        else:
            QMessageBox.warning(self, '警告', '请先选择本体路径与目标路径')

    def dragEnterEvent(self, event):
        raise NotImplementedError