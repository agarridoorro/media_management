from common.log import Logger
from abc import ABC, abstractmethod

class GenericAction(ABC):

    def init(self, *args, **kwargs):
        class_name = f"{self.__class__.__module__}.{self.__class__.__qualname__}"
        Logger.info(f"Initializing {class_name}")
        try:
            return self._init(*args, **kwargs)
        finally:
            Logger.info(f"Initialized {class_name}")

    @abstractmethod
    def _init(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        class_name = f"{self.__class__.__module__}.{self.__class__.__qualname__}"
        Logger.info(f"Executing {class_name}")
        try:
            return self._execute(*args, **kwargs)
        finally:
            Logger.info(f"Executed {class_name}")        

    @abstractmethod
    def _execute(self, *args, **kwargs):
        pass