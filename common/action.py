from abc import ABC, abstractmethod

class GenericAction(ABC):

    #@abstractmethod
    def init(self):
        pass

    @abstractmethod
    def execute(self):
        pass