import streamlit as st
import time

# Streamlit アプリのタイトル
st.title("ニセ授業動画作成システム")

# PDFファイルのアップロード
uploaded_pdf = st.file_uploader("PDFファイルをアップロードしてください", type=["pdf"])

if uploaded_pdf:
  st.success("PDFを読み込みました")
  time.sleep(3)
  
  text = """
  授業内容を生成してここに表示する！
  生成完了後、手動で編集も可能
  """
  st.text_area("授業内容(1ページ目)", text, height=300)

  # 編集後の全テキストを表示
  if st.button("動画作成開始"):
    st.subheader("最終結果")
    progress_bar = st.progress(0)  # プログレスバーの初期値
    time.sleep(1)
    progress_bar.progress(50)  # プログレスバーを更新
    time.sleep(1)
    progress_bar.progress(100)  # プログレスバーを更新
    st.write("※ここに完成した動画を表示する")
    