import streamlit as st
from yuzu_config import *

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
    home_tab, inputs_tab = st.tabs(['Home','Inputs'])
    with home_tab:
        url_column, extract_button_column = st.columns([4,1])
        audio_checkbox_column, playlist_column = st.columns(2)
    with inputs_tab:
        video_format_column, video_resolution_column, frame_rate_column = st.columns(3)
        audio_format_column, audio_quality_column, sample_rate_column = st.columns(3)
        start_time_column, end_time_column, speed_column ,pitch_column = st.columns([1,1,2,2])

    url = url_column.text_input('URL',placeholder = 'Enter a valid video / audio URL',label_visibility='collapsed')
    extract_button = extract_button_column.button('Extract',use_container_width=True)
    audio_checkbox = True if audio_checkbox_column.checkbox('Audio only') else False
    playlist_checkbox = True if playlist_column.checkbox('Playlist') else False
    video_format = video_format_column.selectbox('Video Format',video_formats_list, disabled = audio_checkbox)
    video_resolution = video_resolution_column.selectbox('Resolution',video_resolution_list, disabled = audio_checkbox)
    frame_rate = frame_rate_column.number_input('Frame rate (fps)', min_frame_rate, max_frame_rate, display_frame_rate, disabled = audio_checkbox)
    audio_format = audio_format_column.selectbox('Audio format', audio_formats_list)
    audio_quality = audio_quality_column.number_input('Audio quality (kbps)', min_audio_quality, max_audio_quality, display_audio_quality)
    sample_rate = sample_rate_column.number_input('Sample Rate (Hz)', min_sample_rate, max_sample_rate, display_sample_rate)
    start_time = start_time_column.text_input('Start')
    end_time = end_time_column.text_input('End')
    speed = speed_column.number_input('Speed', min_speed, max_speed, display_speed)
    pitch = pitch_column.number_input('Pitch', min_pitch, max_pitch, display_pitch)

    inputs = {'url':url,'extract_button':extract_button,'audio_checkbox':audio_checkbox, 'playlist_checkbox':playlist_checkbox,
        'video_format':video_format, 'video_resolution':video_resolution, 'frame_rate':frame_rate, 'audio_format':audio_format,
        'audio_quality':audio_quality, 'sample_rate':sample_rate, 'start_time':start_time, 'end_time':end_time,
        'speed':speed, 'pitch':pitch}
    
    return inputs

if __name__ == '__main__':
    main() 