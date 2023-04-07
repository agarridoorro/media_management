import importlib
import inspect
from .log import Logger
from .action import GenericAction

class ModuleCreator():
    def __init__(self, action_name):
        self.action_name = action_name
        last_pos = action_name.rindex('.')
        self._module_name = action_name[:last_pos]
        self._class_name = action_name[last_pos + 1:]
        if self._module_name == '' or self._class_name == '':
            Logger.error("Not a class name", action_name)
        self.module = None
        self.action = None

    def get_module(self):
        try:
            if self.module is None:
                self.module = importlib.import_module(self._module_name)
            return self.module
        except ModuleNotFoundError as e:
            Logger.error("Module not found", e.msg)
    
    def get_action(self):
        if self.action is None:
            try:
                action_class = getattr(self.get_module(), self._class_name)
                if not inspect.isclass(action_class):
                    Logger.error("Class not found", self.action_name)
                if not issubclass(action_class, GenericAction):
                    Logger.error("The class", self.action_name, "is not a subclass of app.common.action.GenericAction")
                self.action = action_class
            except ValueError as e:
                Logger.error("Error getting class name", self.action_name, e.args[0])

        return self.action

