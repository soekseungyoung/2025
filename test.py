import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="🩷", layout="centered")

# -------------------- CSS --------------------
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
.result-box {
    background: #fff0f4;
    border: 2px solid #d57ea0;
    border-radius: 20px;
    padding: 20px;
    margin: 30px auto;
    max-width: 500px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 600;
    color: #7b2a5a;
    box-shadow: 0 6px 12px rgba(213, 126, 160, 0.4);
}
/* 하트 애니메이션 */
@keyframes floatUp {
  0% { transform: translateY(0) scale(1) rotate(-45deg); opacity: 0.8; }
  100% { transform: translateY(-200px) scale(1.5) rotate(-45deg); opacity: 0; }
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
.heart::before { top: -9px; left: 0; }
.heart::after { left: 9px; top: 0; }
.heart:nth-child(1) { left: 12%; animation-duration: 5.5s; animation-delay: 0s; }
.heart:nth-child(2) { left: 28%; animation-duration: 6.8s; animation-delay: 1.2s; width: 15px; height: 15px; }
.heart:nth-child(3) { left: 45%; animation-duration: 7.4s; animation-delay: 2.4s; width: 22px; height: 22px; }
.heart:nth-child(4) { left: 62%; animation-duration: 5.9s; animation-delay: 3s; width: 19px; height: 19px; }
.heart:nth-child(5) { left: 78%; animation-duration: 6.2s; animation-delay: 1.7s; width: 17px; height: 17px; }
.heart:nth-child(6) { left: 90%; animation-duration: 7s; animation-delay: 2.9s; width: 20px; height: 20px; }
</style>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- UI --------------------
st.title("🩷내가 웹툰 속에 들어간다면?🩷")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다! ⚽️")

name = st.text_input("당신의 이름을 입력하세요:")

# -------------------- 캐릭터 생성 함수 --------------------
def generate_character(name):
    height = random.randint(150, 190)
    roles = [
        "⚽ 다정한 공", "❄ 차가운 공", "😏 능글맞은 공", "🙈 츤데레 공",
        "🌸 순진한 수", "🐰 새침한 수", "🍀 털털한 수", "🌑 상처 많은 수"
    ]
    role = random.choice(roles)

    appearances = [
        "짧은 흑발에 강한 인상", "긴 생머리에 차가운 눈매", "은은한 미소를 가진 얼굴",
        "눈이 크고 인형 같은 외모", "스포티한 스타일에 건강미 넘침",
        "항상 후드를 쓰고 다니는 미스터리한 모습", "붉은 염색머리에 개성 넘치는 분위기",
        "단정한 안경과 깔끔한 헤어스타일", "부드러운 갈색 머리에 따뜻한 인상",
        "피어싱이 돋보이는 스트릿 패션", "백발에 신비로운 오라를 풍김",
        "햇살 같은 금발과 밝은 미소", "잘 다져진 근육질 몸매와 자신감 넘치는 포즈",
        "차분한 흑단 머리에 서늘한 눈빛", "웃을 때 보조개가 매력적인 얼굴",
        "항상 헤드폰을 걸치고 다니는 자유로운 모습", "비 오는 날 모자를 눌러쓰는 청춘 같은 분위기",
        "흰 피부에 대비되는 검은 옷차림", "날렵한 이목구비와 도도한 표정",
        "귀여운 단발머리에 발랄한 스타일", "항상 피곤해 보이는 무심한 인상",
        "운동복 차림에 땀에 젖은 건강미", "부드러운 눈매에 신뢰감을 주는 외모",
        "언제나 미소를 머금은 상냥한 인상", "시크한 눈썹과 도발적인 미소"
    ]
    appearance = random.choice(appearances)

    personalities = [
        "겉은 차가워 보이지만 속은 따뜻한 스타일 💖",
        "모든 사람에게 친절한 인싸 ✨",
        "혼자 있는 걸 좋아하는 무뚝뚝한 타입 😶",
        "정의감 넘치고 다혈질 🔥",
        "감성적이고 눈물이 많은 성격 😢",
        "장난기 많고 유쾌한 분위기 메이커 😆",
        "책임감이 강하고 팀을 이끄는 리더십 💪",
        "새로운 걸 좋아하는 모험가 타입 🌍",
        "귀찮음을 많이 타지만 할 건 하는 성격 😴",
        "배려심 많고 남을 잘 챙기는 스타일 🤗",
        "분위기를 주도하는 파티 메이커 🎉",
        "예술적 감각이 뛰어난 감성파 🎨",
        "고집이 강하지만 신념을 지키는 성격 🛡",
        "조용하지만 존재감이 큰 타입 🌌",
        "허당끼가 있는 귀여운 성격 🐣",
        "상상력이 풍부하고 몽상가 같은 스타일 ☁️",
        "마이페이스지만 매력적인 캐릭터 😎",
        "자신감 넘치고 항상 도전하는 타입 🚀",
        "섬세하고 공감 능력이 뛰어난 따뜻한 성격 💕",
        "겉으로는 무심해 보여도 은근 다정한 츤데레 🐺",
        "열정적이고 목표에 몰두하는 노력가 🔥",
        "어색하지만 은근히 귀여운 성격 🐱",
        "사소한 것에 행복을 느끼는 소박한 성격 🌼"
    ]
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
    if st.button("🔄 다시 하기"):
        st.experimental_rerun()
