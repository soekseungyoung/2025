import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="📘", layout="centered")

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

body, .main {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffe4ec 0%, #ffd0dd 100%);
    font-family: 'Nanum Gothic', sans-serif;
    color: #6a0d53;
}

/* 내부 컨테이너 배경 투명 */
[data-testid="stAppViewContainer"] > .main {
    background-color: transparent !important;
    position: relative;
    z-index: 0;
}

/* 제목 스타일 */
h1 {
    font-size: 3rem !important;
    text-align: center;
    margin-bottom: 0.5em;
    color: #7b2a5a;
    font-weight: 700;
}

/* 설명 텍스트 */
h2, p, label {
    color: #7b2a5a !important;
    font-size: 1.25rem !important;
    text-align: center;
    margin-bottom: 1em;
}

/* 입력창 스타일 */
.stTextInput>div>div>input {
    border: 2px solid #d57ea0;
    border-radius: 12px;
    padding: 10px 14px;
    font-size: 18px;
    color: #6a0d53;
    background-color: #fff0f4;
    box-shadow: 0 2px 5px rgba(213, 126, 160, 0.3);
    transition: border-color 0.3s ease;
    width: 100%;
    max-width: 380px;
    margin: 0 auto;
    display: block;
}

.stTextInput>div>div>input:focus {
    border-color: #b94c77;
    outline: none;
}

/* 버튼 스타일 */
.stButton > button {
    background: #d57ea0;
    color: #fff;
    font-weight: 600;
    border: none;
    border-radius: 25px;
    padding: 12px 40px;
    font-size: 18px;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(213, 126, 160, 0.5);
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    display: block;
    margin: 20px auto 0 auto;
    max-width: 240px;
    text-align: center;
}

.stButton > button:hover {
    background: #b94c77;
    box-shadow: 0 6px 12px rgba(185, 76, 119, 0.7);
}

/* 결과 텍스트 스타일 */
.stMarkdown {
    font-size: 1.3rem !important;
    color: #7b2a5a !important;
    text-align: center;
    margin-top: 25px;
    margin-bottom: 40px;
    font-weight: 600;
}

/* 하트 애니메이션 */
@keyframes floatUp {
  0% {
    transform: translateY(0) scale(1) rotate(-45deg);
    opacity: 0.8;
  }
  100% {
    transform: translateY(-180px) scale(1.5) rotate(-45deg);
    opacity: 0;
  }
}

.heart {
  position: fixed;
  width: 18px;
  height: 18px;
  background-color: #d57ea0;
  bottom: 0;
  filter: drop-shadow(0 0 4px #b94c77);
  animation-name: floatUp;
  animation-timing-function: ease-out;
  animation-iteration-count: infinite;
  opacity: 0.8;
  z-index: 15;
  transform: rotate(-45deg);
  border-radius: 3px 3px 0 0;
}

.heart::before,
.heart::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  background-color: #d57ea0;
  border-radius: 50%;
}

.heart::before {
  top: -9px;
  left: 0;
}

.heart::after {
  left: 9px;
  top: 0;
}

.heart:nth-child(1) {
  left: 12%;
  animation-duration: 5.5s;
  animation-delay: 0s;
}
.heart:nth-child(2) {
  left: 32%;
  animation-duration: 6.8s;
  animation-delay: 1.8s;
  width: 15px;
  height: 15px;
}
.heart:nth-child(3) {
  left: 58%;
  animation-duration: 7.4s;
  animation-delay: 2.9s;
  width: 22px;
  height: 22px;
}
.heart:nth-child(4) {
  left: 82%;
  animation-duration: 5.9s;
  animation-delay: 3.1s;
  width: 19px;
  height: 19px;
}
</style>

<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
"""

st.markdown(css, unsafe_allow_html=True)

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
