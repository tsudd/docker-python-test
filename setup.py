from setuptools import setup
from setuptools import find_packages

setup(
    name='serializer',
    packages=['local_packages', 'local_packages/serializers'],
    version='0.1.0',
    description='Custom serializer by tsudd',
    author='tsudd',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    scripts=['bin/tsuddserializer'])
