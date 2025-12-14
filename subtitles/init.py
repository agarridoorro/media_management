from common.file import FileUtils

class Initializer(object):

    @staticmethod
    def init():
        FileUtils.copy_config_file('subtitles', 'auth.json')
        FileUtils.copy_config_file('subtitles', 'params.json')