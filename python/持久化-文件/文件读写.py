'''
   文件  长久保存信息的一种数据信息集合

       oppen函数
           open函数负责打开文件，带有很多参数
           第一个参数必须有，文件路径和名称
           mode 表明文件用什么方式打开
               r 以只读方式打开
               w 以写方式打开，覆盖以前的内容, 若不存在文件则新建后打开
               x 创建方式打开， 如文件已存在，报错
               a append方式，以追加方式对文件内容进行写入
               b binary方式，二进制方式写入
               t 文本方式打开
               + 可读写
'''
# 打开文件，用写的方式
# f称之为句柄
# 文件打开后必须关闭
# r表示后面的字符串内容不需要转义
f = open(r"test01.txt", 'r')
f.close()



'''
    with语句
        with语句使用的技术是一种称为上下文管理协议的技术(ContextManagementProtocal)
        自动判断文件的作用域，自动关闭不再使用的文件句柄
    with open(r"test01.txt", 'r') as f:
        pass
        # 下面语句块开始对文件f进行操作
        # 在本模块中不需要使用close关闭文件f
'''
# with案例
with open(r"test01.txt", "r") as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整的读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()
print("*" *60)


# list能用打开的文件为参数，把文件内每一行内容作为一个元素
with open(r"test01.txt", "r") as f:
    l = list(f)
    for line in l:
        print(line)
print("*" *60)


# read是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果不指定，则从当前位置读取到结尾, 否则从当前位置读取指定个字符
with open(r"test01.txt", "r") as f:
    strChar = f.read(4)
    print(strChar)
print("*" *60)

'''
    seek(offset, from) 移动文件读取指针
        from 的取值范围
            0: 从文件开始偏移
            1: 从当前位置开始偏移
            2: 从文件末尾开始偏移
            
        偏移单位为字节(byte)
            一个汉字为几个字节
'''
# seek案例
with open(r"test01.txt", "r") as f:
    f.seek(6, 0)
    strChar = f.read(5)
    print(strChar)
print("*" *60)


# tell() 显示当前文件指针位置 返回数字的单位是字节
with open(r"test01.txt", "r") as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        print(strChar)
        print(pos)
        strChar = f.read(3)
        pos = f.tell()
print("*" *60)
print()
print()


'''
    文件写操作 write
        write(str) 参数是一个字符串，就是你要写入文件的内容
        writelines(sequence) 参数是序列，比如列表，它会迭代帮你写入文件
'''
# 文件末尾追加内容
with open(r"test01.txt", "a") as f:
    f.write("welcome to my work!")
