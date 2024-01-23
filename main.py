from PyQt5 import QtWidgets, QtGui, QtCore, uic
from windows.main_window import Ui_MainWindow
from windows.start_window import Ui_StartWindow
import configparser
import os
import sqlite3
import sys
from ACR import AutoClickerR

ACTIONS = list()
IMAGES = list()
PROJECT_PATH = str()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, path=''):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons/icon.svg'))

        self.ui.newfile_Button.setIcon(QtGui.QIcon('icons/new_file.png'))
        self.ui.newfile_Button.setIconSize(QtCore.QSize(23, 23))
        self.ui.newfile_Button.clicked.connect(self.create_project)
        self.ui.save_Button.setIcon(QtGui.QIcon('icons/save.svg'))
        self.ui.save_Button.setIconSize(QtCore.QSize(18, 18))
        self.ui.open_Button.setIcon(QtGui.QIcon('icons/open.svg'))
        self.ui.open_Button.setIconSize(QtCore.QSize(23, 23))
        self.ui.open_Button.clicked.connect(self.open_act)
        self.ui.settings_Button.setIcon(QtGui.QIcon('icons/settings.svg'))
        self.ui.settings_Button.setIconSize(QtCore.QSize(20, 20))
        self.ui.resources_Button.setIcon((QtGui.QIcon('icons/picture.svg')))
        self.ui.resources_Button.setIconSize(QtCore.QSize(18, 18))
        self.ui.resources_Button.clicked.connect(self.open_resources)
        self.ui.updateimg_Button.setIcon(QtGui.QIcon('icons/reload.svg'))
        self.ui.updateimg_Button.setIconSize(QtCore.QSize(18, 18))
        self.ui.updateimg_Button.clicked.connect(self.updateImages)
        self.ui.info_Button.setIcon(QtGui.QIcon('icons/info.svg'))
        self.ui.info_Button.setIconSize(QtCore.QSize(20, 20))

        self.ui.delete_action_pushButton.clicked.connect(self.delete_action)
        self.ui.copy_action_pushButton.clicked.connect(self.copy_action)
        self.ui.new_action_puchButton.clicked.connect(self.new_action)
        self.ui.saveaction_Button.clicked.connect(self.save_action)
        self.ui.actions_listWidget.currentItemChanged.connect(self.currentItemChanged)
        self.ui.add_hotkey_pushButton.clicked.connect(self.add_hotkey)
        self.ui.add_hotkey_symbol_pushButton.clicked.connect(self.add_symbol_hotkey)
        self.ui.delete_hotkey_pushButton.clicked.connect(self.delete_hotkey)
        self.ui.add_delay_Button.clicked.connect(self.add_delay)
        self.ui.save_Button.clicked.connect(self.saveProject)
        self.ui.start_Button.clicked.connect(self.start)

        self.ui.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.ui.tray_icon.setIcon(QtGui.QIcon('icons/icon.svg'))

        for i in range(self.ui.actions_tabWidget.count()):
            self.ui.actions_tabWidget.setTabEnabled(i, False)

        self.ui.hotkey_comboBox.addItems(['', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps',
                                          'backspace',
                                          'browserback', 'browserfavorites', 'browserforward', 'browserhome',
                                          'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
                                          'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
                                          'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
                                          'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
                                          'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                                          'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert',
                                          'junja',
                                          'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
                                          'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                                          'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
                                          'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
                                          'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
                                          'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
                                          'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract',
                                          'tab',
                                          'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright',
                                          'yen',
                                          'command', 'option', 'optionleft', 'optionright'])

        if path != '':
            self.open(path)

    def start(self):
        global ACTIONS
        try:
            ACTIONS_ORDER = [str(self.ui.actions_listWidget.item(i).text()) for i in
                             range(self.ui.actions_listWidget.count())]
            self.showMinimized()
            acr = AutoClickerR()
            for i in ACTIONS_ORDER:
                for action in ACTIONS:
                    if i == action['name']:
                        if action['action'] == 'click':
                            print(action['image'])
                            acr.click(button=action['button'], img=action['image'], click_num=action['click_num'],
                                      duration=action['duration'], interval=action['interval'], id=action['index'])
                        elif action['action'] == 'write':
                            acr.write(action['text'], action['interval'])
                        elif action['action'] == 'scroll':
                            acr.scroll(action['scroll'])
        except BaseException as e:
            print('fgg:', e)

    def set_icons(self):
        global ACTIONS
        for i in range(self.ui.actions_listWidget.count()):
            for j in ACTIONS:
                if self.ui.actions_listWidget.item(i).text() == j['name']:
                    if j['action'] == 'click':
                        self.ui.actions_listWidget.item(i).setIcon(QtGui.QIcon('icons/cursor.svg'))
                    elif j['action'] == 'write':
                        self.ui.actions_listWidget.item(i).setIcon(QtGui.QIcon('icons/keyboard.svg'))
                    elif j['action'] == 'press':
                        self.ui.actions_listWidget.item(i).setIcon(QtGui.QIcon('icons/hotkey.png'))
                    elif j['action'] == 'dad':
                        self.ui.actions_listWidget.item(i).setIcon(QtGui.QIcon('icons/drag.svg'))

    def add_delay(self):
        global ACTIONS
        self.ui.actions_listWidget.addItem('Delay ' + str(self.ui.delay_SpinBox.value()))
        ACTIONS.append(
            {'name': 'Delay ' + str(self.ui.delay_SpinBox.value()), 'action': None, 'button': None, 'duration': None,
             'threshold': None, 'click_num': None, 'interval': None, 'text': None, 'keys': None, 'scroll': None,
             'index': None, 'image': None, 'delay': self.ui.delay_SpinBox.value()})
        self.ui.delay_SpinBox.setValue(0)

    def new_action(self):
        for i in range(self.ui.actions_tabWidget.count()):
            self.ui.actions_tabWidget.setTabEnabled(i, True)
        self.updateImages()
        self.ui.actions_listWidget.addItem('...')
        self.ui.actions_listWidget.setCurrentRow(self.ui.actions_listWidget.count() - 1)
        self.ui.button_comboBox.setCurrentIndex(0)
        self.ui.threshold_doubleSpinBox.setValue(0)
        self.ui.duration_doubleSpinBox.setValue(0)
        self.ui.clicknum_spinBox.setValue(0)
        self.ui.interval_doubleSpinBox.setValue(0)
        self.ui.name_lineEdit.setText('')
        self.ui.plainTextEdit.setPlainText('')
        self.ui.interval_doubleSpinBox_2.setValue(0)
        self.ui.hotkeys_listWidget.clear()
        self.ui.hotkey_comboBox.setCurrentIndex(0)
        self.ui.hotkey_lineEdit.setText('')
        self.ui.scroll_spinBox.setValue(0)
        self.ui.duration_dad_doubleSpinBox.setValue(0)

    def copy_action(self):
        if self.ui.actions_listWidget.currentItem().text() != '...':
            self.ui.actions_listWidget.addItem(self.ui.actions_listWidget.currentItem().text())
            self.set_icons()

    def delete_action(self):
        global ACTIONS
        try:
            self.ui.actions_listWidget.takeItem(self.ui.actions_listWidget.currentRow())
            ACTIONS.pop(self.ui.actions_listWidget.currentRow())
        except BaseException as error:
            print(error)

    def delete_hotkey(self):
        self.ui.hotkeys_listWidget.takeItem(self.ui.hotkeys_listWidget.currentRow())

    def add_symbol_hotkey(self):
        if self.ui.hotkey_lineEdit.text() != '':
            self.ui.hotkeys_listWidget.addItem(self.ui.hotkey_lineEdit.text())
            self.ui.hotkey_lineEdit.setText('')

    def add_hotkey(self):
        if self.ui.hotkey_comboBox.currentText() != '':
            self.ui.hotkeys_listWidget.addItem(self.ui.hotkey_comboBox.currentText())
            self.ui.hotkey_comboBox.setCurrentIndex(0)

    def save_action(self):
        global ACTIONS
        global PROJECT_PATH
        if not self.ui.actions_listWidget.currentItem():
            return
        if self.ui.name_lineEdit.text() == '...' or self.ui.name_lineEdit.text() == '' or (
                self.ui.name_lineEdit.text() in [
            self.ui.actions_listWidget.item(i).text() for i in range(
                self.ui.actions_listWidget.count())] and self.ui.actions_listWidget.currentItem().text() != self.ui.name_lineEdit.text()):
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please, change action name')
            return
        elif self.ui.actions_listWidget.currentItem().text() == '...':
            self.ui.actions_listWidget.selectedItems()[0].setText(self.ui.name_lineEdit.text())
            action = self.ui.actions_tabWidget.tabText(self.ui.actions_tabWidget.currentIndex())
            if action == 'DragTo':
                action = 'dad'
            ACTIONS.append(
                {'name': self.ui.name_lineEdit.text(), 'action': action.lower(), 'button': None, 'duration': None,
                 'threshold': None, 'click_num': None, 'interval': None, 'text': None, 'keys': None, 'scroll': None,
                 'index': None, 'image': None, 'delay': None})
            self.tabEnable(self.ui.actions_tabWidget.currentIndex())
            self.set_icons()
        for i in ACTIONS:
            if i['name'] == self.ui.actions_listWidget.currentItem().text():
                if i['action'] == 'click':
                    i['name'] = self.ui.name_lineEdit.text()
                    self.ui.actions_listWidget.currentItem().setText(i['name'])
                    i['image'] = '/'.join(
                        PROJECT_PATH.split('/')[:-1]) + '/Images/' + self.ui.image_comboBox.currentText()
                    i['button'] = self.ui.button_comboBox.currentText()
                    i['threshold'] = self.ui.threshold_doubleSpinBox.value()
                    i['duration'] = self.ui.duration_doubleSpinBox.value()
                    i['click_num'] = self.ui.clicknum_spinBox.value()
                    i['index'] = self.ui.index_spinBox.value()
                    i['interval'] = self.ui.interval_doubleSpinBox.value()
                elif i['action'] == 'write':
                    i['text'] = self.ui.plainTextEdit.toPlainText()
                    i['interval'] = self.ui.interval_doubleSpinBox_2.value()
                elif i['action'] == 'press':
                    i['keys'] = ' '.join([str(self.ui.hotkeys_listWidget.item(i).text()) for i in
                                          range(self.ui.hotkeys_listWidget.count())])
                elif i['action'] == 'scroll':
                    i['scroll'] = self.ui.scroll_spinBox.value()
                elif i['action'] == 'dad':
                    i['image'] = self.ui.image_dad_comboBox.currentText()
                    i['duration'] = self.ui.duration_dad_doubleSpinBox.value()
                    i['threshold'] = self.ui.threshold_dad_doubleSpinBox.value()
                    i['index'] = self.ui.index_dad_spinBox.value()

    def updateImages(self):
        global PROJECT_PATH
        global IMAGES
        path = '/'.join(PROJECT_PATH.split('/')[:-1]) + '/Images'
        if os.path.exists(path):
            IMAGES = os.listdir(path)
            self.ui.image_comboBox.clear()
            self.ui.image_dad_comboBox.clear()
            self.ui.image_comboBox.addItems([''] + IMAGES)
            self.ui.image_dad_comboBox.addItems([''] + IMAGES)
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'The folder did not exist')
            IMAGES = list()
            self.ui.image_comboBox.clear()

    def currentItemChanged(self):
        try:
            global ACTIONS
            for i in range(self.ui.actions_listWidget.count()):
                if self.ui.actions_listWidget.item(i).text() == '...' and self.ui.actions_listWidget.currentRow() != i:
                    self.ui.actions_listWidget.takeItem(i)

            for i in ACTIONS:
                if self.ui.actions_listWidget.currentItem().text() == i['name']:
                    if i['action'] == 'click':
                        self.ui.actions_listWidget.currentItem().setIcon(QtGui.QIcon('icons/cursor.svg'))
                        self.ui.name_lineEdit.setText(i['name'])
                        self.ui.image_comboBox.setCurrentText(i['image'].split('/')[-1])
                        self.ui.button_comboBox.setCurrentText(i['button'])
                        self.ui.threshold_doubleSpinBox.setValue(i['threshold'])
                        self.ui.duration_doubleSpinBox.setValue(i['duration'])
                        self.ui.clicknum_spinBox.setValue(i['click_num'])
                        self.ui.index_spinBox.setValue(i['index'])
                        self.ui.interval_doubleSpinBox.setValue(i['interval'])
                        self.tabEnable(0)
                    elif i['action'] == 'write':
                        self.ui.name_lineEdit.setText(i['name'])
                        self.ui.plainTextEdit.setPlainText(i['text'])
                        self.ui.interval_doubleSpinBox_2.setValue(i['interval'])
                        self.tabEnable(1)
                    elif i['action'] == 'press':
                        self.ui.hotkeys_listWidget.clear()
                        self.ui.hotkeys_listWidget.addItems(i['keys'].split())
                        self.tabEnable(2)
                    elif i['action'] == 'scroll':
                        self.ui.scroll_spinBox.setValue(i['scroll'])
                        self.tabEnable(3)
                    elif i['action'] == 'dad':
                        self.ui.image_dad_comboBox.setCurrentText(i['image'])
                        self.ui.duration_dad_doubleSpinBox.setValue(i['duration'])
                        self.ui.index_dad_spinBox.setValue(i['index'])
                        self.ui.threshold_dad_doubleSpinBox.setValue(i['threshold'])
                        self.tabEnable(4)
        except BaseException as error:
            print(error)

    def tabEnable(self, index):
        for i in range(self.ui.actions_tabWidget.count()):
            self.ui.actions_tabWidget.setTabEnabled(i, False)
        self.ui.actions_tabWidget.setCurrentIndex(index)
        self.ui.actions_tabWidget.setTabEnabled(index, True)

    def open_resources(self):
        global PROJECT_PATH
        path = '/'.join(PROJECT_PATH.split('/')[:-1]) + '/Images'
        print(path)
        if not os.path.exists(path):
            QtWidgets.QMessageBox.warning(self, 'Warning', 'The folder did not exist, perhaps your images were lost')
            os.makedirs(path)
        os.startfile(path)

    def open_act(self):
        try:
            self.open(QtWidgets.QFileDialog.getOpenFileName(filter='*.db')[0])
        except BaseException as error:
            print(error)

    def saveProject(self):
        global ACTIONS
        global PROJECT_PATH
        ACTIONS_ORDER = [str(self.ui.actions_listWidget.item(i).text()) for i in
                         range(self.ui.actions_listWidget.count())]
        try:
            print(PROJECT_PATH)
            con = sqlite3.connect(PROJECT_PATH)
            cur = con.cursor()
            cur.execute('DELETE FROM actions')
            cur.execute('DELETE FROM settings')
            for i in ACTIONS_ORDER:
                for j in ACTIONS:
                    if i == j['name']:
                        cur.execute('INSERT INTO actions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                    [j['name'], j['action'], j['button'], j['duration'], j['threshold'], j['click_num'],
                                     j['interval'], j['text'], j['keys'], j['scroll'], j['index'], j['image'],
                                     j['delay']])
                        con.commit()
            print([self.ui.startstop_comboBox.currentText(),
                   self.ui.pause_comboBox.currentText(), self.ui.actions_interval_doubleSpinBox.value(),
                   self.ui.disable_mouse_checkBox.isChecked(), self.ui.display_info_checkBox.isChecked(),
                   self.ui.cycle_checkBox.isChecked()])
            cur.execute('INSERT INTO settings VALUES (?, ?, ?, ?, ?, ?)', [self.ui.startstop_comboBox.currentText(),
                                                                           self.ui.pause_comboBox.currentText(),
                                                                           self.ui.actions_interval_doubleSpinBox.value(),
                                                                           self.ui.disable_mouse_checkBox.isChecked(),
                                                                           self.ui.display_info_checkBox.isChecked(),
                                                                           self.ui.cycle_checkBox.isChecked()])
            con.commit()
            con.close()
        except BaseException as error:
            print('save:', error)

    def open(self, path):
        global ACTIONS, PROJECT_PATH
        self.ui.actions_listWidget.clear()
        if not os.path.isfile(path):
            QtWidgets.QMessageBox.warning(self, 'Warning!', 'Unable to open database')
            config = configparser.ConfigParser()
            config['MAIN'] = {'last_project': ''}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            return
        con = sqlite3.connect(path)
        con.row_factory = dict_factory
        cur = con.cursor()
        ACTIONS = cur.execute('SELECT * FROM actions').fetchall()
        settings = cur.execute('SELECT * FROM settings').fetchall()
        if len(settings) > 0:
            self.ui.startstop_comboBox.setCurrentText(settings[0]['startstop_key'])
            self.ui.pause_comboBox.setCurrentText(settings[0]['pause_key'])
            self.ui.actions_interval_doubleSpinBox.setValue(settings[0]['actions_interval'])
            self.ui.disable_mouse_checkBox.setChecked(settings[0]['disable_mouse'])
            self.ui.display_info_checkBox.setChecked(settings[0]['display_information'])
            self.ui.cycle_checkBox.setChecked(settings[0]['cycle'])
        con.close()
        print(ACTIONS)
        self.ui.actions_listWidget.addItems([i['name'] for i in ACTIONS])
        self.set_icons()
        self.setWindowTitle('ACR v0.0.1 - {}'.format(path))
        PROJECT_PATH = path
        self.updateImages()
        config = configparser.ConfigParser()
        config['MAIN'] = {'last_project': path}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def create_project(self):
        global PROJECT_PATH
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter database filename:')
        try:
            open(path + '/' + text + '.db', 'a').close()
            print(path + '/' + text + '.db')
            con = sqlite3.connect(path + '/' + text + '.db')
            cur = con.cursor()
            cur.execute('CREATE TABLE actions (\n'
                        '    name      STRING,\n'
                        '    [action]  STRING,\n'
                        '    button    STRING,\n'
                        '    duration  DOUBLE,\n'
                        '    threshold  DOUBLE,\n'
                        '    click_num INTEGER,\n'
                        '    interval  DOUBLE,\n'
                        '    text      TEXT,\n'
                        '    keys      STRING,\n'
                        '    scroll    INTEGER,\n'
                        '    [index]   STRING,\n'
                        '    image     STRING,\n'
                        '    delay     DOUBLE\n'
                        ');\n')
            cur.execute('CREATE TABLE settings (\n'
                        '    startstop_key    STRING,\n'
                        '    pause_key           STRING,\n'
                        '    actions_interval    DOUBLE,\n'
                        '    disable_mouse       BOOLEAN,\n'
                        '    display_information BOOLEAN,\n'
                        '    cycle               BOOLEAN\n'
                        ');')
            con.close()
            os.makedirs(path + '/Images')
            PROJECT_PATH = path + '/' + text + '.db'
            self.open(PROJECT_PATH)
            config = configparser.ConfigParser()
            config['MAIN'] = {'last_project': path + '/' + text + '.db'}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        except BaseException as error:
            QtWidgets.QMessageBox.warning(self, 'Warning', error)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(75, 75, 75).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    config = configparser.ConfigParser()
    if os.path.exists('config.ini'):
        config.read('config.ini')
        window = MainWindow(config['MAIN']['last_project'])
    else:
        config['MAIN'] = {'last_project': ''}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        window = MainWindow()

    window.show()
    sys.exit(app.exec())
