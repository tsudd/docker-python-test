import logging


class BadJSONException(Exception, BaseException):
    def __init__(self, message=None):
        super().__init__(self)

        if not message is None:
            logging.error(message)
            self.__str__()

    def __str__(self):
        return "Error while parsing: bad JSON."
