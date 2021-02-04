# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from DbtLineEdit import DbtDropLineEdit
from MoreGameExcelMange import moreGameExcelManage
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import GameInfoWidget

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 201, 392))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.MainGameLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.MainGameLayout.setContentsMargins(0, 0, 0, 0)
        self.MainGameLayout.setObjectName("MainGameLayout")
        self.MainGameInfo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.MainGameInfo.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.MainGameInfo.setFont(font)
        self.MainGameInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.MainGameInfo.setObjectName("MainGameInfo")
        self.MainGameLayout.addWidget(self.MainGameInfo)
        self.GameId = DbtDropLineEdit("", self.verticalLayoutWidget)
        self.GameId.setMinimumSize(QtCore.QSize(60, 60))
        self.GameId.setAlignment(QtCore.Qt.AlignCenter)
        self.GameId.setObjectName("GameId")
        self.MainGameLayout.addWidget(self.GameId)
        self.GamePath = DbtDropLineEdit("", self.verticalLayoutWidget)
        self.GamePath.setMinimumSize(QtCore.QSize(0, 60))
        self.GamePath.setObjectName("GamePath")
        self.MainGameLayout.addWidget(self.GamePath)
        self.GamePerson = DbtDropLineEdit("", self.verticalLayoutWidget)
        self.GamePerson.setMinimumSize(QtCore.QSize(0, 60))
        self.GamePerson.setObjectName("GamePerson")
        self.MainGameLayout.addWidget(self.GamePerson)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainGameLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setObjectName("pushButton")
        self.MainGameLayout.addWidget(self.pushButton)
        self.MoreGameListWidget = QtWidgets.QWidget(self.centralwidget)
        self.MoreGameListWidget.setGeometry(QtCore.QRect(240, 20, 861, 821))
        self.MoreGameListWidget.setObjectName("MoreGameListWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MoreGameListWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.MoreGameList = QtWidgets.QListView(self.MoreGameListWidget)
        self.MoreGameList.setGeometry(QtCore.QRect(0, 60, 860, 760))
        self.MoreGameList.setObjectName("MoreGameList")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 410, 201, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.showInfosLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.showInfosLayout.setContentsMargins(0, 0, 0, 0)
        self.showInfosLayout.setObjectName("showInfosLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.initMainWindow()
        self.connectAll()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MainGameInfo.setText(_translate("MainWindow", "主玩法信息"))
        self.GameId.setPlaceholderText(_translate("MainWindow", "GameID（选填）"))
        self.GamePath.setPlaceholderText(_translate("MainWindow", "拖入游戏目录 E:/SVN/byteGo"))
        self.GamePerson.setPlaceholderText(_translate("MainWindow", "拖入安卓工程 E:/SVN/byteGo/proj.android_studio"))
        self.pushButton_2.setText(_translate("MainWindow", "查看选中多玩法"))
        self.pushButton.setText(_translate("MainWindow", "生成选中多玩法"))
        self.label.setText(_translate("MainWindow", "多玩法游戏列表"))

    def initMainWindow(self):  # 初始化数据和界面
        moreGameExcelManage.initWithPath("./GameList.xlsx")
        self.__selectLabels = []
        listModel = QStandardItemModel()
        for gameItem in moreGameExcelManage.moreGameItems:
            showString = "\t{:10}{:30}\t{:20}"
            listItem = QStandardItem(showString.format(str(gameItem.GameId), gameItem.GameName, gameItem.GameMaintain))
            listItem.setFont(QFont("", 20, QFont.Normal))
            listItem.setEditable(False)
            listModel.appendRow(listItem)
            pass
        self.MoreGameList.setModel(listModel)
        self.MoreGameList.clicked.connect(self.moreGameListClicked)

    def connectAll(self):  # 连接所有槽盒接口
        self.pushButton_2.clicked.connect(self.showSelecInfos)
        self.pushButton.clicked.connect(self.createFile)
        moreGameExcelManage.selectChange.connect(self.updateSelectItems)
        pass

    def moreGameListClicked(self, qModelIndex):
        if 0 == qModelIndex.row():
            return
        moreGameExcelManage.setTargetGameId(qModelIndex.row())
        # QMessageBox.information(self,'ListWidget','你选择了：'+str(qModelIndex.row()), QMessageBox.Ok)
        gameInfoWidget = GameInfoWidget.MoreGameInfoWidget()
        gameInfoWidget.move(self.MoreGameList.pos())
        gameInfoWidget.show()
        gameInfoWidget.exec_()
        # self.MoreGameList.hide()
        pass

    def showSelecInfos(self):
        selectInfosWidget = GameInfoWidget.AllSelectWidget()
        selectInfosWidget.move(self.MoreGameList.pos())
        selectInfosWidget.show()
        selectInfosWidget.exec_()

        pass

    def updateSelectItems(self):
        selectInfos = moreGameExcelManage.getAllSelectInfos()
        for node in self.__selectLabels:
            node.deleteLater()
        self.__selectLabels.clear()

        for info in selectInfos:
            labelStr = moreGameExcelManage.getGameNameById(info.InfoGameId) + " 列表序号 " + str(info.InfoIndex)
            label = QLabel(labelStr, self)
            self.__selectLabels.append(label)
            self.showInfosLayout.addWidget(label)

        pass

    def createFile(self):
        if moreGameExcelManage.isEnsureInfos() == False:
            QMessageBox.information(self, '提示', '请先查看并确认多玩法信息', QMessageBox.Ok)
            return

        androidPath = self.GamePerson.text()
        projPath = self.GamePath.text()
        if "" == androidPath:
            QMessageBox.critical(self, '错误', '安卓路径未填写', QMessageBox.Ok)
            return
        else:
            jsAndroidProjExist = os.path.exists(androidPath)
            if not jsAndroidProjExist:
                QMessageBox.critical(self, '错误', '安卓目录不存在', QMessageBox.Ok)
                return
            else:
                moreGameExcelManage.createAndroidFile(androidPath)

        if "" == projPath:
            QMessageBox.critical(self, '错误', "项目路径未填写", QMessageBox.Ok)
            return
        else:
            isProjExist = os.path.exists(projPath)
            isClassesExist = os.path.exists(projPath + "/Classes")
            isResourceExist = os.path.exists(projPath + "/Resources")
            if not isProjExist:
                QMessageBox.critical(self, '错误', "项目路径不存在", QMessageBox.Ok)
                return
            elif not isClassesExist:
                QMessageBox.critical(self, '错误', "项目路径中不存在Classes", QMessageBox.Ok)
                return
            elif not isResourceExist:
                QMessageBox.critical(self, '错误', "项目路径不存在Resources", QMessageBox.Ok)
                return
            else:
                moreGameExcelManage.addMoreGameToSVN(projPath)

        moreGameExcelManage.setEnsureInfos(False)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec_())
