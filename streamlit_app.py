# -*- coding: utf-8 -*-
import streamlit as st
import os
import tempfile
import zipfile
import io
from markitdown import MarkItDown

# 设置页面配置 (必须是 Streamlit 命令中的第一个)
st.set_page_config(
    page_title="Markdown 文档转换工具",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义 CSS 样式，提升视觉体验（遵循 Rich Aesthetics 规范）
st.markdown("""
<style>
    /* 引入 Outfit 字体 */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    /* 全局字体与背景渐变 */
    html, body, [class*="css"] {
        font-family: 'Outfit', 'PingFang SC', 'Microsoft YaHei', sans-serif;
    }
    
    /* 渐变标题 */
    .hero-title {
        background: linear-gradient(135deg, #FF4B4B, #8F3BFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0.1rem;
    }
    
    .hero-subtitle {
        color: #555555;
        font-size: 1.15rem;
        font-weight: 400;
        margin-bottom: 1.5rem;
    }
    
    /* 按钮与卡片样式 */
    .stButton > button {
        background: linear-gradient(135deg, #FF4B4B, #FF7575);
        color: white;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.4);
        background: linear-gradient(135deg, #E03E3E, #FF5E5E);
    }
    
    /* 卡片容器 */
    .file-card {
        background-color: #ffffff;
        border: 1px solid #e1e4e8;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        transition: transform 0.2s ease;
    }
    .file-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.06);
    }
    
    /* 侧边栏样式定制 */
    .css-1639ggc {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏设计
with st.sidebar:
    st.markdown("### 📄 关于转换核心")
    st.markdown("""
    本网页工具**完全基于微软官方开源的 `Microsoft MarkItDown` (v0.1.5) 核心库**构建，其后台转换逻辑与命令行工具完全一致。
    """)
    st.divider()

    st.markdown("### 📂 支持的转换格式")
    st.markdown("""
    - **文档类**
      - **Word** (`.docx`): 转换为标准 Markdown，保留标题层级、粗体、列表、超链接等基本样式。
      - **PDF** (`.pdf`): 提取其中的段落文本与表格结构。
      - **网页** (`.html`/`.htm`): 自动清理多余的 HTML 标签，保留干净的正文。
      - **文本** (`.txt`/`.md`): 原文处理与优化。
    - **电子表格**
      - **Excel/CSV** (`.xlsx`/`.xls`/`.csv`): 自动将工作表的数据和边框排版转换成整齐的 **Markdown 表格**。
    - **演示幻灯**
      - **PowerPoint** (`.pptx`): 将每一页 Slide 的文本框内容线性化转换为 Markdown 文本。
    - **半结构化数据**
      - **JSON/XML** (`.json`/`.xml`): 保持数据格式并进行排版优化。
    - **音频文件**
      - **语音音频** (`.mp3`/`.wav`): 自动通过语音识别接口提取对话文本，并输出为 Markdown 记录。
    """)
    st.divider()

    st.markdown("### ⚠️ 转换限制与说明")
    st.markdown("""
    由于本工具免费部署于 Streamlit Community Cloud 云端，使用时请注意以下限制：
    
    1. **文件大小与内存限制**
       - 免费服务器内存仅为 **1GB RAM**。请避免一次性上传超大文件（如大于 50MB 的超大 PDF 或长视频/音频），否则可能会导致服务器内存溢出而导致网页短暂重启。
    2. **纯图片与扫描件识别限制**
       - 微软 `markitdown` 针对拍照图片或纯扫描版 PDF 的高保真文字识别（OCR）需要额外的 API 授权（如 Azure 智能文档服务）。在云端默认运行下，**无法对没有文本层（纯图片）的文档进行完美的 OCR 识别**，请尽量使用原生电子版文档。
    3. **音频识别说明**
       - 语音转文字默认使用标准的免费语音识别网关，建议音频时长控制在几分钟内，且尽量使用标准普通话/英语。
    4. **复杂排版简化**
       - 转换的最终目标是 Markdown 纯文本，因此文档中极其复杂的排版样式（如多栏排版、手绘图形、复杂的图表混合等）将被简化为线性的纯文本或表格。
    """)
    st.divider()
    
    st.markdown("### 💡 使用提示")
    st.markdown("""
    1. 在上方框中点击或拖拽一个或多个文件。
    2. 等待顶部进度条加载完成。
    3. 在右侧“文件列表”中选择对应文件进行预览，或者一键点击 **"📦 一键打包下载全部 (ZIP)"**。
    """)
    st.divider()
    st.markdown("<p style='text-align: center; color: #888;'>Powered by Microsoft MarkItDown & Streamlit</p>", unsafe_allow_html=True)



# 主页面 Hero 区
st.markdown('<h1 class="hero-title">Markdown 文档转换工具</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">基于开源 Microsoft MarkItDown 技术，支持一键上传并批量转换 PDF, Word, Excel, PPT 等文件为 Markdown 文档。</p>', unsafe_allow_html=True)

# 文件上传组件
uploaded_files = st.file_uploader(
    "请选择要转换的文件（支持多选）",
    type=["pdf", "docx", "xlsx", "xls", "pptx", "html", "htm", "txt", "csv", "json", "xml", "md", "mp3", "wav"],
    accept_multiple_files=True,
    help="您可以拖拽或点击选择一个或多个不同格式的文件"
)

# 转换状态容器
if uploaded_files:
    st.subheader("🔄 转换任务与结果")
    
    results = {}
    errors = {}
    
    # 初始化 MarkItDown 实例
    md = MarkItDown()
    
    # 状态条
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # 批量处理
    for idx, uploaded_file in enumerate(uploaded_files):
        filename = uploaded_file.name
        status_text.markdown(f"正在转换第 **{idx+1}/{len(uploaded_files)}** 个文件: `{filename}`...")
        
        # 获取文件后缀名
        _, file_extension = os.path.splitext(filename)
        
        try:
            # 将上传的文件写入临时文件以供 MarkItDown 读取
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
                temp_file.write(uploaded_file.getvalue())
                temp_path = temp_file.name
            
            # 调用转换
            result = md.convert(temp_path)
            results[filename] = result.markdown
            
            # 删除临时文件
            os.unlink(temp_path)
            
        except Exception as e:
            errors[filename] = str(e)
            if os.path.exists(temp_path):
                os.unlink(temp_path)
        
        # 更新进度
        progress_bar.progress((idx + 1) / len(uploaded_files))
    
    # 完成提示
    status_text.success(f"🎉 转换完成！成功 {len(results)} 个，失败 {len(errors)} 个。")
    
    # 失败列表展示
    if errors:
        with st.expander("⚠️ 部分文件转换失败", expanded=True):
            for fname, err in errors.items():
                st.error(f"**{fname}** : {err}")
                
    # 如果有成功转换的文件，提供下载和预览
    if results:
        # 分栏展示：左侧为列表选择，右侧为预览和下载
        col_list, col_preview = st.columns([1, 2], gap="large")
        
        with col_list:
            st.markdown("#### 📂 转换后的文件列表")
            
            # 批量下载打包为 ZIP
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                for fname, md_content in results.items():
                    base_name, _ = os.path.splitext(fname)
                    zip_file.writestr(f"{base_name}.md", md_content.encode("utf-8"))
            
            st.download_button(
                label="📦 一键打包下载全部 (ZIP)",
                data=zip_buffer.getvalue(),
                file_name="converted_markdowns.zip",
                mime="application/zip",
                use_container_width=True
            )
            st.divider()
            
            # 单选框，选择查看哪一个文件的转换结果
            selected_file = st.radio(
                "选择文件进行预览/单独下载：",
                options=list(results.keys()),
                format_func=lambda x: f"📄 {x}"
            )
            
        with col_preview:
            if selected_file:
                md_content = results[selected_file]
                base_name, _ = os.path.splitext(selected_file)
                md_filename = f"{base_name}.md"
                
                # 文件预览标题和单独下载按钮
                st.markdown(f"#### 📄 正在浏览: `{selected_file}`")
                
                col_btn, _ = st.columns([2, 2])
                with col_btn:
                    st.download_button(
                        label=f"⬇️ 下载当前 Markdown 文件",
                        data=md_content,
                        file_name=md_filename,
                        mime="text/markdown",
                        use_container_width=True
                    )
                
                # 预览内容 tabs 切换
                tab_rendered, tab_code = st.tabs(["👁️ 渲染效果预览", "💻 Markdown 源码"])
                
                with tab_rendered:
                    st.markdown(md_content)
                    
                with tab_code:
                    st.code(md_content, language="markdown")
else:
    # 初始状态下的说明与效果示例卡片
    st.info("💡 请在上方上传您想要转换的文件。支持 PDF、Word、PPT、Excel、图片等多种常见格式。")
    
    st.subheader("💡 转换效果示例")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **📥 输入示例 (Excel / PDF / Word):**
        ```text
        年度销售数据表
        月份    销售额(元)  利润率
        1月     12,000      15%
        2月     15,400      18%
        3月     18,900      20%
        ```
        """)
    with col2:
        st.markdown("""
        **📤 转换输出 (Markdown格式):**
        ```markdown
        ### 年度销售数据表
        
        | 月份 | 销售额(元) | 利润率 |
        | --- | --- | --- |
        | 1月 | 12,000 | 15% |
        | 2月 | 15,400 | 18% |
        | 3月 | 18,900 | 20% |
        ```
        """)
