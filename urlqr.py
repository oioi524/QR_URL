import qrcode

img = qrcode.make("https://www.kyoto-wu.ac.jp")  # 文字列を与えてQRCodeを生成

img.save("kyotowu.png")  # ファイルに書き出す




import streamlit as st
import qrcode
import io

st.title("URLを QRCodeに 変換")

# 変換したら入力をクリア
with st.form(key="url-input", clear_on_submit=True):
    url = st.text_input("URL:")
    button = st.form_submit_button("変換")

if url:
    img = qrcode.make(url)

    # ファイルのように見せるオブジェクト BytesIO を開く
    with io.BytesIO() as f:
        img.save(f, format="PNG")  # BytesIO に書き出す
        png = f.getvalue()         # 実体を代入

    st.write(url)          # URLを表示
    st.image(png)          # 画像を表示
    st.download_button("Download", data=png, file_name="urlqr.png")
    # 画像をファイル名 "urlqr.png" としてダウンロードできるようにする
