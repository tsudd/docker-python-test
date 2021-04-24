import pytomlpp as toml

from serilizer_lib.parsers.toml.toml_config import *

CONS = 222


def dumps(d: dict):
    replace_values(d, None, NULL_STRING)
    return toml.dumps(d)


def dump(s, fp):
    replace_values(s, None, NULL_STRING)
    pp = toml.dumps(s)
    fp.write(pp)


def load(fp):
    result = toml.load(fp)
    print(result)
    replace_values(result, NULL_STRING, None)
    return result


def loads(s):
    result = toml.loads(s)
    replace_values(result, NULL_STRING, None)
    return result


def replace_values(d: dict, comp_obj=None, repl_obj=NULL_STRING):
    if type(d) != dict:
        return d
    for name, o in d.items():
        if type(o) == dict:
            replace_values(o, comp_obj, repl_obj)
        else:
            typ = type(o)
            if typ == list or typ == tuple:
                for i in range(len(o)):
                    if type(o[i]) == dict:
                        replace_values(o, comp_obj, repl_obj)
                    elif o[i] == comp_obj:
                        o[i] = repl_obj
            elif o == comp_obj:
                d[name] = repl_obj
