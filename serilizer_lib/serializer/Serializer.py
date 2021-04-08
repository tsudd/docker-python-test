from serilizer_lib.serializer.serilization.proc_complex import serialize_obj, deserialize_obj


class Serializer:
    """
    Serialization class to represent any object in simple python data structures.
    """
    def serialize_obj(self, obj: object):
        """
        Returns serialized object as dictionary.
        """
        return serialize_obj(obj)

    def deserialize_obj(self, obj: dict):
        """
        Returns object from dictionary with data fields of an object.
        """
        return deserialize_obj(obj)
