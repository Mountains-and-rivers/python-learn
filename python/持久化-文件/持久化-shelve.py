'''
    持久化 shelve
        持久化工具  一种数据库
        类似字典，用kv对保存数据， 存取方式同字典
        open， close
'''
import shelve

# 使用shelve创建文件并使用
shv = shelve.open(r"shv.db")
shv["one"] = 1
shv["two"] = 2
shv["three"] = 3
shv.close()
# 通过以上案例发现，shelve创建的不仅仅是一个shv.db文件，还包括其它格式文件
# shelve读取
shv = shelve.open(r"shv.db")
try:
    print(shv["one"])
    print(shv["four"])# 不存在的属性报错, 所以shelve不执行后面的close
except Exception as e:
    print("error")
finally:
    shv.close()

'''
    shelve特性
        不支持多个应用并行写入，可多应用并行读取
            为了解决这个问题，open的时候可以使用flag=r
        写回问题
            shelve的默认情况下不会灯带持久化对象进行任何修改
            解决方法：强制写回: writeback=True
'''
# 以只读打开
shv = shelve.open(r"shv.db", flag='r')
try:
    kl = shv["one"]
    print(kl)
finally:
    shv.close()

# 读取shelve里的值
shv = shelve.open(r"shv.db")
try:
    shv["one"] = {"a":1, "b":2, "c":3}
finally:
    shv.close()

shv = shelve.open(r"shv.db")
try:
    one = shv["one"]
    print(one)
finally:
    shv.close()
                 
# 更改shelve里的值, 不成功
shv = shelve.open(r"shv.db") #未使用强制写回
# shv = shelve.open(r"shv.db", writeback=True) #使用强制写回
try:
    k1 = shv["one"]
    print(k1)
    # 若没有使用强制写回，一旦shelve关闭，则内容仍在内存中，没有写回到数据库
    k1["a"] = 100
finally:
    shv.close()
    
shv = shelve.open(r"shv.db")
try:
    one = shv["one"]
    print(one)
finally:
    shv.close()
