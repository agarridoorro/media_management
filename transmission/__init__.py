from common.log import Logger
from common.file import FileUtils

Logger.info("Initializing transmission module...")
FileUtils.copy_config_file('transmission', 'auth.json')
FileUtils.copy_config_file('transmission', 'params.json')