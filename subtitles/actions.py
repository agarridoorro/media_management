import os
import sys
from common.log import Logger
from common.action import GenericAction
from common.configuration import Configuration
from .open_subtitles import OpenSubtitles
from .init import Initializer

class DownloadAction(GenericAction):

    def _init(self):
        Initializer.init()

    def _execute(self):
        Logger.info("Examining subtitle state...")

        base_path = '/shows'

        #config
        cfg = Configuration("subtitles")
        language = cfg.params.get('language')
        video_extensions = cfg.params.get('video_extensions')
        extensions_tuple = (*video_extensions, )

        #get movie files
        movies = []
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith(extensions_tuple):
                    full_path = os.path.join(root, file)
                    file_without_extension = os.path.splitext(full_path)[0]
                    if not os.path.isfile(file_without_extension + '.' + language + '.srt'):
                        movies.append(full_path)
        if not movies:
            Logger.info("Subtitles up to date")
            sys.exit(0)

        #download subtitles
        subtitles = OpenSubtitles()
        subtitles.login()    
        for movie in movies:
            file_info = subtitles.get_subtitle_file_info(movie, "es", False)
            if not file_info is None:
                subtitles.download_subtitle(file_info['file_no'])