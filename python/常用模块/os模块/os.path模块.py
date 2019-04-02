import os.path

# abspath(路径) 将路径转化位绝对路径 返回路径的绝对路径形式
absp = os.path.abspath("py")
print(absp)

# basename(路径) 获取路径中最后一个文件夹或文件的名字 返回文件名字符串
bn = os.path.basename("Users\os模块.py")
print(bn)

# join(路径1, 路径2 ...) 将多个路径组合成一个路径 返回一个新的路径字符串
op = os.path.join("路径\路径1", "路径2")
print(op)

# split(路径) 将路径切割为文件夹部分和当前文件部分 返回路径和文件名组成的元组
t = os.path.split("Users\py知识点\py文件.py")
print(t)

'''
 isdir()  判断是否是目录(文件夹) 关注的是文件的类型
     判断一个路径是否是纯目录,包含文件则返回false
 exists() 判断文件是否存在 不关心文件类型
     

'''
# isdir(路径) 检查是否是目录
print("该路径是否是目录")
print("不含文件", os.path.isdir("C:\\Users\Archangel\Desktop\py知识点\常用模块\os模块"))
print("包含文件", os.path.isdir("C:\\Users\Archangel\Desktop\py知识点\常用模块\os模块\os模块.py"))

# exists(路径) 检测文件或目录是否存在
print("是否存在该路径")
print("不含文件", os.path.exists("C:\\Users\Archangel\Desktop\py知识点\常用模块\os模块"))
print("包含文件", os.path.exists("C:\\Users\Archangel\Desktop\py知识点\常用模块\os模块\os模块.py"))
