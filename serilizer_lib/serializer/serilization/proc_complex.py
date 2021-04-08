import re
import inspect
from types import FunctionType, CodeType

from serilizer_lib.serializer.serilization.serilization_config import *


def serialize_obj(obj):
    ans = {}
    tp = type(obj)

    ans[TYPE_FIELD_NAME] = re.search(CLASS_TYPE_REGEX, str(tp)).group(1)
    if tp == dict:
        for name, o in obj.items():
            ans[name] = serialize_obj(obj)
    elif tp == list or tp == tuple:
        ans[VALUE_FIELD_NAME] = []
        for o in obj:
            ans[VALUE_FIELD_NAME].append(serialize_obj(o))
    elif inspect.isroutine(obj):
        ans[VALUE_FIELD_NAME] = serialize_function(obj)
    elif isinstance(obj, (int, bytes, float, complex, bool, str)) or obj is None:
        return obj
    else:
        ans[VALUE_FIELD_NAME] = serialize_inst(obj)

    return ans


def serialize_function(f: object):
    ans = {}
    details = inspect.getmembers(f)
    for detail in details:
        if detail[0] in FUNCTION_ATTRS_NAMES:
            ans[detail[0]] = serialize_obj(detail[1])

    return ans


def serialize_inst(inst: object):
    ans = {}

    attrs = inspect.getmembers(inst)
    for attr in attrs:
        if callable(attr[1]):
            continue
        ans[attr[0]] = serialize_obj(attr[1])

    return ans


def deserialize_obj(obj: dict):
    tp = type(obj)
    if tp == dict:
        try:
            return get_inst_with_name(obj[TYPE_FIELD_NAME], obj[VALUE_FIELD_NAME])
        except KeyError:
            return obj
    else:
        return obj


def get_inst_with_name(typ: str, val):
    if typ == "tuple":
        return tuple(val)
    elif typ == "function":
        return deserialize_function(val)
    else:
        return deserialize_obj(val)


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
    details.append(glob)
    for attr in FUNCTION_ATTRS_NAMES:
        if attr == CODE_FIELD_NAME:
            continue
        details.append(deserialize_obj(f[attr]))

    return FunctionType(*details)


# def deserialize_inst(obj: dict):

