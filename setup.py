from setuptools import setup, find_packages
import os

# ▶▶▶ 添加或替换这个函数 ▶▶▶
def get_requirements():
    try:
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            requirements = []
            for line in f:
                line = line.strip()  # 删除首尾空格
                if line and not line.startswith('#'):  # 忽略空行和注释
                    if line[0].isalpha():  # 只接受字母开头的合法包名（如"requests==2.26.0"）
                        requirements.append(line)
            return requirements
    except FileNotFoundError:
        return []  # 如果文件不存在，返回空列表
# ◀◀◀ 函数定义结束 ◀◀◀

setup(
    name="my1ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements(),  # ✅ 关键设置：这里调用函数
    include_package_data=True,
    # 其他参数（如作者、描述等）
)
