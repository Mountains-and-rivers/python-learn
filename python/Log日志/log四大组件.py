'''
https://www.cnblogs.com/yyds/p/6901864.html

    四大组件
        Logger 日志器：产生日志的接口
            操作：
                logger.setLevel() 设置日志器将会处理的日志消息的最低严重级别
                logger.addHandler() 和Logger.removeHandler() 为Logger对象添加和移除处理器
                logger.addFilter() 和Logger.removeFilter() 为Logger对象添加和移除一个过滤器
                logger.debug() 产生一个debug级别的日志消息，同理info，error
                logger.exception() 创建类似于Logger.error的日志消息
                logger.log() 获取一个明确的日志level参数类创建一个日志记录

            如何得到一个Logger对象
                实列化
                logging.getLogger()

            
        Handler 处理器：把生产的日志发送到相应目的地
            操作：
                setLevel
                setFormat
                addFilter, removeFilter
            不需要直接使用，Handler是基类
                logging.StramHandler 将日志消息发送到输出Stream，如std.out, std.err或者任何file-like对象
                logging.FileHandler 将日志消息发送到磁盘文件，默认文件大小会无限增长
                logging.handlers.RotatingFileHandler 将日志消息发送到磁盘文件，并支持日志文件按大小切割
                logging.handlers.TimedRotatingFileHandler 将日志消息发送到磁盘文件，并支持日志文件按时间切割
                logging.handlers.HTTPHandler 将日志消息以GET或POST的方式发送给HTTP服务器
                logging.SMTHandler 将日志消息发送给一个指定的email邮箱
                logging.NullHandler 该handler实例会忽略error message，通常被想使用logging的library开发者使用
            
            
        Filter 过滤器：更精细地控制日志输出
            可以被Handler和Logger使用
            控制传递过来的信息的具体内容

        
        Formatter 格式器：对输出信息进行格式化
            可以实例化
            可以继承Format添加特殊内容
            三个参数
                fmt 指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
                datefmt 指定日期格式字符串，如果不指定默认使用"%Y-%m-%d %H:%M:%S"
                style python3.2新增参数，可取值为"%", "{" 和 "$",如果不指定，默认使用"%"
'''

'''
    案例
        现有一下几个日志记录的需求
            将所有级别的日志都写入磁盘文件中
            all.log文件中记录所有日志信息,日志格式: 日期时间 - 日志级别 - 日志信息
            error.log文件中单独记录error及以上级别的日志信息，日志格式：日期时间 - 日志级别 - 文件名[:行号] - 日志信息
            all.log在每天凌晨进行日志切割
'''
import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# 为两个不同文件设置不同handler
rf_handler = logging.handlers.TimedRotatingFileHandler("all.log", when="midnight", interval=1, backupCount=7, atTime=datetime.time(0,0,0,0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler("error.log")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 添加handler
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

# 产生日志
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
