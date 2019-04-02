import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from day import Ui_MainWindow
import requests
import collector

class MyWindow(QMainWindow, Ui_MainWindow): #成调用qt designer生的界面类并添加查询代码
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def firstPyQt5_button_click(self):#按钮点击
        self.ui.textBrowser.clear()
        str = self.ui.dateEdit.text()    #将日期栏中输入的值赋给 month 和 day
        if str[1] == '/': #判断月份是否为两位数字
            month = str[0]
            day = str[2:4]

        else:
            month = str[0:2]
            day = str[2:4]

        search = collector.Day(month, day)
        result_dict = search.get_thing()        #通过API接口查询
        for i in result_dict['result']:
            self.ui.textBrowser.append(i['title'])
