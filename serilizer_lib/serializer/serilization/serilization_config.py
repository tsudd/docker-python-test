FUNCTION_CLASS_NAME = "function"
FUNCTION_ATTRS_NAMES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__closure__",
]

CODE_FIELD_NAME = "__code__"
GLOBAL_FIELD_NAME = "__globals__"

GLOBALS_NAMES_FIELD = 'co_names'
CODE_OBJECT_ARGS = (
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
)

TYPE_FIELD_NAME = "TYPE"
VALUE_FIELD_NAME = "VALUE"

CLASS_TYPE_REGEX = "\'([\w\W]+)\'"
