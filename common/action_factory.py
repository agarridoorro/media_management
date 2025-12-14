import importlib
import inspect
from .log import Logger
from .action import GenericAction

class ActionFactory():

    @staticmethod
    def get_instance(action_name):
        if not isinstance(action_name, str) or action_name.strip() == '':
            Logger.error("Invalid action name", action_name)

        parts = action_name.split('.')
        if len(parts) != 3 or parts[1] != "actions":
            Logger.error("Action name must be 'package.actions.ClassName'", action_name)

        module_name = parts[0] + ".actions"
        class_name = parts[2]

        if module_name == '' or class_name == '':
            Logger.error("Not a class name", action_name)

        try:
            module = importlib.import_module(module_name)
            action_class = getattr(module, class_name)

            if not inspect.isclass(action_class):
                Logger.error("Action [", action_name, "] is not a class")

            if not issubclass(action_class, GenericAction):
                Logger.error("The class [", action_name, "] is not a subclass of app.common.action.GenericAction")

            return action_class()  # Create an instance of the action class
        except ModuleNotFoundError as e:
            Logger.error("Module [", module_name, "] not found", str(e))
        except AttributeError:
            Logger.error("Class [", class_name, "] not found in module", module_name)
        except Exception as e:
            Logger.error("Error creating action [", action_name, "]", str(e))


