'''
    默认对 __init__.py 进行导入
        包的导入
            import package name
         使用方式
             package_name.function_name
             package_name.class_name.function_name()
    导入包中具体的模块
        import package.module
        使用方式
            package.module.function_name
            package.module.class.function_name()
            package.module.class.var
    from ... import 导入
        from package import module_name 此导入方法不执行 __init__.py里的内容
        from pagkage * 导入当前包 __init__.py里的所有函数和类, 可以直接使用
            __all__在使用 from package * 的时候， * 可以导入的内容
            __init__.py中如果为空， 或者没有 __all__ ， 那么只导入 __init__.py中的内容
            __init__.py中如果设置了__all__的值， 则按照 __all__ 指定的子包或者模块进行加载，这样才不会加载__ini__中的内容
            __all__用法
                __all__ = ["module1", "module2"]
        from package.module import * 导入模块中的内容, 可以直接使用
    
    使用别名
            import package_name as name
            import package.module_name as name

    在开发环境中经常会使用其他模块， 可以在当前包中直接导入其他模块中的内容
        import 完整的包或者模块的路径
'''
# 默认导入 __init__.py
'''
    import package
    package.newInit()
'''

# 导入具体模块
'''
    import package.PersonClass

    teacher = package.PersonClass.Person()
    teacher.say()
'''
# 使用 from pakcage import * 导入
from package_1 import *

stu = PersonClass.Person()
stu.say()

newInit()

