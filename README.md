# 📄 智能简历生成器 | Resume Generator 
[![GitHub Stars](https://img.shields.io/github/stars/miaobaijun/resume-generator?style=flat-square)](https://github.com/miaobaijun/resume-generator)
[![Coverage Status](https://coveralls.io/repos/github/miaobaijun/resume-generator/badge.svg?branch=main)](https://coveralls.io/github/miaobaijun/resume-generator)

🚀 **一键将 JSON 数据转换为专业 DOCX 简历 | 基于 Python 开发**  

![示例截图](docs/screenshot.png)  

## ✨ 功能特性  
- ✅ 从 JSON 文件快速生成标准简历  
- ✅ 支持自定义 Word 模板（`.docx` 格式）  
- ✅ 简洁命令行操作  
- ✅ [即将推出] PDF 导出支持  

---

## 🚀 快速入门  

### 环境准备  
1. **安装 Python 3.8+**  
   - [Python 官网下载](https://www.python.org/downloads/)  
   - 安装时勾选 **"Add Python to PATH"**（Windows）  
2. **克隆仓库**  
   ```bash  
   git clone https://github.com/miaobaijun/resume-generator.git  
   cd resume-generator  
   ```  
3. **安装依赖**  
   ```bash  
   pip install -r requirements.txt  
   ```  

### 基础使用（2分钟生成简历）  
1. **修改示例数据**:  
   - 复制 `example_resume.json` → 重命名为 `my_resume.json` → 按格式填写你的信息  
2. **运行生成命令**:  
   ```bash  
   python main.py --input my_resume.json --template resume_template.docx  
   ```  
3. **获取结果**: 生成文件位于 `output/resume_output.docx`  

### 进阶用法  
- **自定义模板设计**:  
  1. 用 Word 创建新模板 → 保存为 `my_template.docx`  
  2. 使用占位符标识数据插入位置（如 `{{name}}`）  
  3. 运行命令：  
     ```bash  
     python main.py --input my_resume.json --template my_template.docx  
     ```  

---

## 🤝 参与贡献  
我们欢迎任何形式的贡献！请先阅读：  
- [贡献指南](CONTRIBUTING.md)  
- [提交 Issue](https://github.com/miaobaijun/resume-generator/issues)  

---

## 📜 开源协议  
本项目基于 [MIT License](LICENSE) 授权  
