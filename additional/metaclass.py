from abc import abstractstaticmethod
import inspect


class StringField:

    def __init__(self):
        self.__type = str
        self.__value = str()
        self.name = None

    def __get__(self, instance, owner):
        return getattr(instance, self.name, str())

    def __set__(self, instance, value):
        assert type(value) == str
        setattr(instance, self.name, value)


class ModelCreator(type):

    def __new__(cls, name, bases, namespace):
        storage = set()
        for base in bases:
            if hasattr(base, '__slots__'):
                storage.update(base.__slots__)
        for k, v in namespace.items():
            if isinstance(v, AnyField):
                v.name = f"_{k}"
                storage.add(v.name)

        def __new__(cls, *args, **kwargs):
            instance = object.__new__(cls)
            for k, v in kwargs.items():
                if f'_{k}' in cls.__slots__:
                    setattr(instance, k, v)
            return instance

        namespace['__new__'] = __new__
        namespace['__slots__'] = list(storage)

        return super(ModelCreator, cls).__new__(cls, name, bases, namespace)

    @staticmethod
    def _custom_init(default_init):
        def field_init(self, *args, **kwargs):
            init_params = inspect.signature(default_init).parameters
            for param in init_params:
                if init_params[param]._kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
                    if self.__slots__.get(init_params[param]._name) is not None:
                        raise SyntaxError(
                            f"ModelCreator got conflict with {self.__class__}.__init__() args\nSolve conflict with attribute: '{param}'")
            # for field in self.__fields__:
            #     if kwargs.get(field) != None:
            #         self.__setattr__(field, kwargs[field])
            #         kwargs.pop(field)
            #     else:
            #         if getattr(self, field, None) == None or isinstance(getattr(self, field, None), AbstractField):
            #             raise TypeError(
            #                 f"{self.__class__}.__init__() missing required keyword-only argument: '{field}'")
            # default_init(self, *args, **kwargs)

        return field_init


class AnyField:
    def __init__(self, field_type: type):
        self._type = field_type
        self.__value = None
        self.name = None

    def field_checker(self, val):
        if isinstance(val, self._type):
            return val
        else:
            raise TypeError(f"Expected attr type is {self._type.__name__} but got {type(val)}")

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        try:
            assert type(value) == self._type
        except AssertionError:
            raise TypeError(f"Expected attr type {self._type.__name__}")
        setattr(instance, self.name, value)


class Student(metaclass=ModelCreator):
    name = AnyField(str)
    address = StringField()


