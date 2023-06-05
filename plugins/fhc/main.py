from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .fhc_ui import Ui_fhc

import os,sys,math,hashlib

class FHC(QWidget,Ui_fhc):
    '''file hash check'''
    def __init__(self,parent:QWidget):
        super().__init__()
        self.setupUi(parent)
        self.signal_connect()

    def signal_connect(self):
        self.btn_A.clicked.connect(self.fhc_select)
        self.btn_B.clicked.connect(self.fhc_select)
        self.lineedit_A.textChanged.connect(self.fhc_table_update_data)
        self.lineedit_B.textChanged.connect(self.fhc_table_update_data)
        self.tablewidget.currentItemChanged.connect(self.fhc_table_update_data)
    
    def fhc_select(self):
        section = self.lineedit_A if self.btn_A.hasFocus() else self.lineedit_B
        path = QFileDialog.getOpenFileName(self, '请选择文件')[0]
        if path:
            # with open(path, 'br')as file:
            #     section.setPlainText(str(file.read()))
            section.setPlainText('file:'+path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def fhc_get_hash(self, method: str, txt: str):
        if method+':' in txt:
            return [i[len(method)+1:] for i in txt.split('\n') if method+':' in i][0]
        elif 'file:' in txt and os.path.isfile([i[5:] for i in txt.split('\n') if 'file:' in i][0]):
            with open(txt[5:].split('\n')[0], 'rb')as file:
                txt = file.read()
        else:
            txt = txt.encode()

        if method == '字符数':
            try:
                return str(len(txt.decode()))
            except:
                return str(len(txt))+' 未解码'
        elif method == '文件大小':
            num = sys.getsizeof(txt)
            match math.floor(math.log(num, 1024)):
                case 0:
                    return f'{num} B'
                case 1:
                    return f'{round(num/1024,2)} KiB'
                case 2:
                    return f'{round(num/1024**2,2)} MiB'
                case 3:
                    return f'{round(num/1024**3,2)} GiB'
                case 4:
                    return f'{round(num/1024**3,2)} TiB'
        elif method == 'md5':
            return hashlib.md5(txt).hexdigest()
        elif method == 'sha1':
            return hashlib.sha1(txt).hexdigest()
        elif method == 'sha224':
            return hashlib.sha224(txt).hexdigest()
        elif method == 'sha256':
            return hashlib.sha256(txt).hexdigest()
        elif method == 'sha384':
            return hashlib.sha384(txt).hexdigest()
        elif method == 'sha512':
            return hashlib.sha512(txt).hexdigest()

    def fhc_table_update_size(self):
        self.tablewidget.setColumnWidth(
            0, self.tablewidget.width()*0.4)
        self.tablewidget.setColumnWidth(
            1, self.tablewidget.width()*0.1)
        self.tablewidget.setColumnWidth(
            2, self.tablewidget.width()*0.4)

    def fhc_table_update_data(self):
        self.tablewidget.clearContents()
        self.fhc_table_update_size()
        for i in range(self.tablewidget.rowCount()):

            if self.lineedit_A.toPlainText():
                self.tablewidget.setItem(i, 0, QTableWidgetItem(self.fhc_get_hash(
                    self.tablewidget.verticalHeaderItem(i).text(), self.lineedit_A.toPlainText())))
            if self.lineedit_B.toPlainText():
                self.tablewidget.setItem(i, 2, QTableWidgetItem(self.fhc_get_hash(
                    self.tablewidget.verticalHeaderItem(i).text(), self.lineedit_B.toPlainText())))

            if self.tablewidget.item(i, 0) != None and self.tablewidget.item(i, 2) != None:
                if self.tablewidget.item(i, 0).text() == self.tablewidget.item(i, 2).text():
                    self.tablewidget.setItem(
                        i, 1, QTableWidgetItem('True'))
                    self.tablewidget.item(
                        i, 1).setBackground(QColor('green'))
                else:
                    self.tablewidget.setItem(
                        i, 1, QTableWidgetItem('False'))
                    self.tablewidget.item(
                        i, 1).setBackground(QColor('red'))
            else:
                self.tablewidget.setItem(i, 1, QTableWidgetItem())
