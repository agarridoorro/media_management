import shutil
from pathlib import Path
from .log import Logger
from .settings import CLEAN_CONFIG_PATH, CONFIG_PATH

def _copy_if_not_exists(src_path, dst_path):
    if not dst_path.exists():
        if not src_path.is_file():
            Logger.error('Source not found', src_path)
        
        dst_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            shutil.copy2(src_path, dst_path)
            Logger.info('Created', dst_path)
        except Exception as e:
            Logger.error('Failed to copy', src_path, '->', dst_path, str(e))

class FileUtils(object):

    @staticmethod
    def copy_config_file(entity, file_name):
        src = Path(CLEAN_CONFIG_PATH) / entity / file_name
        dst = Path(CONFIG_PATH) / entity / file_name
        _copy_if_not_exists(src, dst)

