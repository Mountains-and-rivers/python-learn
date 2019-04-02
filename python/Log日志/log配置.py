import logging

LOG_FORMAT = "%(asctime)s     %(levelname)s  ---------------------------  %(message)s"
# 若不对日志进行配置filename，则直接输出到控制台
# 日志配置：filename日志保存文件路径和名字，level日志级别，默认为warning，format日志输出格式
logging.basicConfig(filename="mylog.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("this is a debug")
logging.warning("this is a warning")
logging.error("this is a error")
