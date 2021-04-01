from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Abstract class of a parser, which has all necessary methods to process different data formats.
    """
    @abstractmethod
    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        pass

    @abstractmethod
    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        pass

    @abstractmethod
    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        pass

    @abstractmethod
    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        pass