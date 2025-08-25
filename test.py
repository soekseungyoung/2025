import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="📘", layout="centered")

# 배경 연한 핑크색 + 하트 애니메이션 CSS
page_bg_css = """
<style>
/* 배경 연한 핑크색 */
[data-testid="stAppViewContainer"] > .main {
    background-color: #ffd1dc;  /* 연한 핑크 */
    position: relative;
    z-index: 0;
}

/* 하트 애니메이션 정의 */
@keyframes floatUp {
  0% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translateY(-200px) scale(1.5);
    opacity: 0;
  }
}

/* 하트 모양 */
.heart {
  position: fixed;
  width: 20px;
  height: 20px;
  background-color: #ff6b81;
  transform: rotate(-45deg);
  bottom: 0;
  animation-name: floatUp;
  animation-timing-function: ease-out;
  animation-iteration-count: infinite;
  opacity: 0.8;
  z-index: 10;
}

.heart::before,
.heart::after {
  content: "";
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: #ff6b81;
  border-radius: 50%;
}

.heart::before {
  top: -10px;
  left: 0;
}

.heart::after {
  left: 10px;
  top: 0;
}

/* 하트 위치 및 애니메이션 타이밍 */
.heart:nth-child(1) {
  left: 20%;
  animation-duration: 4s;
  animation-delay: 0s;
}
.heart:nth-child(2) {
  left: 40%;
  animation-duration: 5s;
  animation-delay: 1.5s;
  width: 15px;
  height: 15px;
}
.heart:nth-child(3) {
  left: 60%;
  animation-duration: 6s;
  animation-delay: 3s;
  width: 25px;
  height: 25px;
}
.heart:nth-child(4) {
  left: 80%;
  animation-duration: 4.5s;
  animation-delay: 2s;
  width: 18px;
  height: 18px;
}
</style>

<!-- 하트 div 4개 -->
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
"""

# CSS 적용
st.markdown(page_bg_css, unsafe_allow_html=True)

# 타이틀과 설명
st.title("📘 내가 웹툰 속에 들어간다면?")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다!")

# 이름 입력
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

    # 결과 한 줄로 조합
    result = (f"{name}님의 웹툰 캐릭터는 키 {height}cm에 '{role}' 포지션이며, "
              f"외형은 {appearance}, 성격은 {personality}입니다.")
    return result

if name:
    st.write(generate_character(name))

    if st.button("다시 하기"):
        st.experimental_rerun()
