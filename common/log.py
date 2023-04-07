from datetime import datetime
import sys

class Logger(object):

    @staticmethod
    def info(*values):
        print(datetime.now(), 'INFO', ' '.join([str(i) for i in values]))

    @staticmethod
    def warn(*values):
        print(datetime.now(), 'WARN', ' '.join([str(i) for i in values]))

    @staticmethod
    def error(*values):
        print(datetime.now(), 'ERROR', ' '.join([str(i) for i in values]))
        sys.exit(0)