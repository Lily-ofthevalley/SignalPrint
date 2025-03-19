from setuptools import setup, find_packages

setup(
    name='SignalPrint',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'click>=8.0.0',
        'numpy>=1.21.0',
        'Pillow>=8.0.0',
        'qrcode[pil]>=7.0.0',
        'numpy-stl>=2.16.0',
    ],
    entry_points={
        'console_scripts': [
            'SignalPrint=SignalPrint.cli:cli',
        ],
    },
    include_package_data=True,
    package_data={
        'SignalPrint': ['supportingFiles/*'],
    },
    python_requires='>=3.6',
)