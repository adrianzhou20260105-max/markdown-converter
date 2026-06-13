# 📄 Markdown 文档转换工具 (网页版)

基于微软开源的 **Microsoft MarkItDown** 技术构建的文档转 Markdown 网页版工具。支持上传一个或多个不同格式的文件，一键转换为 Markdown，并提供实时预览、单文件下载及打包 ZIP 下载功能。

---

## 🌟 功能特点

- **多文件批量上传**：支持直接拖拽或点击上传多个文件。
- **广泛的文件格式支持**：
  - **文档**：`.pdf`, `.docx`, `.html`, `.htm`, `.txt`, `.md`
  - **演示文稿**：`.pptx`
  - **电子表格**：`.xlsx`, `.xls`, `.csv`
  - **结构化/音频等其他文件**：`.json`, `.xml`, `.mp3`, `.wav` (语音转文字)
- **实时效果预览**：提供“渲染效果预览”和“Markdown 源码”双标签页对照查看。
- **灵活的下载选项**：支持单独下载某个转换后的 `.md` 文件，或一键打包下载全部转换文件的 `.zip` 压缩包。
- **极其简便的部署**：已针对 Streamlit Community Cloud 进行优化，支持一键零成本部署到公网。

---

## 💻 本地运行

在本地运行该网页应用非常简单：

1. **克隆或下载本项目** 到本地电脑。
2. **进入项目目录**：
   ```powershell
   cd "D:\my_project\markdown格式转换"
   ```
3. **激活虚拟环境**（若您使用本项目自带的 `.venv`）：
   ```powershell
   .venv\Scripts\activate
   ```
4. **安装依赖**：
   ```powershell
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```
5. **运行网页服务**：
   ```powershell
   streamlit run streamlit_app.py
   ```
6. 浏览器会自动打开以下地址：
   ```text
   http://localhost:8501
   ```

---

## 🚀 免费公网部署指南

此网页应用支持通过 **Streamlit Community Cloud** 免费部署至互联网，方便您在任何设备上随时访问和分享：

### 第一步：将代码推送到 GitHub
1. 打开您的 GitHub 账号，创建一个新的公开仓库，例如命名为 `markdown-converter`。
2. 在本地项目根目录初始化 Git 并将代码推送到您的 GitHub 仓库：
   ```powershell
   git init
   git add .
   git commit -m "Initialize markdown converter web app"
   git branch -M main
   git remote add origin https://github.com/<您的GitHub用户名>/markdown-converter.git
   git push -u origin main
   ```

### 第二步：部署到 Streamlit Community Cloud
1. 访问 [Streamlit Community Cloud 官网](https://share.streamlit.io/)。
2. 使用您的 GitHub 账号授权登录。
3. 点击页面右上角的 **"Create App"** 或 **"New app"**。
4. 填写部署表单：
   - **Repository**: 选择您的 `markdown-converter` 仓库。
   - **Branch**: 选择 `main`。
   - **Main file path**: 填写 `streamlit_app.py`。
5. 点击 **"Deploy!"** 按钮。
6. 等待几分钟，系统会自动完成环境构建和依赖安装。部署完成后，您将获得一个专属的公网链接（如 `https://xxx.streamlit.app`），即可在网上任意使用该工具！

---

## 🛠️ 技术栈
- 网页框架：[Streamlit](https://streamlit.io/)
- 转换内核：[Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- 音频转换/表格解析/文档转换等辅助依赖件见 `requirements.txt`。
