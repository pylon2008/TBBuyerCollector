#-*- coding: utf-8 -*-

#加载有需要的Qt库
from PyQt4 import QtCore, QtGui

#从ui_test.py文件中读取Ui_Dialog类，Ui_Dialog类由pyuic4生成
from MainDialog import Ui_MainDialog
from MainDialog import _fromUtf8


#继承的类要和生成的ui对相
class Ui(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.ui = Ui_MainDialog()
        self.ui.setupUi(self)
        self.__initSignalConnect()
        
    def __initSignalConnect(self):
        QtCore.QObject.connect(self.ui.m_btnSearch, QtCore.SIGNAL(_fromUtf8("clicked()")), self.beginSearch)
        
    def beginSearch(self):  
        stri = self.ui.m_targetURL.toPlainText()
        row = 2
        col = 5
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(col)  
        self.ui.tableWidget.setHorizontalHeaderLabels(['SUN','MON','TUE','WED','THU'])     
        self.ui.tableWidget.horizontalHeader().setClickable(False)
        for i in range(row):
            for j in range(col):
                value = str(i)+str(j)
                item = QtGui.QTableWidgetItem(QtGui.QIcon("pic//b_blue_1.gif"), value)
                #item = QtGui.QTableWidgetItem(value)
                self.ui.tableWidget.setItem(i,j,item)
        self.ui.tableWidget.show()
        self.show()

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
