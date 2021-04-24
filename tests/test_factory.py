from serilizer_lib.parser_factory.factory import ParserFactory
from serilizer_lib.serializer.Serializer import Serializer
from serilizer_lib.parsers.toml import tsuddtoml as custom_toml
import json
import yaml
from tests.test_config import sum_two_elements

d = {"niceNone": None, "goodnums": [22.6, 33, 2e5], "ohhyes": True, "uegay": False}


def test_jsonparser():
    par = ParserFactory.get_parser("json")
    assert par.loads(par.dumps(d)) == json.loads(json.dumps(d))


def test_tomlparser():
    par = ParserFactory.get_parser("toml")
    assert par.loads(par.dumps(d)) == custom_toml.loads(custom_toml.dumps(d))


def test_yamlparser():
    par = ParserFactory.get_parser("yaml")
    assert par.loads(par.dumps(d)) == yaml.load(yaml.dump(d), Loader=yaml.FullLoader)


def test_tomlload():
    par = ParserFactory.get_parser("toml")
    f = open("./tests/test.toml", "r")
    file = {"goodnums": [22.6, 33, 2e5], "niceNone": None, "ohhyes": True, "uegay": False}
    rez = par.load(f)
    f.close()
    assert str(file) == str(rez)


def test_serializer_setting():
    par = ParserFactory.get_parser("json")
    par.set_serializer(Serializer())
    assert par.loads(par.dumps(d)) == json.loads(json.dumps(d))


def test_load_yaml():
    par = ParserFactory.get_parser("yaml")
    fp = open("./tests/rez11.yaml", "r")
    rez = par.load(fp)
    assert str(rez.__name__) == str(sum_two_elements.__name__)


def test_dump_json():
    par = ParserFactory.get_parser("json")
    fp = open("./tests/test.json", "w")
    par.dump(d, fp)
    fp.close()
    fp = open("./tests/test.json", "r")
    s = fp.read()
    fp.close()
    assert s == json.dumps(Serializer().serialize_obj(d))
