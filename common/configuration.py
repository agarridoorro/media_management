import json
from threading import Lock
from pathlib import Path
from .log import Logger
from .settings import CONFIG_PATH

class SingletonMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect the returned instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Configuration(metaclass=SingletonMeta):
    def __init__(self, entity):
        self.auth = _CfgMap(CONFIG_PATH, entity, 'auth.json')
        self.params = _CfgMap(CONFIG_PATH, entity, 'params.json')

class _CfgMap(object):
    def __init__(self, base_path, entity, relative_path):
        self._values_dic = {}
        self._file_name = Path(base_path) / entity / relative_path
        try:
            with open(self._file_name, 'r', encoding='utf-8') as f:
                self._values_dic = json.load(f)
                if not isinstance(self._values_dic, dict):
                    Logger.error("Config file[", self._file_name, "] does not contain a JSON object")
        except FileNotFoundError:
            Logger.error("No config file found at", self._file_name)
        except json.JSONDecodeError as e:
            Logger.error("Invalid JSON in", self._file_name, str(e))
        except Exception as e:
            Logger.error("Unexpected error reading", self._file_name, str(e))
        
    def get(self, key):
        try:
            return self._values_dic[key]
        except KeyError:
            Logger.error("Key [", key, "] is not present in [", self._file_name, "]")
