import sys
from common.action_factory import ActionFactory

action_name = sys.argv[1]
#action_name = "transmission.actions.CleanAction" #for test purposes
#action_name = "subtitles.actions.DownloadAction" #for test purposes

action = ActionFactory.get_instance(action_name)

action.init()
action.execute()
