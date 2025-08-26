import streamlit as st
import random

st.set_page_config(page_title="내가 축구 웹툰 속에 들어간다면?", page_icon="🩷", layout="centered")

# -------------------- CSS --------------------
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

.stApp {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ff69b4);
    font-family: 'Nanum Gothic', sans-serif;
    color: #6a0d53;
}
[data-testid="stAppViewContainer"] > .main {
    background-color: transparent !important;
    position: relative;
    z-index: 0;
}
h1 {
    font-size: 3rem !important;
    text-align: center;
    margin-bottom: 0.5em;
    color: #7b2a5a;
    font-weight: 700;
}
h2, p, label {
    color: #7b2a5a !important;
    font-size: 1.25rem !important;
    text-align: center;
    margin-bottom: 1em;
}
.stTextInput>div>div>input {
    border: 2px solid #ff69b4;
    border-radius: 12px;
    padding: 10px 14px;
    font-size: 18px;
    color: #6a0d53;
    background-color: #fff0f4;
    box-shadow: 0 2px 5px rgba(255, 105, 180, 0.4);
    transition: border-color 0.3s ease;
    width: 100%;
    max-width: 380px;
    margin: 0 auto;
    display: block;
}
.stTextInput>div>div>input:focus {
    border-color: #ff1493;
    outline: none;
}
.stButton > button {
    background: #ff69b4;
    color: #fff;
    font-weight: 600;
    border: none;
    border-radius: 25px;
    padding: 12px 40px;
    font-size: 18px;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(255, 105, 180, 0.5);
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    display: block;
    margin: 20px auto 0 auto;
    max-width: 240px;
    text-align: center;
}
.stButton > button:hover {
    background: #ff1493;
    box-shadow: 0 6px 12px rgba(255, 20, 147, 0.6);
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
    box-shadow: 0 6px 12px rgba(255, 105, 180, 0.4);
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- UI --------------------
st.title("🩷내가 축구 웹툰 속에 들어간다면?🩷")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다! ⚽️")

name = st.text_input("당신의 이름을 입력하세요:")

# -------------------- 캐릭터 생성 함수 --------------------
def generate_character(name):
    height = random.randint(150, 190)
    roles = [
        "⚽ 다정한 공", "❄ 차가운 공", "😏 능글맞은 공", "🙈 츤데레 공",
        "🌸 순진한 수", "🐰 새침한 수", "🍀 털털한 수", "🌑 상처 많은 수"
    ]
    appearances = [
        "짧은 흑발에 강한 인상", "긴 생머리에 차가운 눈매", "은은한 미소를 가진 얼굴",
        "눈이 크고 인형 같은 외모", "스포티한 스타일에 건강미 넘침",
        "항상 후드를 쓰고 다니는 미스터리한 모습", "붉은 염색머리에 개성 넘치는 분위기",
        "단정한 안경과 깔끔한 헤어스타일", "부드러운 갈색 머리에 따뜻한 인상",
        "피어싱이 돋보이는 스트릿 패션", "백발에 신비로운 오라를 풍김",
        "햇살 같은 금발과 밝은 미소", "잘 다져진 근육질 몸매와 자신감 넘치는 포즈",
        "차분한 흑단 머리에 서늘한 눈빛", "웃을 때 보조개가 매력적인 얼굴"
    ]
    personalities = [
        "겉은 차가워 보이지만 속은 따뜻한 스타일 💖",
        "모든 사람에게 친절한 인싸 ✨",
        "혼자 있는 걸 좋아하는 무뚝뚝한 타입 😶",
        "정의감 넘치고 다혈질 🔥",
        "감성적이고 눈물이 많은 성격 😢",
        "장난기 많고 유쾌한 분위기 메이커 😆",
        "책임감이 강하고 팀을 이끄는 리더십 💪",
        "귀찮음을 많이 타지만 할 건 하는 성격 😴",
        "배려심 많고 남을 잘 챙기는 스타일 🤗",
        "예술적 감각이 뛰어난 감성파 🎨",
        "허당끼가 있는 귀여운 성격 🐣",
        "자신감 넘치고 항상 도전하는 타입 🚀"
    ]
    role = random.choice(roles)
    appearance = random.choice(appearances)
    personality = random.choice(personalities)

    return (f"<div class='result-box'>"
            f"{name}님의 웹툰 캐릭터는<br><br>"
            f"📏 키 <b>{height}cm</b>, <br>"
            f"포지션은 <b>{role}</b><br><br>"
            f"외형은 <b>{appearance}</b>,<br>"
            f"성격은 <b>{personality}</b>입니다!"
            f"</div>")

# -------------------- 결과 출력 --------------------
if name:
    st.markdown(generate_character(name), unsafe_allow_html=True)

    # ✅ 결과가 나오면 소리 자동 재생
    st.markdown(
        """
        <audio autoplay>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

    if st.button("🔄 다시 하기"):
        st.rerun()
