# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\WorkStation\Git\Hub\\TBBuyerCollector\MainDialog.ui'
#
# Created: Thu Jul 18 10:58:35 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(552, 426)
        self.tabWidget = QtGui.QTabWidget(MainDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 531, 401))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.m_targetURL = QtGui.QTextEdit(self.tab_1)
        self.m_targetURL.setGeometry(QtCore.QRect(60, 16, 351, 30))
        self.m_targetURL.setObjectName(_fromUtf8("m_targetURL"))
        self.label = QtGui.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(20, 26, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.tableWidget = QtGui.QTableWidget(self.tab_1)
        self.tableWidget.setGeometry(QtCore.QRect(20, 56, 481, 311))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.m_btnSearch = QtGui.QPushButton(self.tab_1)
        self.m_btnSearch.setGeometry(QtCore.QRect(420, 20, 75, 23))
        self.m_btnSearch.setObjectName(_fromUtf8("m_btnSearch"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(MainDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(_translate("MainDialog", "Dialog", None))
        self.label.setText(_translate("MainDialog", "目标:", None))
        self.m_btnSearch.setText(_translate("MainDialog", "开始", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainDialog", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainDialog", "Tab 2", None))

