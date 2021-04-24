class BadJSONException(BaseException):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return "Error while parsing: bad JSON."
