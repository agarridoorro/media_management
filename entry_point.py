import sys
from common.log import Logger
from common.module import ModuleCreator

action_name = sys.argv[1]
#action_name = "transmission.actions.CleanAction" #for test purposes
#action_name = "subtitles.actions.DownloadAction" #for test purposes

module_creator = ModuleCreator(action_name)
ActionClass = module_creator.get_action()
action = ActionClass()

Logger.info("Executing:", module_creator.action_name)

action.init()
action.execute()
