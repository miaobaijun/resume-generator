@"
from setuptools import setup, find_packages

setup(
    name="my1ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'my1ai=src.cli:main',
        ],
    }
)
"@ | Out-File -FilePath setup.py -Encoding utf8
