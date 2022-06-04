from socket import *
import detect
import os
import shutil


# 业务代码
def fun(url):
    # 将图像拷贝至data下的images
    fileNameList = url.split("\\")
    fileName = fileNameList[len(fileNameList) - 1]
    to = "./data/images/" + fileName
    fromFile = open(url, 'rb')
    toFile = open(to, 'wb')
    toFile.write(fromFile.read())
    fromFile.close()
    toFile.close()
    # 调用图像处理软件
    detect.FUN()
    # 将图像从runs.detect下的exp取出到新url下
    newUrl = url.replace("warehouse", "newWarehouse")
    resFile = open("./runs/detect/exp/" + fileName, "rb")
    toResFile = open(newUrl, 'wb')
    toResFile.write(resFile.read())
    toResFile.close()
    resFile.close()
    # 将data下的images和runs.detect清空
    os.remove(to)
    filelist = []
    rootDir = r"./runs/detect"
    filelist = os.listdir(rootDir)
    for f in filelist:
        filepath = os.path.join(rootDir, f)
        if os.path.isfile(filepath):
            os.remove(filepath)
            # print filepath+" removed!"
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)
            # print "dir "+filepath+" removed!"
    return


if __name__ == "__main__":
    # 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    address = ('', 9600)
    tcp_server_socket.bind(address)
    tcp_server_socket.listen(128)
    while True:
        client_socket, client_address = tcp_server_socket.accept()
        # 接受客户端发送信息
        recv_data = client_socket.recv(1024)
        recv_data = str(recv_data)
        recv_data_url = recv_data.split('%%', -1)
        recv_data_url = recv_data_url[1]
        fun(recv_data_url)
        # 发送数据
        client_socket.send("success!".encode("utf-8"))
        # 关闭套接字
        client_socket.close()
    # tcp_server_socket.close()
