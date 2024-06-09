
import os
import glob

# 指定のデータサイズでファイルを分割
def divide_file(filePath, chunkSize):

    readedDataSize = 0
    i = 0
    fileList = []

    # 対象ファイルを開く
    targetFile = open(filePath, "rb") # 読み取り＋バイナリモード オプション

    # ファイルを読み込む
    contentLength = os.path.getsize(filePath)
    while readedDataSize < contentLength: # 終了時にClose

        # 読み取り位置をシーク・指定されたデータサイズを読み込み
        targetFile.seek(readedDataSize)
        data = targetFile.read(chunkSize)

        # 対象フォルダが存在しなかったら作成
        fileName, extention = os.path.splitext(filePath)
        saveFolderPath = os.getcwd() + "\_devided"
        
        if (not os.path.exists(saveFolderPath)): 
            os.mkdir(saveFolderPath)
        
        # 対象フォルダに分割ファイルを保存
        saveFilePath = f"{saveFolderPath}\\{fileName}.{format(i, "04d")}{extention}" # 連番名に変更
        with open(saveFilePath, "wb") as saveFile: # 書き込み＋バイナリモード オプション
            saveFile.write(data)\

        # 次の読みとり開始位置を更新
        readedDataSize += len(data)
        i += 1
        fileList.append(saveFilePath)


    return fileList


# 渡された順で1つのファイルに結合
def merge_file(exportPath, dirPath):

    fileList = glob.glob(os.path.join(dirPath, "*.png"))
    fileName, extention = os.path.splitext(exportPath)
    exportPath = str(exportPath).rstrip(extention) + "_merged" + extention

    with open(exportPath, "wb") as saveFile: # 終了時にClose
        for f in fileList:
            data = open(f, "rb").read()
            saveFile.write(data)
            saveFile.flush()


