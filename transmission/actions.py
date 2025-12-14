from transmission_rpc import Client
from transmission_rpc import error
from common.log import Logger
from common.action import GenericAction
from common.configuration import Configuration
from .init import Initializer

class CleanAction(GenericAction):

    def _init(self):
        Initializer.init()

    def _execute(self):
        try:
            cfg = Configuration("transmission")
            cfg_host = cfg.params.get('host')
            cfg_port = cfg.params.get('port')
            auth_username = cfg.auth.get('username')
            auth_password = cfg.auth.get('password')
            
            tClient = Client(host=cfg_host, port=cfg_port, username=auth_username, password=auth_password)
            torrents = tClient.get_torrents()
            for torrent in torrents:
                if torrent.status == 'seeding' and torrent.progress == 100 and torrent.done_date is not None:
                    tClient.remove_torrent(torrent.id, False)
                    Logger.info("Torrent", torrent.name, "removed successfully")
                    
        except error.TransmissionAuthError:
            Logger.error("Username or password is incorrect")
        except error.TransmissionConnectError:
            Logger.error("Can’t connect to transmission daemon")
        except error.TransmissionError as e:
            Logger.error("Error connecting with transmission", str(e))
