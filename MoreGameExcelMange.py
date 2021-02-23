import xlwt
import xlrd
import OperateSVN
import os
from PyQt5.QtCore import QObject
import PyQt5.QtCore
import copy

class MoreGameItem():

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

    def printInfo(self):
        print("id {0} 名字 {1} 维护人 {2}".format(self.GameId, self.GameName, self.GameMaintain));

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

    def printInfo(self):
        print("index {0} id {1}".format(self.InfoIndex, self.InfoGameId))

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
        self.InfoGameCodePath = self.InfoGameCodePath.replace(" ", "\n")
        self.InfoGameResourcePath = self.InfoGameResourcePath.replace(" ", "\n")
        # print("InfoGameCodePath\n\t{0}\n_____\nInfoGameResourcePath\n\t{1}".format(self.InfoGameCodePath, self.InfoGameResourcePath))
        pass

class MoreGameExcelManage(QObject):
    selectChange = PyQt5.QtCore.pyqtSignal()


    def __init__(self):
        super(MoreGameExcelManage, self).__init__()
        self.openGameId = 0
        self.moreGameItems = []
        self.moreGameInfos = []
        self.selectGameIndex = []
        self.__isEnsure = False             # 是否确认信息
        self.__selectInfos = []             # 选中列表

    def initWithPath(self, filePath):
        self.excelPath = filePath
        self.wb = xlrd.open_workbook(filePath)
        self.readExcel()

    def judgeExcel(self):                   # 判断Excel文件的正确性

        pass

    def readExcel(self):
        self.__readMoreGameItem()
        self.__readMoreGameInfo()
        # print(self.moreGameItems)
        # print(self.moreGameInfos)
        pass

    #   0     1   2
    # 游戏ID 游戏名 维护人
    def __readMoreGameItem(self):
        itemSheet = self.wb.sheet_by_index(1)
        rowNum = itemSheet.nrows
        for row in range(rowNum):
            item = MoreGameItem()
            item.GameId = itemSheet.cell(row, 0).value
            item.GameName = itemSheet.cell(row, 1).value
            item.GameMaintain = itemSheet.cell(row, 2).value
            item.judgeSelf()
            self.moreGameItems.append(item)
            # item.printInfo()
            pass
        pass

    #   0   1   2   3   4   5   6
    #序号 游戏ID 宏 代码 资源 变量 描述
    def __readMoreGameInfo(self):
        infoSheet = self.wb.sheet_by_index(0)
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
            # print("index = {0} id = {1} row = {2} ".format(infoSheet.cell(row, 0).value, infoSheet.cell(row, 1).value, row))
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
        self.__updateSelectInfos()
        self.selectChange.emit()

    def removeSelected(self, id):
        if id in self.selectGameIndex:
            self.selectGameIndex.remove(id)
        self.__updateSelectInfos()
        self.selectChange.emit()
        pass

    def __updateSelectInfos(self):
        self.__selectInfos.clear()
        for index in self.selectGameIndex:
            for info in self.moreGameInfos:
                if info.InfoIndex == index:
                    self.__selectInfos.append(copy.deepcopy(info))
                    break

    def getAllSelectInfos(self):
        return self.__selectInfos
        pass

    def updateSelectInfos(self, infoIndex, defineStr = "", codePath = "", resourcePath = ""):
        for info in self.__selectInfos:
            if info.InfoIndex == infoIndex:
                if "" != defineStr:
                    info.InfoGameDefine = defineStr
                if "" != codePath:
                    info.InfoGameCodePath = codePath
                if "" != resourcePath:
                    info.InfoGameResourcePath = resourcePath
                break
                pass
        pass

    def createAndroidFile(self, androidProjPath, gameMoreDirPath):
        selectInfos = self.getAllSelectInfos()
        ###
        resourceDirList = []
        resourceDirList.append(gameMoreDirPath)
        for info in selectInfos:
            for line in info.InfoGameResourcePath.splitlines():
                resourceDirList.append(line.split("/")[-1])
            pass
        resourceDirList = list(set(resourceDirList))        # 去重

        resources_listPy = "GameResources=[\"PublicRes\","
        for resourceDir in resourceDirList:
            resources_listPy += "\"" + resourceDir + "\","
        if "," == resources_listPy[-1]:
            resources_listPy = resources_listPy[0:-1]
        resources_listPy += "]"
        # print(resources_listPy)

        ###
        codeDirList = []
        for info in selectInfos:
            for line in info.InfoGameCodePath.splitlines():
                codeDirList.append(line.split("/")[-1])
        codeDirList = list(set(codeDirList))        # 去重

        androidMk = "LOCAL_PATH := $(call my-dir)\n\
\n\
include $(LOCAL_PATH)/../../../C2DXPdragonSDK/Common/mk/cocos2d_316/AndroidCommon.mk\n\
\n\
FILE_LIST += $(wildcard $(LOCAL_PATH)/../../Classes/*.cpp)\n"

        for codeDir in codeDirList:
            androidMk += "FILE_LIST += $(wildcard $(LOCAL_PATH)/../../Classes/" + codeDir + "/*.cpp)\n"
            pass
        androidMk += "FILE_LIST += $(wildcard $(LOCAL_PATH)/../../Classes/Public/*.cpp)\n\n"

        androidMk += "\nLOCAL_C_INCLUDES += $(LOCAL_PATH)/../../Classes \\\n"
        for codeDir in codeDirList:
            androidMk += "\t\t\t\t\t$(LOCAL_PATH)/../../Classes/" + codeDir + " \\\n"
            pass

        androidMk += "\t\t\t\t\t$(LOCAL_PATH)/../../Classes/Public \n"
        androidMk += "LOCAL_SRC_FILES := $(FILE_LIST:$(LOCAL_PATH)/%=%)\n\
include $(BUILD_SHARED_LIBRARY)\n\
$(call import-module,.)\n"

        # print(androidMk)
        ###

        applicationMk = "LOCAL_PATH := $(call my-dir)\n\
APP_SHORT_COMMANDS := true\n\
include $(LOCAL_PATH)/../../../C2DXPdragonSDK/Common/mk/cocos2d_316/ApplicationCommon.mk\n\
\n\
##Debug##\n\
#APP_CPPFLAGS += -DCOCOS2D_DEBUG=1\n\
#APP_OPTIM := debug\n\
##Release##\n\
APP_CPPFLAGS += -DNDEBUG\n\
APP_OPTIM := release\n\
\n\
####游戏用到的所有宏定义全部在这里\n"
        applicationMk += "APP_CPPFLAGS += -DCOCOS2D_316 -DCC_USE_3D=1 -DCC_USE_3D_PHYSICS=1 -DSHOW_MORE_GAME"

        for info in selectInfos:
            defines = info.InfoGameDefine.split(" ")
            for define in defines:
                define = define.strip()
                if '' != define:
                    applicationMk += " -D" + info.InfoGameDefine

        # print(applicationMk)

        ###

        isJniExist = os.path.exists(androidProjPath + "/jni")

        if not isJniExist:
            os.mkdir(androidProjPath + "/jni")

        with open(androidProjPath + "/jni/Android.mk", 'w', encoding="UTF-8") as file:
            file.write(androidMk)

        with open(androidProjPath + "/jni/Application.mk", 'w', encoding="UTF-8") as file:
            file.write(applicationMk)

        with open(androidProjPath + "/resources_list.py", 'w', encoding="UTF-8") as file:
            file.write(resources_listPy)

        pass

    def isEnsureInfos(self):
        return self.__isEnsure

    def setEnsureInfos(self, ensure):
        self.__isEnsure = ensure

    def addMoreGameToSVN(self, projPath):
        selectInfos = self.getAllSelectInfos()
        codeString = ""
        resourceString = ""
        for info in selectInfos:
            codeString += info.InfoGameCodePath + "\n"
            resourceString += info.InfoGameResourcePath + "\n"
        return OperateSVN.addPathToSVN(projPath, codeString, resourceString)
        pass

    def getGameNameById(self, gameId):
        for game in self.moreGameItems:
            if game.GameId == gameId:
                return game.GameName

    def judgeSelectInfos(self):
        result = ""

        infos = self.getAllSelectInfos()
        for info in infos:
            if "*" in info.InfoGameResourcePath:
                result = "资源中有*没有被修改"
                break
            elif "*" in info.InfoGameCodePath:
                result = "代码中有*没有被修改"
                break
            elif "*" in info.InfoGameDefine:
                result = "宏定义中有*没有被修改"
                break

        return result

    pass

moreGameExcelManage = MoreGameExcelManage()