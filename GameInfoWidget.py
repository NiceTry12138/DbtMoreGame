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

        self.indexLine = QLineEdit(str(infoItem.InfoIndex), self)
        self.gameIdLine = QLineEdit(str(infoItem.InfoGameId), self)
        self.InfoGameDefineLine = QLineEdit(str(infoItem.InfoGameDefine), self)
        self.InfoGameCodePathLine = QTextEdit(str(infoItem.InfoGameCodePath), self)
        self.InfoGameResourcePathLine = QTextEdit(str(infoItem.InfoGameResourcePath), self)
        self.InfoGameVariateLine = QLineEdit(str(infoItem.InfoGameVariate), self)
        self.InfoIntroduceLine = QLineEdit(str(infoItem.InfoIntroduce), self)
        self.addBtn = QPushButton('Add', self, clicked=self.doDeleteItem)

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
        layout.addWidget(QLabel("代码路径"), 2, 0)
        layout.addWidget(self.InfoGameCodePathLine, 2, 1, 4, 2)
        layout.addWidget(QLabel("资源路径"), 6, 0)
        layout.addWidget(self.InfoGameResourcePathLine, 6, 1, 4, 2)
        layout.addWidget(QLabel("描述内容"), 10, 0)
        layout.addWidget(self.InfoIntroduceLine, 10, 1)
        layout.addWidget(QLabel("操作按钮"), 10, 2)
        layout.addWidget(self.addBtn, 10, 3)

        self.setLayout(layout)

        if moreGameExcelManage.isSlectedById(self.index):
            self.addBtn.setText("Del")

        pass

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(InfoWidgetItem, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))

    def doDeleteItem(self):
        if moreGameExcelManage.isSlectedById(self.index):
            moreGameExcelManage.removeSelected(self.index)
            self.addBtn.setText("Add")
        else:
            moreGameExcelManage.addSelected(self.index)
            self.addBtn.setText("Del")
        pass

    def sizeHint(self):
        # 决定item的高度
        return QSize(860, 400)
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