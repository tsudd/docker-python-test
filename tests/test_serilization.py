from serilizer_lib.serializer.serilization.proc_complex import serialize_obj, deserialize_obj
from tests.test_config import sum_two_elements, fib_nums
import yaml


def test_func_serialization():
    ser = serialize_obj(sum_two_elements)
    deser_func = deserialize_obj(ser)
    assert deser_func(2, 2) == sum_two_elements(2, 2)


def test_lambda():
    l = lambda x: x*x
    deser_lambda = deserialize_obj(l)
    assert deser_lambda(2) == l(2)


def test_recursive_func():
    ser = serialize_obj(fib_nums)
    deser_func = deserialize_obj(ser)
    assert deser_func(10) == fib_nums(10)


def test_other_func():
    fs = open("tests/rez11.yaml", "r")
    d = yaml.load(fs, Loader=yaml.FullLoader)
    fs.close()
    o = deserialize_obj(d)
    assert o(1, 2) == 225

