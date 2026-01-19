# 项目简介

## 项目名称
Chat-LangChain

## 项目描述
Chat-LangChain 是一个基于 LangChain 框架的聊天机器人项目，旨在实现高效的文档检索、自然语言处理和交互式问答功能。项目结合了前后端技术栈，支持本地运行和云端部署，适用于构建知识问答系统、文档助手等应用场景。

---

## 项目结构

### 1. **根目录**
- **README.md**: 项目概览和使用说明。
- **Dockerfile**: 项目容器化配置。
- **Makefile**: 常用开发和部署命令。
- **pyproject.toml**: Python 项目依赖管理。
- **package.json**: 前端依赖管理。
- **DEPLOYMENT.md / PRODUCTION.md / RUN_LOCALLY.md**: 部署和运行相关文档。
- **LICENSE**: 项目开源协议。

### 2. **_scripts/**
存放脚本工具，主要用于评估和清理操作：
- **clear_index.py**: 清理索引数据。
- **evaluate_chains.py**: 测试链式调用的性能。
- **evaluate_chat_langchain.py**: 测试聊天功能。

### 3. **backend/**
后端模块，基于 Python 开发，主要负责数据处理和业务逻辑：
- **main.py**: 后端服务入口。
- **chain.py**: 定义链式调用逻辑。
- **ingest.py**: 数据导入和预处理。
- **constants.py**: 全局常量定义。
- **parser.py**: 数据解析工具。

### 4. **frontend/**
前端模块，基于 Next.js 和 Tailwind CSS 开发，提供用户交互界面：
- **app/**: 应用主目录，包含页面和组件。
  - **layout.tsx**: 全局布局。
  - **page.tsx**: 主页面。
  - **components/**: 可复用的 UI 组件（如聊天窗口、消息气泡等）。
  - **utils/**: 前端工具函数。
- **public/**: 静态资源（如图片）。
- **next.config.js**: Next.js 配置文件。
- **tailwind.config.ts**: Tailwind CSS 配置文件。

### 5. **langchain_test/**
测试模块，包含与 LangChain 相关的单元测试和工具：
- **langchain_util.py**: LangChain 工具函数。

### 6. **terraform/**
基础设施即代码（IaC）模块，基于 Terraform 管理云端资源：
- **main.tf**: Terraform 主配置文件。
- **modules/**: 模块化配置，包含后端服务的定义。

### 7. **assets/**
存放项目相关的资源文件（如图片）。

---

## 技术栈

### 后端
- **语言**: Python
- **框架**: LangChain
- **依赖管理**: pip, pyproject.toml

### 前端
- **语言**: TypeScript
- **框架**: Next.js
- **样式**: Tailwind CSS

### 基础设施
- **容器化**: Docker
- **云资源管理**: Terraform

---

## 功能亮点
1. **文档检索与问答**: 基于 LangChain 实现高效的文档处理和问答功能。
2. **模块化设计**: 前后端分离，代码结构清晰，易于扩展。
3. **多环境支持**: 提供本地运行、生产部署和云端配置的完整文档。
4. **测试覆盖**: 包含后端和 LangChain 功能的测试模块，确保代码质量。

---

## 适用场景
- 企业知识库问答系统
- 文档助手
- 教育和学习辅助工具