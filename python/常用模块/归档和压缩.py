import os
import os.path
import shutil
'''
    归档: 把多个文件或者文件夹合并到一个文件当中
    压缩: 用算法把多个文件或者文件夹无损或者有损合并到一个文件中

'''
# make_archive() 归档操作 返回归档后的地址
print("归档img文件夹到 zip文件夹", os.linesep)
srcArchivePath = os.path.join(os.getcwd(), "shutil模块使用", "src", "img")
copyArchivePath = os.path.join(os.getcwd(), "shutil模块使用", "zip")
print("来源路径", srcArchivePath)
print("来源路径", copyArchivePath)

# 归档得到一个叫做 img.zip 的归档文件
rst = shutil.make_archive(os.path.join(copyArchivePath, "img"), "zip", srcArchivePath)
print("归档返回结果", rst)
print("*" *60, os.linesep *2)


# unpack_archive(归档文件地址, 解包后的地址) 解包操作
ua = shutil.unpack_archive(os.path.join(copyArchivePath, "img.zip"), copyArchivePath, "zip")
print("解包返回结果", ua)
print("*" *60, os.linesep *2)


import zipfile
'''
    zipfile.ZipFile(file[， mode[, compression[, allowZip64]])
        创建一个ZipFile对象，表示一个Zip文件
            参数file表示文件路径或类文件对象(file-like object)
            参数mode指示打开zip文件的模式，默认是'r',表示读已存在的zip文件，也可以时'w'或'a', 'w'表示新建一个zip文档或覆盖一个已存在的zip文档，a表示将数据附加到一个现存的zip文档中
            参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile.ZIP_STORED 或zipfile.ZIPDEFLATED。如果操作的zip文件大小超过2G，应该将allowZip64设置为True        
'''
print("ZIP...", os.linesep)
zipFilePath = os.path.join(os.getcwd(), "shutil模块使用", "zip")
zf = zipfile.ZipFile(os.path.join(zipFilePath, "img.zip"))

# ZipFile.getinfo(name) 获取zip文档内指定文件的信息，返回zipfile.ZipInfo对象，它包括文件的详细信息
rst = zf.getinfo("220.jpg")
print("img.zip文档内 220.jpg的详细信息", rst)

# ZipFile.namelist() 获取zip文档的名称列表
nl = zf.namelist()
print("img.zip文档的名称列表", nl)

# ZipFile.extractall([path[, members[, pwd]]])
# 解压zip文档中的所有文件到当前目录，参数members的默认值为zip文档内所有文件名称列表
zipFilePath = os.path.join(os.getcwd(), "shutil模块使用", "zip", "zip_img")
rst = zf.extractall(zipFilePath)
print("zip文档解压返回结果", rst)
