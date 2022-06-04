if __name__ == "__main__":
    # 复制图片代码
    url = "D:\\360MoveData\\Users\\44380\\Desktop\\bishehouduan\\bishehouduan\\src\\main\\resources\\warehouse\\1\\11" \
          "\\47c7206c-b736-4daa-b512-14bcf93e338c.png "
    fileNameList = url.split("\\")
    fileName = fileNameList[len(fileNameList)-1]
    to = "../data/images/" + fileName
    fromFile = open(url, 'rb')
    toFile = open(to, 'wb')
    toFile.write(fromFile.read())
    fromFile.close()
    toFile.close()
