import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="📘", layout="centered")

pink_css = """
<style>
/* 배경색을 진한 연핑크로 */
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(135deg, #ffc1e3 0%, #ffb6c1 100%);
    position: relative;
    z-index: 0;
    color: #800040;  /* 진한 핑크 텍스트 */
    font-family: 'Nanum Gothic', sans-serif;
}

/* 제목과 텍스트 색상 */
h1, h2, h3, p, label {
    color: #800040 !important;
}

/* 입력창 꾸미기 */
.stTextInput>div>div>input {
    border: 2px solid #ff69b4;
    border-radius: 10px;
    padding: 8px;
    font-size: 18px;
    color: #800040;
    background-color: #ffe4f1;
}

/* 버튼 꾸미기 */
.stButton > button {
    background: linear-gradient(45deg, #ff69b4, #ff1493);
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 15px;
    padding: 10px 30px;
    font-size: 18px;
    cursor: pointer;
    transition: background 0.3s ease;
}
.stButton > button:hover {
    background: linear-gradient(45deg, #ff1493, #ff69b4);
}

/* 하트 애니메이션 */
@keyframes floatUp {
  0% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translateY(-250px) scale(1.8);
    opacity: 0;
  }
}

.heart {
  position: fixed;
  width: 22px;
  height: 22px;
  background-color: #ff3399;
  transform: rotate(-45deg);
  bottom: 0;
  animation-name: floatUp;
  animation-timing-function: ease-out;
  animation-iteration-count: infinite;
  opacity: 0.9;
  z-index: 10;
  filter: drop-shadow(0 0 4px #ff66b2);
}

.heart::before,
.heart::after {
  content: "";
  position: absolute;
  width: 22px;
  height: 22px;
  background-color: #ff3399;
  border-radius: 50%;
}

.heart::before {
  top: -11px;
  left: 0;
}

.heart::after {
  left: 11px;
  top: 0;
}

/* 각 하트 위치와 속도 조절 */
.heart:nth-child(1) {
  left: 15%;
  animation-duration: 5s;
  animation-delay: 0s;
}
.heart:nth-child(2) {
  left: 35%;
  animation-duration: 6s;
  animation-delay: 1.7s;
  width: 18px;
  height: 18px;
}
.heart:nth-child(3) {
  left: 60%;
  animation-duration: 7s;
  animation-delay: 3.2s;
  width: 28px;
  height: 28px;
}
.heart:nth-child(4) {
  left: 85%;
  animation-duration: 5.5s;
  animation-delay: 2.3s;
  width: 20px;
  height: 20px;
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
    st.write(generate_character(name))

    if st.button("다시 하기"):
        st.experimental_rerun()
