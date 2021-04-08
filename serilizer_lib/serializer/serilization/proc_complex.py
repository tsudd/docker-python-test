import re
import inspect
from types import FunctionType, CodeType

from serilizer_lib.serializer.serilization.serilization_config import *


def serialize_obj(obj):
    result = {}
    tp = type(obj)

    type_string = re.search(CLASS_TYPE_REGEX, str(tp)).group(1)
    if tp == dict:
        for name, o in obj.items():
            result[name] = serialize_obj(o)
    elif tp == list or tp == tuple:
        result[TYPE_FIELD_NAME] = type_string
        result[VALUE_FIELD_NAME] = []
        for o in obj:
            result[VALUE_FIELD_NAME].append(serialize_obj(o))
    elif inspect.isroutine(obj):
        result[TYPE_FIELD_NAME] = type_string
        result[VALUE_FIELD_NAME] = serialize_function(obj)
    elif isinstance(obj, (int, bytes, float, complex, bool, str)) or obj is None:
        return obj
    else:
        result[TYPE_FIELD_NAME] = type_string
        result[VALUE_FIELD_NAME] = serialize_inst(obj)

    return result


def serialize_function(f: object):
    result = {}
    details = inspect.getmembers(f)
    for detail in details:
        if detail[0] in FUNCTION_ATTRS_NAMES:
            result[detail[0]] = serialize_obj(detail[1])
            if detail[0] == CODE_FIELD_NAME:
                result[GLOBAL_FIELD_NAME] = {}
                glob = f.__getattribute__(GLOBAL_FIELD_NAME)
                for name in detail[1].__getattribute__(GLOBALS_NAMES_FIELD):
                    if name in glob:
                        result[GLOBAL_FIELD_NAME][name] = serialize_obj(glob[name])

    return result


def serialize_inst(inst: object):
    result = {}

    attrs = inspect.getmembers(inst)
    for attr in attrs:
        if callable(attr[1]):
            continue
        result[attr[0]] = serialize_obj(attr[1])

    return result


def deserialize_obj(obj):
    typ = type(obj)
    if typ == dict:
        result = {}
        if VALUE_FIELD_NAME in obj and TYPE_FIELD_NAME in obj:
            return get_inst_with_name(obj[TYPE_FIELD_NAME], obj[VALUE_FIELD_NAME])
        for name, o in obj.items():
            tp = type(o)
            if tp == dict:
                result[name] = deserialize_obj(o)
            else:
                result[name] = o
        return result
    return obj


def get_inst_with_name(typ: str, val):
    if typ == "tuple":
        return tuple(val)
    elif typ == "function":
        return deserialize_function(val)
    else:
        return val


def deserialize_function(f: dict):
    details = [CodeType(
        f[CODE_FIELD_NAME]['VALUE']['co_argcount'],
        f[CODE_FIELD_NAME]['VALUE']['co_posonlyargcount'],
        f[CODE_FIELD_NAME]['VALUE']['co_kwonlyargcount'],
        f[CODE_FIELD_NAME]['VALUE']['co_nlocals'],
        f[CODE_FIELD_NAME]['VALUE']['co_stacksize'],
        f[CODE_FIELD_NAME]['VALUE']['co_flags'],
        f[CODE_FIELD_NAME]['VALUE']['co_code'],
        tuple(f[CODE_FIELD_NAME]['VALUE']['co_consts']['VALUE']),
        tuple(f[CODE_FIELD_NAME]['VALUE']['co_names']['VALUE']),
        tuple(f[CODE_FIELD_NAME]['VALUE']['co_varnames']['VALUE']),
        f[CODE_FIELD_NAME]['VALUE']['co_filename'],
        f[CODE_FIELD_NAME]['VALUE']['co_name'],
        f[CODE_FIELD_NAME]['VALUE']['co_firstlineno'],
        f[CODE_FIELD_NAME]['VALUE']['co_lnotab'],
        tuple(f[CODE_FIELD_NAME]['VALUE']['co_freevars']['VALUE']),
        tuple(f[CODE_FIELD_NAME]['VALUE']['co_cellvars']['VALUE'])
    )]
    glob = {"__builtins__": __builtins__}
    for name, o in f[GLOBAL_FIELD_NAME].items():
        glob[name] = deserialize_obj(o)
    details.append(glob)
    for attr in FUNCTION_ATTRS_NAMES:
        if attr == CODE_FIELD_NAME:
            continue
        details.append(deserialize_obj(f[attr]))

    return FunctionType(*details)


# def deserialize_inst(obj: dict):

