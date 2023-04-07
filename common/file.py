import os
import shutil
from pathlib import Path
from .log import Logger
from . import *

def _copy_if_not_exists(src, dst):
    parent_dst = Path(dst).parent.absolute()
    if not os.path.isdir(parent_dst):
        parent_src = Path(src).parent.absolute()
        os.mkdir(parent_dst)
        Logger.info('Created', parent_src)
    if not os.path.isfile(dst):
        shutil.copyfile(src, dst)
        Logger.info('Created', dst)

class FileUtils(object):

    @staticmethod
    def copy_config_file(entity, file_name):
        src = os.path.join(CLEAN_CONFIG_PATH, entity, file_name)
        dst = os.path.join(CONFIG_PATH, entity, file_name)
        _copy_if_not_exists(src, dst)

