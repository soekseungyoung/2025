import streamlit as st
import random

st.set_page_config(page_title="내가 축구 웹툰 속에 들어간다면?", page_icon="🩷", layout="centered")

# -------------------- CSS --------------------
css = """
<style>
.stApp {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ff69b4);
    font-family: 'Nanum Gothic', sans-serif;
    color: #6a0d53;
}
.stButton>button {
    background: #ff69b4;
    color: white;
    border-radius: 25px;
    padding: 12px 40px;
    font-size: 18px;
}
.stButton>button:hover {
    background: #ff1493;
}
.result-box {
    background: #fff0f4;
    border: 2px solid #ff69b4;
    border-radius: 20px;
    padding: 20px;
    margin: 30px auto;
    max-width: 500px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 600;
    color: #7b2a5a;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- UI --------------------
st.title("🩷내가 축구 웹툰 속에 들어간다면?🩷")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다! ⚽️")

name = st.text_input("당신의 이름을 입력하세요:")

# -------------------- 캐릭터 생성 함수 --------------------
def generate_character():
    height = random.randint(150, 190)
    roles = ["⚽ 다정한 공", "❄ 차가운 공", "😏 능글맞은 공", "🙈 츤데레 공",
             "🌸 순진한 수", "🐰 새침한 수", "🍀 털털한 수", "🌑 상처 많은 수"]
    appearances = ["짧은 흑발에 강한 인상", "긴 생머리에 차가운 눈매", "은은한 미소를 가진 얼굴",
                   "눈이 크고 인형 같은 외모", "스포티한 스타일에 건강미 넘침",
                   "항상 후드를 쓰고 다니는 미스터리한 모습"]
    personalities = ["겉은 차가워 보이지만 속은 따뜻한 스타일 💖",
                     "모든 사람에게 친절한 인싸 ✨",
                     "혼자 있는 걸 좋아하는 무뚝뚝한 타입 😶",
                     "정의감 넘치고 다혈질 🔥",
                     "감성적이고 눈물이 많은 성격 😢"]

    role = random.choice(roles)
    appearance = random.choice(appearances)
    personality = random.choice(personalities)

    return f"<div class='result-box'>{name}님의 웹툰 캐릭터는<br>📏 키 <b>{height}cm</b><br>포지션: <b>{role}</b><br>외형: <b>{appearance}</b><br>성격: <b>{personality}</b></div>"

# -------------------- 결과 출력 --------------------
if name:
    if st.button("✨ 캐릭터 생성!"):
        # 결과 출력
        st.markdown(generate_character(), unsafe_allow_html=True)

        # 결과 나오면 소리 재생
        st.markdown(
            """
            <audio autoplay>
                <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
            </audio>
            """, unsafe_allow_html=True
        )
