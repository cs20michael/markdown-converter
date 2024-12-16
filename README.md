# Markdown 檔案轉換工具

這是一個使用 Streamlit 開發的網頁應用程式，可以將各種檔案格式轉換成 Markdown 格式。

## 功能特色

- 支援批量上傳檔案
- 即時預覽轉換結果
- 支援多種檔案格式（Excel、Word、PowerPoint、PDF）
- 可下載轉換後的 Markdown 檔案
- 美觀的使用者介面

## 本地安裝步驟
1. 建立virtualenv：
```bash
virtualenv llm
.\llm\Scripts\activate
```

2. 安裝相依套件：
```bash
pip install -r requirements.txt
```

3. 執行應用程式：
```bash
streamlit run app.py
```

## 部署到 Streamlit Cloud

1. Fork 這個專案到你的 GitHub
2. 登入 [Streamlit Cloud](https://streamlit.io/cloud)
3. 點擊 "New app"
4. 選擇你 fork 的專案和主分支
5. 點擊 "Deploy!"

## 使用方式

1. 開啟應用程式網址
2. 將檔案拖曳到上傳區域或點擊上傳按鈕選擇檔案
3. 等待檔案轉換完成
4. 預覽並下載轉換後的 Markdown 檔案

## 技術支援

- 使用 Microsoft MarkItDown 進行檔案轉換
- Streamlit 用於建立網頁介面
- 支援繁體中文介面
