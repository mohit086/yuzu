import streamlit as st
import yuzu_backend

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
    url_column, extract_column = st.columns([4,1])
    audio_only_column, playlist_column = st.columns(2)

    url = url_column.text_input('URL',placeholder = 'Enter a valid video / audio URL',label_visibility='collapsed')
    extract_button = extract_column.button('Extract',use_container_width=True)
    audio_only = audio_only_column.checkbox('Audio only')
    playlist = playlist_column.checkbox('Playlist')
    download_params = {'url':url, 'extract_button':extract_button, 'audio_only':audio_only}

    if extract_button:
        with st.spinner("Extracting ..."):
            extracted_file, filename = yuzu_backend.extract_file(download_params)
        with open(extracted_file, "rb") as f:
            st.download_button(label="Download", data = f, file_name = filename)
        
if __name__ == '__main__':
    main()