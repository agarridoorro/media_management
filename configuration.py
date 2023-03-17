import os
import sys
from threading import Lock

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
    def __init__(self):
        self.auth = _Reader('/config/auth.json')
        self.params = _Reader('/config/params.json')

class _Reader(object):
    def __init__(self, file_name):
        try:
            self._values_dic = []
            self._file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
            with open(file_name, 'r') as dictionary_file:
                self._values_dic = eval(dictionary_file.read())
        except FileNotFoundError:
            print("No config file found at [" + self._file_name + "]")
            sys.exit(100)
        
    def get(self, key):
        try:
            return self._values_dic[key]
        except KeyError:
            print("Key [" + key + "] is not present in [" + self._file_name + "]")
            sys.exit(100)
