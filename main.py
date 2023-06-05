from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui_ui import Ui_gui
from plugins.aam.main import AAM
from plugins.csl.main import CSL
from plugins.fhc.main import FHC
from plugins.settings.main import Settings
from plugins.about.main import About

import os,sys,json

class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.subwin_aam=AAM(self.tab_1)
        self.subwin_csl=CSL(self.tab_2)
        self.subwin_fhc=FHC(self.tab_3)
        self.subwin_settings=Settings(self.tab_4,app,self)
        self.subwin_about=About(self.tab_5)

        self.pivot.addItem('aam','安卓应用管理',lambda:self.update_tab(0))
        self.pivot.addItem('csl','创建符号链接',lambda:self.update_tab(1))
        self.pivot.addItem('fhc','文件哈希校验',lambda:self.update_tab(2))
        self.pivot.addItem('settings','设置',lambda:self.update_tab(3))
        self.pivot.addItem('about','关于',lambda:self.update_tab(4))
        self.tabWidget.setCurrentIndex(0)

        app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__),'icon/toolbox.svg')))
        self.subwin_aam.btn_device.setIcon(QIcon(os.path.join(os.path.dirname(__file__),'icon','android.svg')))
        

        self.tabWidget.currentChanged.connect(self.window_size_change)
        self.window_size_change()

        self.drag_file = ''
        self.read_settings()
        
        self.show()

    def update_tab(self,tab_index:int):
        self.tabWidget.setCurrentIndex(tab_index)

    def read_settings(self):
        if os.path.isfile(os.path.join(path, '神龙工具箱', 'settings.json')):
            with open(os.path.join(path, '神龙工具箱', 'settings.json'), 'r')as file:
                data = json.load(file)
            try:
                {'Auto':self.subwin_settings.radio_auto,'Light':self.subwin_settings.radio_light,'Dark':self.subwin_settings.radio_dark}[data['theme']].setChecked(True)
                self.subwin_settings.ckb_enable_animation.setChecked(data['animation'][0])
                self.subwin_settings.cmb_animation.setCurrentText(data['animation'][1])
                self.subwin_settings.settings_change_status(False)
            except:
                print('配置文件异常，重置所有设置')
                self.subwin_settings.settings_change_status(False)
        else:
            try:os.mkdir(path)
            except:pass
            try:os.mkdir(os.path.join(path, '神龙工具箱'))
            except:pass
            with open(os.path.join(path, '神龙工具箱', 'settings.json'), 'w')as file:
                print('Successfully created the setting file')
            self.subwin_settings.settings_change_status(False)

    def save_settings(self):
        data = {'theme': self.subwin_settings.btn_group_theme.checkedButton().objectName()[6:].capitalize(),
                'animation': [self.subwin_settings.ckb_enable_animation.isChecked(), self.subwin_settings.cmb_animation.currentText()]}
        with open(os.path.join(path, '神龙工具箱', 'settings.json'), 'w')as file:
            json.dump(data, file)

    def window_size_change(self):
        self.animation = QPropertyAnimation(self, b'size')
        if self.subwin_settings.ckb_enable_animation.isChecked():
            self.animation.setDuration(500)
        else:
            self.animation.setDuration(0)
        self.animation.setEasingCurve(
            eval('QEasingCurve.'+self.subwin_settings.cmb_animation.currentText()))
        match self.tabWidget.currentIndex():
            case 0:
                self.animation.setEndValue(QSize(800, 500))
            case 1:
                self.animation.setEndValue(QSize(600, 50))
            case 2:
                self.animation.setEndValue(QSize(800, 600))
                self.subwin_fhc.fhc_table_update_size()
            case 3:
                self.animation.setEndValue(QSize(500, 75))
            case 4:
                self.animation.setEndValue(QSize(500,400))
        self.animation.start()

    def dragEnterEvent(self, event):
        drag_path = event.mimeData().urls()[0].toLocalFile()
        ext = os.path.splitext(drag_path)[1]
        if self.tabWidget.currentIndex() == 0 and ext == '.apk':
            event.accept()
            self.drag_file = drag_path
        if self.tabWidget.currentIndex()==1 and os.path.isdir(drag_path):
            event.accept()
            self.drag_file=drag_path
        elif self.tabWidget.currentIndex() == 2 and os.path.isfile(drag_path):
            event.accept()
            self.drag_file = drag_path
        else:
            event.ignore()
            self.drag_file = ''

    def dropEvent(self, event):
        if self.drag_file:
            if self.tabWidget.currentIndex() == 0:
                if self.subwin_aam.cmb_device.currentText():
                    if QMessageBox.question(self, '拖拽安装', f'你确认将\n{self.drag_file}\n安装到 {self.subwin_aam.cmb_device.currentText()} 上吗？') == QMessageBox.Yes:
                        self.subwin_aam.aam_install(self.drag_file)
                else:
                    QMessageBox.warning(self, '警告', '请先连接设备')

            elif self.tabWidget.currentIndex()==1:
                if self.subwin_csl.lineedit_from.hasFocus():
                    self.subwin_csl.lineedit_from.setText(self.drag_file)
                elif self.subwin_csl.lineedit_to_dir.hasFocus():
                    self.subwin_csl.lineedit_to_dir.setText(self.drag_file)

            elif self.tabWidget.currentIndex() == 2:
                if event.pos().x() <= self.width()//2:
                    self.subwin_fhc.lineedit_A.setPlainText(f'file:{self.drag_file}')
                else:
                    self.subwin_fhc.lineedit_B.setPlainText(f'file:{self.drag_file}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    path = os.path.expandvars(r'%appdata%/Avoconal')
    window = Main()

    sys.exit(app.exec())