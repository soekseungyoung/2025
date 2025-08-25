import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="📘", layout="centered")

pink_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Brush+Script&display=swap');

body, .main {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffe6f0 0%, #ffb3d9 100%);
    font-family: 'Nanum Brush Script', cursive;
    color: #800040;
}

/* 내부 컨테이너 배경 투명 */
[data-testid="stAppViewContainer"] > .main {
    background-color: transparent !important;
    position: relative;
    z-index: 0;
}

/* 제목 스타일 */
h1 {
    font-size: 3.5rem !important;
    text-align: center;
    margin-bottom: 0.3em;
    color: #9b0068;
    text-shadow: 1px 1px 5px #ffb6c1;
}

/* 설명 텍스트 */
h2, p, label {
    color: #a3006a !important;
    font-size: 1.4rem !important;
    text-align: center;
    margin-bottom: 1.2em;
}

/* 입력창 스타일 */
.stTextInput>div>div>input {
    border: 3px solid #ff77b7;
    border-radius: 15px;
    padding: 12px 15px;
    font-size: 20px;
    color: #800040;
    background-color: #fff0f6;
    box-shadow: 0 4px 8px rgba(255, 105, 180, 0.3);
    transition: border-color 0.3s ease;
    width: 100%;
    max-width: 400px;
    margin: 0 auto;
    display: block;
}

.stTextInput>div>div>input:focus {
    border-color: #ff1493;
    outline: none;
}

/* 버튼 스타일 */
.stButton > button {
    background: linear-gradient(135deg, #ff69b4 0%, #ff1493 100%);
    color: #fff;
    font-weight: 700;
    border: none;
    border-radius: 30px;
    padding: 15px 50px;
    font-size: 22px;
    cursor: pointer;
    box-shadow: 0 6px 12px rgba(255, 20, 147, 0.6);
    transition: all 0.4s ease;
    display: block;
    margin: 20px auto 0 auto;
    max-width: 300px;
    text-align: center;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ff1493 0%, #ff69b4 100%);
    box-shadow: 0 8px 20px rgba(255, 20, 147, 0.8);
    transform: scale(1.05);
}

/* 결과 텍스트 스타일 */
.streamlit-expanderHeader, .stMarkdown {
    font-size: 1.5rem !important;
    color: #a3006a !important;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 30px;
    font-weight: 600;
    text-shadow: 1px 1px 3px #ffb6c1;
}

/* 하트 애니메이션 */
@keyframes floatUp {
  0% {
    transform: translateY(0) scale(1) rotate(-45deg);
    opacity: 1;
  }
  100% {
    transform: translateY(-300px) scale(2) rotate(-45deg);
    opacity: 0;
  }
}

.heart {
  position: fixed;
  width: 24px;
  height: 24px;
  background-color: #ff4da6;
  bottom: 0;
  filter: drop-shadow(0 0 6px #ff66b2);
  animation-name: floatUp;
  animation-timing-function: ease-out;
  animation-iteration-count: infinite;
  opacity: 0.9;
  z-index: 15;
  transform: rotate(-45deg);
  border-radius: 4px 4px 0 0;
}

.heart::before,
.heart::after {
  content: "";
  position: absolute;
  width: 24px;
  height: 24px;
  background-color: #ff4da6;
  border-radius: 50%;
}

.heart::before {
  top: -12px;
  left: 0;
}

.heart::after {
  left: 12px;
  top: 0;
}

.heart:nth-child(1) {
  left: 10%;
  animation-duration: 5s;
  animation-delay: 0s;
}
.heart:nth-child(2) {
  left: 30%;
  animation-duration: 6.5s;
  animation-delay: 1.5s;
  width: 20px;
  height: 20px;
}
.heart:nth-child(3) {
  left: 55%;
  animation-duration: 7.5s;
  animation-delay: 2.5s;
  width: 28px;
  height: 28px;
}
.heart:nth-child(4) {
  left: 80%;
  animation-duration: 5.5s;
  animation-delay: 2.8s;
  width: 22px;
  height: 22px;
}
</style>

<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
"""

st.markdown(pink_css, unsafe_allow_html=True)

st.title("📘 내가 웹툰 속에 들어간다면?")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다!")

name = st.text_input("당신의 이름을 입력하세요:")

def generate_character(name):
    height = random.randint(150, 190)
    roles = [
        "다정한 공", "차가운 공", "능글맞은 공", "츤데레 공",
        "순진한 수", "새침한 수", "털털한 수", "상처 많은 수"
    ]
    role = random.choice(roles)

    appearances = [
        "짧은 흑발에 강한 인상", "긴 생머리에 차가운 눈매", "은은한 미소를 가진 얼굴",
        "눈이 크고 인형 같은 외모", "스포티한 스타일에 건강미 넘침",
        "항상 후드를 쓰고 다니는 미스터리한 모습"
    ]
    appearance = random.choice(appearances)

    personalities = [
        "겉은 차가워 보이지만 속은 따뜻한 스타일",
        "모든 사람에게 친절한 인싸",
        "혼자 있는 걸 좋아하는 무뚝뚝한 타입",
        "정의감 넘치고 다혈질",
        "감성적이고 눈물이 많은 성격",
        "장난기 많고 유쾌한 분위기 메이커"
    ]
    personality = random.choice(personalities)

    return (f"{name}님의 웹툰 캐릭터는 키 {height}cm에 '{role}' 포지션이며, "
            f"외형은 {appearance}, 성격은 {personality}입니다.")

if name:
    st.markdown(f"### {generate_character(name)}")

    if st.button("다시 하기"):
        st.experimental_rerun()
