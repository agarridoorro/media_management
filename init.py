from common.log import Logger
from common.action_factory import ActionFactory

Logger.info('Initializing modules...')

file_cron = open('mycron')
lines = file_cron.readlines()
for line in lines:
    if not line.startswith('#') and ' python3 /app/entry_point.py ' in line:
        parts = line.split(' ')
        index_entry_point = parts.index('/app/entry_point.py')
        action_name = parts[index_entry_point + 1]
        action = ActionFactory.get_instance(action_name)
        action.init()
