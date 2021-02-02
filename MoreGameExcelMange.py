import xlwt
import xlrd

class MoreGameItem:

    def __init__(self):
        self.GameId = 0             # 游戏id
        self.GameName = ""          # 游戏名
        self.GameMaintain = ""      # 游戏维护人
        pass

    def judgeSelf(self):
        self.GameName = self.GameName.strip()
        self.GameMaintain = self.GameMaintain.strip()
        # self.GameId = self.GameId.split(".")[0]
        # self.GameId = int(self.GameId)
        if '.' in str(self.GameId):
            self.GameId = int(self.GameId)
        pass

    pass

class MoreGameInfo:

    def __init__(self):
        self.InfoIndex = 0                  # 序号
        self.InfoGameId = 0                 # 对应游戏Id
        self.InfoGameDefine = ""            # 游戏宏
        self.InfoGameCodePath = ""          # 游戏代码路径
        self.InfoGameResourcePath = ""      # 游戏资源路径
        self.InfoGameVariate = ""           # 游戏变量
        self.InfoIntroduce = ""             # 描述
        pass

    def judgeSelf(self):
        if '.' in str(self.InfoGameId):
            self.InfoGameId = int(self.InfoGameId)
        if '.' in str(self.InfoIndex):
            self.InfoIndex = int(self.InfoIndex)
        self.InfoIntroduce = self.InfoIntroduce.strip()
        self.InfoGameVariate = self.InfoGameVariate.strip()
        self.InfoGameResourcePath = self.InfoGameResourcePath.strip()
        self.InfoGameCodePath = self.InfoGameCodePath.strip()
        self.InfoGameDefine = self.InfoGameDefine.strip()
        pass

class MoreGameExcelManage :

    def __init__(self):
        self.openGameId = 0
        self.moreGameItems = []
        self.moreGameInfos = []
        self.selectGameIndex = []

    def initWithPath(self, filePath):
        self.excelPath = filePath
        self.wb = xlrd.open_workbook(filePath)
        self.readExcel()

    def judgeExcel(self):                   # 判断Excel文件的正确性

        pass

    def readExcel(self):
        self.readMoreGameItem()
        self.readMoreGameInfo()
        print(self.moreGameItems)
        print(self.moreGameInfos)
        pass

    #   0     1   2
    # 游戏ID 游戏名 维护人
    def readMoreGameItem(self):
        itemSheet = self.wb.sheet_by_index(0)
        rowNum = itemSheet.nrows
        for row in range(rowNum):
            item = MoreGameItem()
            item.GameId = itemSheet.cell(row, 0).value
            item.GameName = itemSheet.cell(row, 1).value
            item.GameMaintain = itemSheet.cell(row, 2).value
            item.judgeSelf()
            self.moreGameItems.append(item)
            pass
        pass

    #   0   1   2   3   4   5   6
    #序号 游戏ID 宏 代码 资源 变量 描述
    def readMoreGameInfo(self):
        infoSheet = self.wb.sheet_by_index(1)
        rowNum = infoSheet.nrows
        for row in range(rowNum):
            info = MoreGameInfo()
            info.InfoIndex = infoSheet.cell(row, 0).value
            info.InfoGameId = infoSheet.cell(row, 1).value
            info.InfoGameDefine = infoSheet.cell(row, 2).value
            info.InfoGameCodePath = infoSheet.cell(row, 3).value
            info.InfoGameResourcePath = infoSheet.cell(row, 4).value
            info.InfoGameVariate = infoSheet.cell(row, 5).value
            info.InfoIntroduce = infoSheet.cell(row, 6).value
            info.judgeSelf()
            self.moreGameInfos.append(info)
            pass
        pass

    def getInfoByGameId(self, targetId):
        result = []
        # if len(self.moreGameInfos):
        #     result.append(self.moreGameInfos[0])
        for info in self.moreGameInfos:
            if info.InfoGameId == targetId:
                result.append(info)
        return result
        pass

    def getMoreGameItems(self):
        return self.moreGameItems

    def setTargetGameId(self, id):
        self.openGameId = id

    def getTargetGameId(self):
        return self.openGameId

    def isSlectedById(self, id):
        if id in self.selectGameIndex:
            return True
        else:
            return False

    def addSelected(self, id):
        self.selectGameIndex.append(id)

    def removeSelected(self, id):
        if id in self.selectGameIndex:
            self.selectGameIndex.remove(id)
        pass

    pass

moreGameExcelManage = MoreGameExcelManage()