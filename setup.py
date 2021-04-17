from setuptools import setup
from setuptools import find_packages

setup(
    name='serializer',
    packages=[
        'serilizer_lib',
        'serilizer_lib/serializer',
        'serilizer_lib/parser_factory',
        'serilizer_lib/serializer/serilization',
        'serilizer_lib/parsers/json',
        'serilizer_lib/parsers/yaml',
        'serilizer_lib/parsers/toml',
        'serilizer_lib/parsers',
        'serilizer_lib/parser_factory/parser_objects',
        'serilizer_lib/parser_factory/parser_objects/json',
        'serilizer_lib/parser_factory/parser_objects/toml',
        'serilizer_lib/parser_factory/parser_objects/yaml'
    ],
    version='0.2.0',
    description='Custom serializer by tsudd',
    author='tsudd',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    scripts=['bin/tsuddserializer']
)
