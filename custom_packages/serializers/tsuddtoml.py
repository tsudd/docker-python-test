import toml


def dumps(s):
    return toml.dumps(s)


def dump(s, fp):
    s = toml.dumps(s)
    fp.write(s)


def load(fp):
    return fp.load(fp)


def loads(s):
    return toml.loads(s)


def solve():
    def sum(a, b):
        return a + b

    sum.__setattr__("nice", solve)
    sum.__setattr__("num", 228)

    # print(dumps(sum))
    # print(yaml.dump(sum))
    ass = {"cool": ["228", "nice"], "gogo": {"good": "boy", "nice": 229, "dont": {"lol": 20.9}}}
    oo = dumps(ass)
    print(loads(oo.replace(",]", " ]")))
