from setuptools import setup, find_packages
import os  # 新增导入 os 模块

# 动态处理 requirements.txt
def get_requirements():
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            # 过滤空行和注释行
            return [
                line.strip() 
                for line in f.readlines() 
                if line.strip() and not line.startswith('#')
            ]
    else:
        return []

setup(
    name="my1ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements(),  # 调用函数获取依赖
    entry_points={
        'console_scripts': [
            'my1ai=src.main:main',
        ],
    }
)
