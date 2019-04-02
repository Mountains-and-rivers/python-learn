'''
    os 操作系统相关
    与系统相关的操作主要在三个模块里:
        os 操作系统目录
        os.path 系统路径相关操作
        shutil 高级文件操作，目录树的操作，文件赋值、删除、移动
'''
import os

# os.getcwd() 获取当前工作目录

mydir = os.getcwd()
print("当前工作目录:", mydir)
print("*" *60)

# os.chdir() 改变当前工作目录
os.chdir("C:\\Users\Archangel\Desktop\py知识点")
mydir = os.getcwd()
print("更改后的工作目录:", mydir)
print("*" *60)

# os.listdir() 获取目录中所有子目录和文件的名称列表
print("当前工作目录下的文件夹及文件")
ld = os.listdir()
print(ld)
print("*" *60)

# os.makedirs() 递归创建文件夹 递归路径：多个文件夹层层包含的路径
print("创建文件夹")
#rst = os.makedirs("make文件夹")
print("*" *60)

# os.system() 运行系统shell命令，返回值是打开一个shell或者终端界面
# 一般推荐使用subprocess模块代替
# 使用note执行看不到效果
rst = os.system("ls")
print(rst)
print("*" *60)

# os.getenv() 获取指定的系统环境变量 相对应的有os.putenv()
rst = os.getenv("JAVA_HOME")
print(rst)
print("*" *60)

'''
    值部分
        os.curdir current dir 当前目录
        os.pardir parent dir 父目录
        os.sep 当前系统路径分隔符
            windows: "\"
            linux: "/"
        os.linesep 当前系统的换行符(不可见)
            windows: "\r\n"
            unix,linux,macos: "\n"
        os.name 当前系统名称
            windows: "nt"
            linux,mac,unix: "posix"
    在路径相关操作中不建议手动拼写地址，因为手动拼写的地址不具有可移植性
'''
print("当前目录", os.curdir)
print("父目录", os.pardir)
print("当前系统路径分隔符", os.sep)
print("当前系统换行符(不可见)", os.linesep)
print("当前系统名称", os.name)
