import streamlit as st
import yuzu_backend
import time

def main():
    st.set_page_config(page_title = 'Yuzu',page_icon = ':lemon:', menu_items = {'Get help':'https://github.com/mohit086/yuzu'})
    st.markdown('''
        <style>
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    ''', unsafe_allow_html=True)

    st.title('Yuzu')
    url_column, download_column = st.columns([4,1])

    url = url_column.text_input('URL',placeholder = 'Enter a valid video / audio URL',label_visibility='collapsed')
    download_button = download_column.button('Download',use_container_width=True)
    download_params = {'url':url, 'donwload_button':download_button}

    if download_button:
        with st.spinner("Downloading ..."):
            yuzu_backend.download_file(download_params)
        success_placeholder = st.empty()
        success_placeholder.success("Downloaded successfully")
        time.sleep(2)
        success_placeholder.empty()

if __name__ == '__main__':
    main()