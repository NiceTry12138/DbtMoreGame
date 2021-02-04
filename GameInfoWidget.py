from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets
from PyQt5.QtCore import *
from MoreGameExcelMange import moreGameExcelManage
from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton,\
    QListWidgetItem, QVBoxLayout, QListWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class InfoWidgetItem(QWidget):
    def __init__(self, infoItem, item, *args, **kwargs):
        super(InfoWidgetItem, self).__init__(*args, **kwargs)
        self.index = infoItem.InfoIndex
        self.item = item

        self.indexLine = QLabel(str(infoItem.InfoIndex), self)
        self.gameIdLine = QLabel(str(infoItem.InfoGameId), self)
        self.InfoGameDefineLine = QLineEdit(infoItem.InfoGameDefine, self)
        self.InfoGameCodePathLine = QTextEdit(self)
        self.InfoGameResourcePathLine = QTextEdit(self)
        self.InfoGameVariateLine = QLineEdit(infoItem.InfoGameVariate, self)
        self.InfoIntroduceLine = QLabel(infoItem.InfoIntroduce, self)
        self.addBtn = QPushButton('添加到多玩法', self, clicked=self.doDeleteItem)
        # self.rmeoveBtn = QPushButton('从表中删除')

        introduceFont = QFont()
        introduceFont.setBold(True)
        introduceFont.setPointSize(16)
        self.InfoIntroduceLine.setFont(introduceFont)
        self.InfoIntroduceLine.setStyleSheet("color:red")

        self.InfoGameCodePathLine.setPlainText(infoItem.InfoGameCodePath)
        self.InfoGameResourcePathLine.setPlainText(infoItem.InfoGameResourcePath)

        # self.InfoGameCodePathLine.setMinimumHeight(150)
        # self.InfoGameResourcePathLine.setMinimumHeight(150)

        layout = QGridLayout(self)                                  # 网格管理器
        layout.setSpacing(10)                                       # 设置间距
        layout.addWidget(QLabel("表单序号"), 0, 0)
        layout.addWidget(self.indexLine, 0, 1)
        layout.addWidget(QLabel("游戏ID"), 0, 2)
        layout.addWidget(self.gameIdLine, 0, 3)
        layout.addWidget(QLabel("宏定义"), 1, 0)
        layout.addWidget(self.InfoGameDefineLine, 1, 1)
        layout.addWidget(QLabel("游戏变量"), 1, 2)
        layout.addWidget(self.InfoGameVariateLine, 1, 3)
        layout.addWidget(QLabel("描述内容"), 2, 0)
        layout.addWidget(self.InfoIntroduceLine, 2, 1, 1, 4)
        layout.addWidget(QLabel("代码路径"), 3, 0)
        layout.addWidget(self.InfoGameCodePathLine, 3, 1, 4, 2)
        layout.addWidget(QLabel("资源路径"), 7, 0)
        layout.addWidget(self.InfoGameResourcePathLine, 7, 1, 4, 2)
        layout.addWidget(QLabel("操作按钮"), 11, 0)
        layout.addWidget(self.addBtn, 11, 1)

        self.setLayout(layout)

        if moreGameExcelManage.isSlectedById(self.index):
            self.addBtn.setText("从多玩法移除")

        pass

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(InfoWidgetItem, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))

    def doDeleteItem(self):
        if moreGameExcelManage.isSlectedById(self.index):
            moreGameExcelManage.removeSelected(self.index)
            self.addBtn.setText("添加到多玩法")
        else:
            moreGameExcelManage.addSelected(self.index)
            self.addBtn.setText("从多玩法移除")
        pass

    def sizeHint(self):
        # 决定item的高度
        return QSize(860, 400)

    def connectChengeToManage(self):
        self.InfoGameDefineLine.textChanged.connect(self.__updateToGameInfoManage)
        self.InfoGameResourcePathLine.textChanged.connect(self.__updateToGameInfoManage)
        self.InfoGameCodePathLine.textChanged.connect(self.__updateToGameInfoManage)

    def __updateToGameInfoManage(self):
        reourceStr = self.InfoGameResourcePathLine.toPlainText()
        codeStr = self.InfoGameCodePathLine.toPlainText()
        defineStr = self.InfoGameDefineLine.text()
        # print(reourceStr + " " + codeStr + " " + defineStr)
        moreGameExcelManage.updateSelectInfos(self.index, defineStr, codeStr, reourceStr)
        print("修改成功")
    pass

class MoreGameInfoWidget(QDialog):
    sinOut = pyqtSignal()   # 自定义信号

    def __init__(self, parent = None):
        super(MoreGameInfoWidget, self).__init__(parent)
        self.showList = moreGameExcelManage.getInfoByGameId(moreGameExcelManage.getTargetGameId())
        self.resize(860, 760)
        self.layout = QVBoxLayout(self)
        self.listWidget = QListWidget(self)
        self.layout.addWidget(self.listWidget)
        self.returnBack = QPushButton("返回", self, clicked=self.back)
        self.layout.addWidget(self.returnBack)
        self.addShowList()

    def addShowList(self):
        for info in self.showList:
            item = QListWidgetItem(self.listWidget)
            widget = InfoWidgetItem(info, item, self.listWidget)
            self.listWidget.setItemWidget(item, widget)
        pass

    def back(self):         # 关闭本界面
        self.deleteLater()
        pass

class AllSelectWidget(QDialog):

    def __init__(self, parent = None):
        super(AllSelectWidget, self).__init__(parent)
        self.showList = moreGameExcelManage.getAllSelectInfos()
        self.resize(860, 760)
        self.layout = QVBoxLayout(self)
        self.listWidget = QListWidget(self)
        self.layout.addWidget(self.listWidget)
        self.returnBack = QPushButton("确认信息", self, clicked=self.back)
        self.layout.addWidget(self.returnBack)
        self.addShowList()
        self.returnBack.setStyleSheet("QPushButton \
        {\
            color:white;\
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\
            border-width: 1px;\
            border-color: #339;\
            border-style: solid;\
            border-radius: 7;\
            padding: 3px;\
            font-size: 20px;\
            padding-left: 5px;\
            padding-right: 5px;\
            min-height: 50px;\
        }"
        "QPushButton:hover{"
            "background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #66d, stop: 0.1 #66e, stop: 0.49 #66c, stop: 0.5 #66b, stop: 1 #66c);"
        "}")

    def addShowList(self):
        for info in self.showList:
            item = QListWidgetItem(self.listWidget)
            widget = InfoWidgetItem(info, item, self.listWidget)
            widget.connectChengeToManage()
            self.listWidget.setItemWidget(item, widget)
        pass

    def back(self):         # 关闭本界面
        judgeString = moreGameExcelManage.judgeSelectInfos()
        if "" != judgeString:
            QMessageBox.warning(self, "警告", judgeString, QMessageBox.Ok)
        else:
            self.deleteLater()
            moreGameExcelManage.setEnsureInfos(True)
        pass
    pass