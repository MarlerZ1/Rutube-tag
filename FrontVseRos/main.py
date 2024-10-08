import json

import requests
import streamlit as st
import base64
import os
from dotenv import load_dotenv
load_dotenv()

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {  
    background-image: url("https://sun9-13.userapi.com/impg/Yp2wYB2uWR8oMi3bjLUyoQMyenIq7G2pDA9Qsw/LAYhT_K3z9A.jpg?size=2560x1402&quality=96&sign=4d19a05796bc4b2b7ac2035839d4926a&type=album");     
    background-size: cover;
}
[data-testid="stHeader"]{                    
    background-color: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"]{                    
    background-color: black;
}

[data-testid="stWidgetLabel"] {
    color: rgb(253,255,254);
    font: Optima, sans-serif;
}

[class="st-emotion-cache-19rxjzo ef3psqc12"] {
    color: rgb(253,255,254);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

gradient_text_html = """
<style>
.gradient-text {
    background-color: rgb(253,255,254);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 60px;
    font-family: Optima, sans-serif;
    font-weight: bold;
    padding: 10px;
    text-align: center;
    letter-spacing: 4px;
}
</style>

<div class="gradient-text">Тэги для видео</div>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)

def extract_video(uploaded_video):
    video_content = uploaded_video.read()
    encoded_video_content = base64.b64encode(video_content).decode('utf-8')
    return encoded_video_content

video_title = st.text_input('Введите название видео')
video_description = st.text_area('Введите описание видео', height=100)
uploaded_video = st.file_uploader('Перетащите видео файл', type=["mp4", "avi", "mov"])

if uploaded_video is not None and st.button("Загрузить видео"):
    encoded_video_content = extract_video(uploaded_video)
    
    data_to_send = {
        "video_title": video_title,
        "video_description": video_description,
        "video_content": encoded_video_content
    }

    # response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)

    st.video(uploaded_video)
    st.write(f"Название видео: {video_title}")
    st.write(f"Описание видео: {video_description}")
    address = f'http://{os.getenv("IP")}:{os.getenv("PORT")}/ai/get_analysis'
    print(address)

    get_response = requests.get(address, json=data_to_send)
    if get_response.status_code == 200:
        json_data = get_response.json()
        # st.json(json_data)
        st.write(f"\nСписок тегов с вероятностями:")
        for tag, prob in json_data.items():
            st.write(f"• {tag}: {prob}")
    else:
        st.error(f"Не удалось получить данные. Статус: {get_response.status_code}")
