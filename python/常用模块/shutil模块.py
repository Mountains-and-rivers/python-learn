import os
import os.path
import shutil

# copy(来源路径, 目标路径) 复制文件，拷贝的同时可以重命名文件
# copy2(来源路径, 目标路径) 复制文件 保留元文件(文件信息)
# copy和copy2的区别在于copy2复制文件时尽量保留元数据，如文件创建时间
    
print("拷贝 default.jsp 并命名为 default_copy.jpg", os.linesep)
# 获取路径并整合路径
srcPath = os.path.join(os.getcwd(), "shutil模块使用", "src", "default.jpg")
copyPath = os.path.join(os.getcwd(), "shutil模块使用", "copy", "default_copy.jpg")
print("来源路径", srcPath)
print("目标路径", copyPath)

rst = shutil.copy(srcPath, copyPath)
print("拷贝返回结果", rst)
print("*" *60, os.linesep *3)


# copyfile(来源路径, 目标路径) 将文件内容复制到另外一个文件当中
print("拷贝 文件.txt 中的内容到 文件_copy.txt", os.linesep)
srcFilePath = os.path.join(os.getcwd(), "shutil模块使用", "src", "文件.txt")
copyFilePath = os.path.join(os.getcwd(), "shutil模块使用", "copy", "文件_copy.txt")
print("来源路径", srcFilePath)
print("来源路径", copyFilePath)

rst = shutil.copyfile(srcFilePath, copyFilePath)
print("拷贝返回结果", rst)
print("*" *60, os.linesep *3)

# move(来源路径, 目标路径) 移动文件夹/文件
print("移动 350.jpg", os.linesep)
srcMovePath = os.path.join(os.getcwd(), "shutil模块使用", "src", "350.jpg")
copyMovePath = os.path.join(os.getcwd(), "shutil模块使用", "copy")
print("来源路径", srcMovePath)
print("来源路径", copyMovePath)

rst = shutil.move(srcMovePath, copyMovePath)
print("拷贝返回结果", rst)
