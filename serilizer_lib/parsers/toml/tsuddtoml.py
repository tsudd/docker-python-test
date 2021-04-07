import toml
from serilizer_lib.serializer.serilization.proc_complex import serialize_obj, deserialize_function


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
    n = 229
    print(n)
    n += 327
    print(n)
    return a + b


def solve():
    noce = 99

    sum.__setattr__("nice", solve)
    sum.__setattr__("num", 228)

    # print(dumps(sum))
    # print(yaml.dump(sum))
    ass = {"cool": ["228", "nice"], "gogo": {"good": "boy", "nice": 229, "dont": {"lol": 20.9}}}
    oo = dumps(ass)
    sum(2, 2)
    aba = sum.__globals__
    sts = sum.__code__
    bbt = sum.__closure__
    s = serialize_obj(sum)
    iddd = deserialize_function(s)
    print(iddd(2, 2))
    bts = iddd.__globals__
    pass
