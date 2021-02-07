import os
from functools import reduce
import sys

# projPath = "E:/SVN/byteGo"
# addProp = "https://192.168.10.5/svn/pdragon/tetris_redo/Classes/hexagon\nhttps://192.168.10.5/svn/pdragon/tetris_redo/Classes/tetrix\nhttps://192.168.10.5/svn/pdragon/tetris_redo/Classes/tetrix_common"
# resourceProp = "https://192.168.10.5/svn/pdragon/tetris_redo/Resources/free1010_skin1\nhttps://192.168.10.5/svn/pdragon/tetris_redo/Resources/hexagon_skin1\nhttps://192.168.10.5/svn/pdragon/tetris_redo/Resources/popblock_skin1\nhttps://192.168.10.5/svn/pdragon/tetris_redo/Resources/tetrix_common_skin1"

def addPathToSVN(projPath, addProp, resourceProp):
    showTipString = "设置成功"

    propItems = []
    resourceItems = []
    addProp = addProp.strip()
    resourceProp = resourceProp.strip()
    addProp = addProp.replace("https://192.168.10.5/svn/pdragon", "^")
    for line in addProp.splitlines():
        itemMap = {}
        itemMap["name"] = line.split("/")[-1]
        itemMap["path"] = line
        propItems.append(itemMap)

    resourceProp = resourceProp.replace("https://192.168.10.5/svn/pdragon", "^")
    for line in resourceProp.splitlines():
        itemMap = {}
        itemMap["name"] = line.split("/")[-1]
        itemMap["path"] = line
        resourceItems.append(itemMap)

    codeResult = os.popen("svn pg svn:externals " + projPath + "/Classes")
    contenxt = codeResult.read()
    resourceResult = os.popen("svn pg svn:externals " + projPath + "/Resources")
    resourceContenxt = resourceResult.read()

    if "不是内部或外部命令" in contenxt or "不是内部或外部命令" in resourceContenxt:
        showTipString = "未配置SVN命令行工具"

    # print(resourceItems)
    # print(propItems)

    if contenxt.startswith("^") and resourceContenxt.startswith("^"):
        for line in contenxt.splitlines():
            itemMap = {}
            KV = line.strip().split(" ")
            if len(KV) == 2:
                itemMap["name"] = KV[1]
                itemMap["path"] = KV[0]
                hasSame = False
                for item in propItems:
                    if item["name"] == KV[1] or item["path"] == KV[0]:
                        hasSame = True
                if not hasSame:
                    propItems.append(itemMap)

        for line in resourceContenxt.splitlines():
            itemMap = {}
            KV = line.strip().split(" ")
            if len(KV) == 2:
                itemMap["name"] = KV[1]
                itemMap["path"] = KV[0]
                hasSame = False
                for item in resourceItems:
                    if item["name"] == KV[1] or item["path"] == KV[0]:
                        hasSame = True
                if not hasSame:
                    resourceItems.append(itemMap)

        run_function = lambda x, y: x if y in x else x + [y]
        propItems = reduce(run_function, [[], ] + propItems)       #  去重
        filestring = ""
        for item in propItems:
            filestring += item["path"] + " " + item["name"] + "\n"

        print("添加后Classes的外部属性")
        print(filestring)

        resourceItems = reduce(run_function, [[], ] + resourceItems)    # 去重
        resourceFileString = ""
        for item in resourceItems:
            resourceFileString += item["path"] + " " + item["name"] + "\n"

        print("添加后Resources的外部属性")
        print(resourceFileString)

        with open("svnCodeExternalPropList.txt", "w") as file:
            file.write(filestring)

        with open("svnResourceExternalPropList.txt", "w") as file:
            file.write(resourceFileString)

        result = os.popen("svn ps svn:externals " + projPath + "/Classes" + " -F svnCodeExternalPropList.txt")
        resourceResult = os.popen("svn ps svn:externals " + projPath + "/Resources" + " -F svnResourceExternalPropList.txt")
        # if os.path.exists("svnCodeExternalPropList.txt"):
        #     os.remove("svnCodeExternalPropList.txt")
        # if os.path.exists("svnResourceExternalPropList.txt"):
        #     os.remove("svnResourceExternalPropList.txt")
        print(result.read())
        print(resourceResult.read())

        if "database is locked" in result.read():
            showTipString = "请主动SVN或还原SVN外部属性"

    else:
        print("error")
        showTipString = "存在未知错误\n请查看控制台输出"

    return showTipString