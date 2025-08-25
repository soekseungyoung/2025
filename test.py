import streamlit as st
import random
import base64

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="📘", layout="centered")

st.title("📘 내가 웹툰 속에 들어간다면?")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다!")

# 아까 올려준 이미지 경로(환경에 맞게 변경)
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img1 = get_base64("/mnt/data/43d95ac7-f428-47d5-b91f-cbd4f39c889c.png")
img2 = get_base64("/mnt/data/cbc22f0b-7324-4ffa-93a6-b79adc4ae1a5.png")
img3 = get_base64("/mnt/data/96c7810b-8338-4063-ba21-899e5bcd32ab.png")
img4 = get_base64("/mnt/data/ff3f1811-f4e1-419e-b905-df876e236b89.png")

# 배경 스타일 (연한 핑크 + 이미지 4장 + 하트 애니메이션)
page_bg = f"""
<style>
@keyframes floatUp {{
  0% {{
    transform: translateY(0) scale(1);
    opacity: 1;
  }}
  100% {{
    transform: translateY(-200px) scale(1.5);
    opacity: 0;
  }}
}}

[data-testid="stAppViewContainer"] > .main {{
    background-color: #ffd1dc; /* 연한 핑크 */
    background-image:
        url("data:image/png;base64,{img1}"),
        url("data:image/png;base64,{img2}"),
        url("data:image/png;base64,{img3}"),
        url("data:image/png;base64,{img4}");
    background-repeat: no-repeat, no-repeat, no-repeat, no-repeat;
    background-position: left top, right top, left bottom, right bottom;
    background-size: 150px 200px, 150px 200px, 150px 200px, 150px 200px;
    opacity: 0.2;
    position: relative;
    z-index: 0;
}}

/* 하트 컨테이너 */
.heart {{
  position: fixed;
  width: 20px;
  height: 20px;
  background-color: #ff6b81;
  transform: rotate(-45deg);
  left: 50%;
  bottom: 0;
  animation-name: floatUp;
  animation-timing-function: ease-out;
  animation-iteration-count: infinite;
  opacity: 0.8;
  z-index: 10;
}}

/* 하트 모양 만들기 */
.heart::before,
.heart::after {{
  content: "";
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: #ff6b81;
  border-radius: 50%;
}}

.heart::before {{
  top: -10px;
  left: 0;
}}

.heart::after {{
  left: 10px;
  top: 0;
}}

/* 여러 개 하트 위치와 애니메이션 딜레이 달리기 */
.heart:nth-child(1) {{
  left: 20%;
  animation-duration: 4s;
  animation-delay: 0s;
}}
.heart:nth-child(2) {{
  left: 40%;
  animation-duration: 5s;
  animation-delay: 1.5s;
  width: 15px;
  height: 15px;
}}
.heart:nth-child(3) {{
  left: 60%;
  animation-duration: 6s;
  animation-delay: 3s;
  width: 25px;
  height: 25px;
}}
.heart:nth-child(4) {{
  left: 80%;
  animation-duration: 4.5s;
  animation-delay: 2s;
  width: 18px;
  height: 18px;
}}

</style>

<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
"""

st.markdown(page_bg, unsafe_allow_html=True)

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
