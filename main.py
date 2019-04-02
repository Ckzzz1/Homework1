from qt import *
if __name__ == '__main__':    #主函数显示窗口
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
