import logging

LOG_LEVEL = logging.NOTSET
LOG_FORMAT = f'[%(name)s/%(funcName)s/] [%(levelname)s]: %(message)s '


class Logger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name, level=LOG_LEVEL)
        self._set_handlers_file()

    def _set_handlers_console(self):
        formatter_console = logging.Formatter(LOG_FORMAT)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter_console)
        self.addHandler(console_handler)

    def _set_handlers_file(self):
        formatter_file = logging.Formatter(LOG_FORMAT)
        file_handler = logging.FileHandler('LOGGING.log')
        file_handler.setFormatter(formatter_file)
        self.addHandler(file_handler)
