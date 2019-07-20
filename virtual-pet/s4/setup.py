from setuptools import setup

setup(
    name='virtual_pet',
    version='0.1',
    packages=['virtual_pet'],
    install_requires=['ppb'],
    author='Piper',
    entry_points={
        'console_scripts': ['virtual_pet=virtual_pet.__main__:main']
    }
)
