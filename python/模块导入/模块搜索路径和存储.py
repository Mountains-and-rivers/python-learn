import sys
'''
    系统默认的模块搜索路径
        import sys
        sys.path 属性可以获取到路径列表

    添加搜索路径
        sys.path.append(dir)
    模块的加载顺序
        先搜索内存中已经加载好的模块
        搜索python内置模块
        搜索sys.path路径
'''
print(type(sys.path))
print("-" *60)

for p in sys.path:
    print(p)
print("-" *60)

# 添加搜索路径
sys.path.append("E://newPath")

for p in sys.path:
    print(p)
