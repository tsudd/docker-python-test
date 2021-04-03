import re
import inspect
from types import FunctionType, CodeType

FUNCTION_CLASS_NAME = "function"
FUNCTION_ATTRS_NAMES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__closure__",
]

CODE_FIELD_NAME = "__code__"

TYPE_FIELD_NAME = "TYPE"
VALUE_FIELD_NAME = "VALUE"

CLASS_TYPE_REGEX = "\'([\w\W]+)\'"


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


def deserialize_function(f: dict):
    details = []
    fields = f[VALUE_FIELD_NAME]
    for attr in FUNCTION_ATTRS_NAMES:
        if attr == CODE_FIELD_NAME:
            details.append(CodeType(
                fields[CODE_FIELD_NAME]['VALUE']['co_argcount'],
                fields[CODE_FIELD_NAME]['VALUE']['co_kwonlyargcount'],
                fields[CODE_FIELD_NAME]['VALUE']['co_nlocals'],
                fields[CODE_FIELD_NAME]['VALUE']['co_stacksize'],
                fields[CODE_FIELD_NAME]['VALUE']['co_flags'],
                fields[CODE_FIELD_NAME]['VALUE']['co_code'],
                tuple(fields[CODE_FIELD_NAME]['VALUE']['co_consts']['VALUE']),
                tuple(fields[CODE_FIELD_NAME]['VALUE']['co_names']['VALUE']),
                tuple(fields[CODE_FIELD_NAME]['VALUE']['co_varnames']['VALUE']),
                fields[CODE_FIELD_NAME]['VALUE']['co_filename'],
                fields[CODE_FIELD_NAME]['VALUE']['co_name'],
                fields[CODE_FIELD_NAME]['VALUE']['co_firstlineno'],
                fields[CODE_FIELD_NAME]['VALUE']['co_lnotab'],
                tuple(fields[CODE_FIELD_NAME]['VALUE']['co_freevars']['VALUE']),
                tuple(fields[CODE_FIELD_NAME]['VALUE']['co_cellvars']['VALUE'])
            ))
        else:
            details.append(fields[attr])

    return FunctionType(*details)


# def deserialize_inst(obj: dict):

