import streamlit as st
import yuzu_frontend, yuzu_parser, yuzu_extractor

def main():
    inputs = yuzu_frontend.main()
    params = yuzu_parser.parse(inputs)
    if inputs['extract_button'] and inputs['url'] != '':
        with st.spinner("Extracting ..."):
            extracted_file, filename = yuzu_extractor.extract_file(params)
        with open(extracted_file, "rb") as f:
            st.download_button(label="Download", data = f, file_name = filename)

if __name__ == '__main__':
    main()