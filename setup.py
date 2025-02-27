from setuptools import setup, find_packages

setup(
    name="my1ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={  # 顶格对齐，配置入口点
        'console_scripts': [
            'my1ai=src.main:main',  # 这是Python语法，而非PS命令
        ],
    }
)
