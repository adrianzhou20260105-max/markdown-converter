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

## 💡 How to Use / 使用说明

### English
1. **Upload Files**: Click on the upload box or drag and drop files (Word, Excel, PDF, Audio, etc.) onto the website.
2. **Auto Convert**: The app will automatically convert each file using `markitdown` and show a progress bar.
3. **Preview & Copy**: 
   - Click a file name in the left panel to browse its content.
   - Switch between **Rendered Preview** (how it looks formatted) and **Markdown Code** (raw markdown).
4. **Download**: Click "Download Markdown File" to get the single file, or click "Download All (ZIP)" to download all files at once.

### 中文
1. **上传文件**：点击上传区域，或者直接将要转换的文件（Word、Excel、PDF、音频等）拖入网页中。
2. **自动转换**：系统将自动在后台进行队列转换，并在网页上方显示处理进度。
3. **对照预览**：
   - 在左侧列表中选择您想查看的文件。
   - 切换 **“👁️ 渲染效果预览”**（排版后的富文本）和 **“💻 Markdown 源码”** 进行对比或一键复制。
4. **灵活下载**：
   - 点击 **“下载当前 Markdown 文件”** 单独保存。
   - 点击 **“📦 一键打包下载全部 (ZIP)”**，将所有转换成功的文件一次性打包下载。

---


## 📂 Supported Formats & Capabilities / 支持的转换类型

### English
The conversion engine is fully powered by Microsoft MarkItDown (v0.1.5). The supported formats include:
- **Documents**: 
  - `.docx` (Word): Extracts text, headings, lists, bold/italic formatting, and hyper-links.
  - `.pdf` (Portable Document): Extracts readable text layers and simple structured layout tables.
  - `.html`/`.htm` (Web page): Extracts clean article content, discarding sidebars and navigation panels.
  - `.txt`/`.md`: Direct markdown formatting optimization.
- **Spreadsheets**:
  - `.xlsx`/`.xls`/`.csv` (Excel): Intelligently reads sheet grids and formats them into clean markdown tables.
- **Presentations**:
  - `.pptx` (PowerPoint): Transcribes text content from slide text boxes slide-by-slide.
- **Structured Data**:
  - `.json`/`.xml`: Beautifies and outputs clean formatted structured layouts.
- **Audio Files**:
  - `.mp3`/`.wav`: Integrates standard speech-to-text API to automatically transcribe spoken words into structured Markdown notes.
- **Archives**:
  - `.zip`: Decompresses on the fly and recursively processes all supported files within.

### 中文
本项目完全采用微软官方 `Microsoft MarkItDown` 核心转换库。支持的解析能力包含：
- **文本与文档**：
  - **Word** (`.docx`)：完美转换段落文本，保留标题分级、列表、加粗/倾斜和超链接。
  - **PDF** (`.pdf`)：自动识别并提取其中的纯文本段落与简单的图表结构。
  - **网页** (`.html`/`.htm`)：智能剥离网页两侧的导航栏与广告栏，仅提取核心正文。
  - **文本文档** (`.txt`/`.md`)：纯文本自动清理。
- **电子表格 (Excel)**：
  - **Excel/CSV** (`.xlsx`/`.xls`/`.csv`)：自动识别合并单元格和行数据，将其规整排版为标准的 **Markdown 表格**。
- **演示文稿 (PPT)**：
  - **PowerPoint** (`.pptx`)：按幻灯片张数线性化排版其中的所有文本框与标题。
- **数据文件**：
  - **JSON/XML** (`.json`/`.xml`)：将其以结构化文本的排版美化输出。
- **音频转录**：
  - **语音音频** (`.mp3`/`.wav`)：内置语音识别网关，可自动将会议发言或录音听写转为 **Markdown 会议纪要**。
- **打包文件**：
  - **ZIP 压缩包** (`.zip`)：自动提取解压包内的所有匹配文件进行静默批量转换。

---

## ⚠️ Known Limitations / 使用限制说明

### English
- **Free Cloud Server Memory**: The app is hosted on Streamlit Community Cloud (with a **1GB RAM** quota). Avoid uploading extremely large files (e.g., >50MB PDFs or long movies) to prevent container crash and restart.
- **No OCR for Scanned Files**: In the default cloud environment, Microsoft MarkItDown is not configured with high-fidelity paid OCR engines (like Azure Document Intelligence). Therefore, scanned PDFs or image-only documents containing no text layer cannot be parsed. Please use native digital documents.
- **Audio Length**: The default speech recognition API has a time limit. It is recommended to upload audio clips under 5 minutes for stable transcription.
- **Layout Simplification**: Complex layouts (multi-column newsletters, custom drawings, nested groups, text boxes overlap) will be simplified to a linear, clean text flow.

### 中文
- **服务器内存限制**：由于本工具免费部署于 Streamlit 共享云端（每个容器配额仅 **1GB RAM**），请勿一次性上传过大文件（如超过 50MB 的 PDF 或长视频），否则容器可能会因为内存溢出而导致网页崩溃并自动重启。
- **纯图片/扫描件识别限制**：微软 `markitdown` 进行高精度 OCR 文字提取需要 Azure Document Intelligence 密钥或本地加载大型 OCR 库。在目前云端免费默认配置下，**无法对“纯图片”形式的扫描 PDF 或拍照截图提取出文字**。建议您使用原生电子导出的文档。
- **语音识别时长**：默认使用的免费语音识别 API 对音频长度有一定限制。为保证稳定性，建议上传 5 分钟以内的录音音频。
- **排版降维简化**：因为最终输出目标是 Markdown 纯文本，任何极其复杂的排版（如多栏排版、手绘图表、重叠文本框）都会被“拍扁”简化为线性的段落文字或表格。

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
