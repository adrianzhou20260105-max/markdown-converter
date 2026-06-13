# 📄 Markdown Document Converter (Web Edition) / Markdown 文档转换工具 (网页版)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://adrianzhou20260105-max-markdown-converter-streamlit-app-6ej60u.streamlit.app/)
[![GitHub license](https://img.shields.io/github/license/adrianzhou20260105-max/markdown-converter?style=flat-square)](https://github.com/adrianzhou20260105-max/markdown-converter)
[![Built with Microsoft MarkItDown](https://img.shields.io/badge/Built%20with-Microsoft%20MarkItDown-blue?style=flat-square)](https://github.com/microsoft/markitdown)

A web-based tool powered by Microsoft **MarkItDown** for converting files (PDF, Word, Excel, PowerPoint, Audio, etc.) to Markdown with real-time previews and batch downloads.

基于微软开源 **Microsoft MarkItDown** 核心构建的文档转 Markdown 网页端工具。支持批量上传、实时渲染预览、单文件及打包 ZIP 下载，并且完全免费、开源。

---

## ⚡ Try It Online / 在线体验

👉 **[https://adrianzhou20260105-max-markdown-converter-streamlit-app-6ej60u.streamlit.app/](https://adrianzhou20260105-max-markdown-converter-streamlit-app-6ej60u.streamlit.app/)**

---

## 🌟 Features / 核心亮点

### English
- **Batch Upload & Convert**: Drag and drop multiple files to convert them all at once.
- **Rich Format Support**:
  - **Documents**: `.pdf`, `.docx`, `.html`, `.htm`, `.txt`, `.md`
  - **Spreadsheets**: `.xlsx`, `.xls`, `.csv` (Converts sheet data into clean Markdown tables!)
  - **Presentations**: `.pptx` (Linearizes slide layouts)
  - **Audio (Speech-to-Text)**: `.mp3`, `.wav` (Transcribes audio into written Markdown notes)
  - **Structured Data**: `.json`, `.xml`
  - **Archives**: `.zip` (Extracts and batch converts supported contents inside)
- **Live Preview**: Dual-panel preview supporting both rendered HTML layout and raw Markdown code.
- **Download Flexibly**: Download converted files individually, or grab them all in a single `.zip` package.
- **Privacy & Free**: 100% open source, running entirely on secure serverless environments.

### 中文
- **批量拖拽上传**：支持一次性拖拽上传多个不同类型的文件进行队列化批量转换。
- **全格式支持**：
  - **文档**：`.pdf` (电子版)、`.docx`、`.html`、`.txt`
  - **表格转换**：`.xlsx`、`.xls`、`.csv`，智能识别表格并排版为整齐的 **Markdown 表格**。
  - **幻灯片**：`.pptx` 提取文本。
  - **音频识别**：`.mp3`、`.wav`，内置语音识别，自动将会议或录音转换为 **Markdown 文字纪要**。
  - **其他**：`.json`、`.xml` 数据整理，`.zip` 压缩包自动解压并批量转换。
- **双标签对照预览**：提供“渲染效果预览”和“Markdown 源码”双标签页对照，效果一目了然。
- **打包一键下载**：支持单个文件单独下载，或点击 “📦 一键打包下载全部 (ZIP)”。
- **开源安全**：完全透明的开源代码，不保留用户上传的文件，转换即用，安全可靠。

---

## 💻 Local Running / 本地运行

```bash
# 1. Clone the repository / 克隆仓库
git clone https://github.com/adrianzhou20260105-max/markdown-converter.git
cd markdown-converter

# 2. Activate virtual environment (if using existing .venv) / 激活虚拟环境
.venv\Scripts\activate

# 3. Install dependencies / 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 4. Start the application / 启动应用
streamlit run streamlit_app.py
```

---

## 🚀 One-Click Cloud Deployment / 一键云端部署

You can deploy your own instance of this app to Streamlit Community Cloud for free:
1. Fork this repository.
2. Go to [Streamlit Share](https://share.streamlit.io/) and click **"New app"**.
3. Select your repository, set the branch to `main`, the main file path to `streamlit_app.py`, and click **"Deploy!"**.

---

## 🛠️ Credits & Tech Stack / 致谢与技术栈
- Core Engine: [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- Web Framework: [Streamlit](https://streamlit.io/)
