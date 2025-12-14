from common.file import FileUtils
from common.log import Logger

class Initializer(object):

    @staticmethod
    def init():
        FileUtils.copy_config_file('transmission', 'auth.json')
        FileUtils.copy_config_file('transmission', 'params.json')