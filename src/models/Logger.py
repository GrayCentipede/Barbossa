class Logger(object):

    listener = None

    def __init__(self, listener):
        self.listener = listener

    def debug(self, msg):
        self.listener(msg)

    def warning(self, msg):
        self.listener(msg)

    def error(self, msg):
        self.listener(msg)
