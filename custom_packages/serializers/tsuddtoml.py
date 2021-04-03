import toml
from custom_packages.serializers.proc_complex import serialize_obj
from types import FunctionType, CodeType


def dumps(s):
    return toml.dumps(s)


def dump(s, fp):
    s = toml.dumps(s)
    fp.write(s)


def load(fp):
    return fp.load(fp)


def loads(s):
    return toml.loads(s)


def sum(a=0, b=0):
    return a + b


def solve():
    noce = 99

    sum.__setattr__("nice", solve)
    sum.__setattr__("num", 228)

    # print(dumps(sum))
    # print(yaml.dump(sum))
    ass = {"cool": ["228", "nice"], "gogo": {"good": "boy", "nice": 229, "dont": {"lol": 20.9}}}
    oo = dumps(ass)
    print(loads(oo.replace(",]", " ]")))
    co = sum.__code__
    print(co.co_argcount, co.co_kwonlyargcount,
             co.co_nlocals, co.co_stacksize, co.co_flags,
             co.co_code, co.co_consts, co.co_names,
             co.co_varnames, co.co_filename,
             'MyNewCodeName',
             co.co_firstlineno, co.co_lnotab, co.co_freevars,
             co.co_cellvars)
    p = serialize_obj(sum)
    print(
        p['VALUE']["__code__"]['VALUE']['co_argcount'],
        p['VALUE']["__code__"]['VALUE']['co_kwonlyargcount'],
        p['VALUE']["__code__"]['VALUE']['co_nlocals'],
        p['VALUE']["__code__"]['VALUE']['co_stacksize'],
        p['VALUE']["__code__"]['VALUE']['co_flags'],
        p['VALUE']["__code__"]['VALUE']['co_code'],
        tuple(p['VALUE']["__code__"]['VALUE']['co_consts']['VALUE']),
        tuple(p['VALUE']["__code__"]['VALUE']['co_names']['VALUE']),
        tuple(p['VALUE']["__code__"]['VALUE']['co_varnames']['VALUE']),
        p['VALUE']["__code__"]['VALUE']['co_filename'],
        p['VALUE']["__code__"]['VALUE']['co_name'],
        p['VALUE']["__code__"]['VALUE']['co_firstlineno'],
        p['VALUE']["__code__"]['VALUE']['co_lnotab'],
        tuple(p['VALUE']["__code__"]['VALUE']['co_freevars']['VALUE']),
        tuple(p['VALUE']["__code__"]['VALUE']['co_cellvars']['VALUE']))
    details = [
        CodeType(
            p['VALUE']["__code__"]['VALUE']['co_argcount'],
            p['VALUE']["__code__"]['VALUE']['co_posonlyargcount'],
            p['VALUE']["__code__"]['VALUE']['co_kwonlyargcount'],
            p['VALUE']["__code__"]['VALUE']['co_nlocals'],
            p['VALUE']["__code__"]['VALUE']['co_stacksize'],
            p['VALUE']["__code__"]['VALUE']['co_flags'],
            p['VALUE']["__code__"]['VALUE']['co_code'],
            tuple(p['VALUE']["__code__"]['VALUE']['co_consts']['VALUE']),
            tuple(p['VALUE']["__code__"]['VALUE']['co_names']['VALUE']),
            tuple(p['VALUE']["__code__"]['VALUE']['co_varnames']['VALUE']),
            p['VALUE']["__code__"]['VALUE']['co_filename'],
            p['VALUE']["__code__"]['VALUE']['co_name'],
            p['VALUE']["__code__"]['VALUE']['co_firstlineno'],
            p['VALUE']["__code__"]['VALUE']['co_lnotab'],
            tuple(p['VALUE']["__code__"]['VALUE']['co_freevars']['VALUE']),
            tuple(p['VALUE']["__code__"]['VALUE']['co_cellvars']['VALUE']),
        ),
        {},
        p['VALUE']["__name__"],
        tuple(p['VALUE']["__defaults__"]["VALUE"]),
        p['VALUE']["__closure__"]
    ]
    id2 = FunctionType(*details)
    print(id2(2, 2))
    pass
