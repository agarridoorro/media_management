import os
from threading import Lock
from .log import Logger
from . import *

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
        try:
            self._values_dic = []
            self._file_name = os.path.join(base_path, entity, relative_path)
            with open(self._file_name, 'r') as dictionary_file:
                self._values_dic = eval(dictionary_file.read())
        except FileNotFoundError:
            Logger.error("No config file found at [", self._file_name, "]")
        
    def get(self, key):
        try:
            return self._values_dic[key]
        except KeyError:
            Logger.error("Key [", key, "] is not present in [", self._file_name, "]")
