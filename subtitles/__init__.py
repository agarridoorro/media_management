from common.log import Logger
from common.file import FileUtils

Logger.info("Initializing subtitles module...")
FileUtils.copy_config_file('subtitles', 'auth.json')
FileUtils.copy_config_file('subtitles', 'params.json')