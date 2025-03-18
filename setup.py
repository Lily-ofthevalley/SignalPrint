from setuptools import setup, find_packages

setup(
    name='my_cli_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'colorama',
        'euclid3',
        'numpy',
        'numpy-stl',
        'pillow',
        'ply',
        'prettytable',
        'pypng',
        'python-utils',
        'qrcode[pil]',
        'setuptools',
        'solidpython',
        'typing-extensions',
    ],
    entry_points={
        'console_scripts': [
            'SignalPrint=SignalPrint.cli:cli',
        ],
    },
)