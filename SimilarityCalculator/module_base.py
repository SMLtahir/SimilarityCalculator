from logger_base import LoggerBase
from config_base import ConfigBase


class BaseClass(LoggerBase, ConfigBase):
    def __init__(self):

        LoggerBase.__init__(self, self.__class__.__name__)

        self.logger.info("\nLoading config file...")
        ConfigBase.__init__(self)
        self.logger.info("JSON config file loaded.")
