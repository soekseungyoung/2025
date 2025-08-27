import streamlit as st
import random

st.set_page_config(page_title="웹툰 속 운명", page_icon="💀", layout="centered")

# ----------------- 데이터 -----------------
roles = ["빛과 어둠의 경계에 선 주인공", "세계를 집어삼키는 악의 화신", "몰락한 영웅", "저주받은 방랑자", "끝없는 전쟁의 군주"]
personalities = ["냉혹한 카리스마", "광기에 잠식된 자", "어둠을 속삭이는 자", "불멸을 갈망하는 자", "고독 속에서 깨어난 자"]
items = ["지옥의 낫", "저주받은 서책", "붉은 달의 반지", "망자의 검", "심연의 화관"]
fates = [
    "세상과 함께 불타 사라졌다.",
    "끝내 괴물로 변해버렸다.",
    "전설로 남았지만, 두려움의 상징이었다.",
    "모든 이를 배신하고 고독 속에 사라졌다.",
    "마지막 웃음과 함께 피의 비를 내렸다.",
    "영원히 기억 속에서 저주받은 이름이 되었다.",
    "끝내 왕좌에 앉았으나, 공허만이 남았다.",
    "모든 것을 삼키고 스스로를 파괴했다."
]

# ----------------- UI -----------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #000000, #1a001a, #330000);
        color: white;
        font-family: 'Cinzel', serif;
    }
    .title {
        font-size: 40px;
        text-align: center;
        color: #ff0000;
        text-shadow: 0 0 30px red, 0 0 60px black;
        margin-bottom: 30px;
    }
    .result-box {
        background: black;
        border: 3px solid red;
        padding: 20px;
        text-align: center;
        font-size: 20px;
        text-shadow: 0 0 20px red, 0 0 40px black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>💀 내가 웹툰 속에 들어간다면 💀</div>", unsafe_allow_html=True)

name = st.text_input("이름을 입력하세요:")

# ----------------- 결과 -----------------
if st.button("운명 확인하기"):
    if not name.strip():
        st.warning("이름을 입력해주세요!")
    else:
        role = random.choice(roles)
        personality = random.choice(personalities)
        item = random.choice(items)
        fate = random.choice(fates)

        # --- 웅장한 음악 재생 ---
        st.audio("https://cdn.pixabay.com/download/audio/2022/03/15/audio_57c9f6e5bb.mp3?filename=dark-epic-trailer-109278.mp3")

        result_html = f"""
        <div class="result-box">
        ☠️ <b>{name}</b> 님의 운명 ☠️<br><br>
        🎭 역할: <b>{role}</b><br>
        🩸 성격: <b>{personality}</b><br>
        🔮 아이템: <b>{item}</b><br>
        ⚰️ 최후: <b>{fate}</b>
        </div>
        """
        st.markdown(result_html, unsafe_allow_html=True)
