import streamlit as st
from markitdown import MarkItDown
import tempfile
import os

# 設置頁面配置
st.set_page_config(
    page_title="檔案轉換 Markdown 工具",
    page_icon="🔥",
    layout="wide"
)

# 自定義 CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .upload-box {
        border: 2px dashed #4CAF50;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
    }
    .success-msg {
        padding: 10px;
        border-radius: 5px;
        background-color: #E8F5E9;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 標題和說明
st.title("📝 檔案轉換 Markdown 工具")
st.markdown("### 輕鬆將您的檔案轉換成 Markdown 格式")
st.markdown("#### 參考 GitHub Repo: [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)")

# 初始化 MarkItDown
markitdown = MarkItDown()

# 檔案上傳區域
st.markdown("## 📤 上傳檔案")
st.markdown("支援的檔案格式：Excel, Word, PowerPoint, PDF 等")

uploaded_files = st.file_uploader(
    "拖曳檔案到此處或點擊上傳",
    accept_multiple_files=True,
    type=["xlsx", "xls", "doc", "docx", "ppt", "pptx", "pdf"]
)

if uploaded_files:
    st.markdown("### 🔄 轉換結果")
    
    for uploaded_file in uploaded_files:
        with st.expander(f"📄 {uploaded_file.name}", expanded=True):
            # 創建臨時文件
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name

            try:
                # 轉換文件
                result = markitdown.convert(tmp_file_path)
                
                # 顯示轉換結果
                st.markdown("**轉換成功！** ✨")
                
                # 顯示 Markdown 預覽
                st.markdown("##### Markdown 預覽")
                st.text_area(
                    "Markdown 內容",
                    result.text_content,
                    height=300,
                    key=f"markdown_{uploaded_file.name}"
                )
                
                # 下載按鈕
                st.download_button(
                    label="📥 下載 Markdown 檔案",
                    data=result.text_content,
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
                    mime="text/markdown",
                    key=f"download_{uploaded_file.name}"
                )
                
            except Exception as e:
                st.error(f"轉換 {uploaded_file.name} 時發生錯誤：{str(e)}")
                st.info("提示：請確保檔案格式正確且未損壞。如果問題持續存在，請嘗試其他檔案格式。")
            
            finally:
                # 清理臨時文件
                os.unlink(tmp_file_path)

else:
    # 顯示空狀態提示
    st.markdown("""
        <div class="upload-box">
            <h3>👆 請上傳您要轉換的檔案</h3>
            <p>支援批量上傳多個檔案</p>
        </div>
    """, unsafe_allow_html=True)

# 頁腳
st.markdown("---")
st.markdown("### 💡 使用說明")
st.markdown("""
- 支援批量上傳多個檔案
- 每個檔案都會自動轉換為 Markdown 格式
- 可以預覽轉換結果並下載
- 支援 Excel、Word、PowerPoint、PDF 等格式
""")
