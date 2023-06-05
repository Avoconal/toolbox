from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .aam_ui import Ui_aam
from .wireless_ui import Ui_wireless

import os

class AAM(QWidget,Ui_aam):
    '''Android application manager'''
    def __init__(self,parent:QWidget):
        super().__init__()
        self.setupUi(parent)
        self.subwin_wireless=Wireless(self)
        self.signal_connect()

    def signal_connect(self):
        self.btn_wireless.clicked.connect(self.subwin_wireless.show)
        self.btn_device.clicked.connect(self.aam_device_update)
        self.btn_getapp_high.clicked.connect(self.aam_getapp_high)
        self.btn_getapp_low.clicked.connect(self.aam_getapp_low)
        self.btn_clear.clicked.connect(self.textedit_log.clear)
        self.btn_launch.clicked.connect(self.aam_launch)
        self.btn_extract.clicked.connect(self.aam_extract)
        self.btn_install.clicked.connect(self.aam_install)
        self.btn_uninstall.clicked.connect(self.aam_uninstall)
        self.btn_freeze.clicked.connect(self.aam_freeze)
        self.btn_unfreeze.clicked.connect(self.aam_unfreeze)
        self.btn_backup.clicked.connect(self.aam_backup)
        self.btn_restore.clicked.connect(self.aam_restore)

        self.cmb_device.currentIndexChanged.connect(self.aam_app_update)
        self.cmb_app.currentIndexChanged.connect(self.aam_app_update)


    def aam_read(self, ip, port):
        log = os.popen(f'adb connect {ip}:{port}').read()
        self.textedit_log.append(log)
        if self.cmb_device.findText(f'{ip}:{port}') == -1:
            QMessageBox.warning(self, '警告', '未能成功连接')
        self.aam_device_update()

    def aam_device_update(self):
        log = os.popen('adb devices').read()
        self.textedit_log.append(log)
        self.cmb_device.clear()
        if log.count('device') > 1:
            for i in log.split('\n')[1:]:
                if i:
                    self.cmb_device.addItem(i.split('\t')[0])
        else:
            QMessageBox.warning(self, '警告', '设备连接失败')

    def aam_app_update(self):
        if self.cmb_device.currentText():
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} shell pm list package').read()
            # self.aam.textedit_log.append(log)
            self.cmb_app.clear()
            self.cmb_app.addItems([i[8:] for i in log.split('\n')if i])
        else:
            QMessageBox.warning(self, '警告', '无法获取应用列表，请先连接设备')

    def aam_icon_update(self):
        if self.cmb_device.currentText():
            # 获取iconRes值
            log=os.popen(f'adb shell dumpsys package {self.cmb_app.currentText()}').read()
            iconRes='' 
            raise NotImplementedError
            self.textedit_log.append(log)
            # 还要提取字符！！！
            # 获取apk路径，不是包名
            log=os.popen(f'adb shell "pm path {self.cmb_app.currentText()} | findstr icon"')
            apk_path=''
            self.textedit_log.append(log)
            # 拉取文件 <apk_path>:icon=<iconRes>
            log=os.popen(f'adb pull {apk_path}:icon{iconRes}')

            # update icon
            self.label_app_name.setText(app_name)
            self.label_app_icon.setPixmap(QPixmap(f''))
            raise NotImplementedError


    def aam_getapp_high(self):
        log = os.popen(
            f'adb -s {self.cmb_device.currentText()} shell dumpsys activity |findstr "mResumedActivity"').read()
        if 'ActivityRecord' in log:
            self.textedit_log.append(log)
            log = log.split(' ')[7].split('/')[0]
            self.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aam_getapp_low(self):
        log = os.popen(
            f'adb -s {self.cmb_device.currentText()} shell dumpsys activity |findstr "mFocusedActivity"').read()
        if 'ActivityRecord' in log:
            self.textedit_log.append(log)
            log = log.split(' ')[7].split('/')[0]
            self.cmb_app.setCurrentText(log)
        else:
            QMessageBox.warning(self, '警告', '无法获取包名，确保手机处于亮屏状态')

    def aam_launch(self):
        if self.cmb_app.currentText():
            # 获取activity
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} shell monkey -p {self.cmb_app.currentText()} -v -v -v 1 | findstr "cmp="').read()
            # 启动应用
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} shell am start -n {log.split("cmp=")[1].split(" }")[0]}').read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_extract(self):
        if self.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} shell pm path {self.cmb_app.currentText()}').read()[8:]
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} pull {log}').read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_install(self, apk=''):
        if self.cmb_device.currentText():
            if apk:
                log = os.popen(
                    f'adb -s {self.cmb_device.currentText()} install "{apk}"').read()
                self.textedit_log.append(log)
            else:
                path = QFileDialog.getOpenFileName(
                    self, '请选择安装包', filter='安卓安装包 (*.apk)')[0]
                if path:
                    log = os.popen(
                        f'adb -s {self.cmb_device.currentText()} install "{path}"').read()
                    self.textedit_log.append(log)
                else:
                    QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先连接设备')

    def aam_uninstall(self):
        if self.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} uninstall {self.cmb_app.currentText()}').read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_freeze(self):
        if self.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} shell pm disable-user {self.cmb_app.currentText()}').read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_unfreeze(self):
        if self.cmb_app.currentText():
            log = os.popen(
                f'adb -s {self.cmb_device.currentText()} shell pm enable {self.cmb_app.currentText()}').read()
            self.textedit_log.append(log)
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_backup(self):
        if self.cmb_app.currentText():
            path = QFileDialog.getSaveFileName(
                self, '请选择备份文件保存位置', filter='安卓应用备份文件 (*.ab)')[0]
            if path:
                # -apk 含安装包备份
                log = os.popen(
                    f'adb -s {self.cmb_device.currentText()} backup -nosystem -noshared -f "{path}" {self.cmb_app.currentText()}').read()
                self.textedit_log.append(log)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先填写应用包名')

    def aam_restore(self):
        if self.cmb_app.currentText():
            path = QFileDialog.getOpenFileName(
                self, '请选择恢复文件位置', filter='安卓应用备份文件 (*.ab)')[0]
            if path:
                log = os.popen(
                    f'adb -s {self.cmb_device.currentText()} restore "{path}"').read()
                self.textedit_log.append(log)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先填写备份文件路径')

    def keyPressEvent(self, event):
        if self.lineedit_cmd.hasFocus():
            if event.key() == Qt.Key_Return:
                popen = os.popen(self.lineedit_cmd.text()).read()
                self.textedit_log.append(popen)

class Wireless(QMainWindow, Ui_wireless):
    def __init__(self,parent:AAM):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.parent=parent

    def closeEvent(self, event):
        self.hide()
        self.parent.aam_read(self.lineedit_ip.text(), self.lineedit_port.text())
