import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="🩷", layout="centered")

# -------------------- CSS --------------------
css = """
<style>
@keyframes fadeIn {from {opacity: 0; transform: translateY(-20px);} to {opacity:1; transform: translateY(0);}}
@keyframes glow {0% {text-shadow: 0 0 5px #ff69b4, 0 0 10px #ff1493;}50% {text-shadow: 0 0 20px #ff69b4, 0 0 35px #ff1493;}100% {text-shadow: 0 0 5px #ff69b4, 0 0 10px #ff1493;}}
@keyframes boxGlow {0% {box-shadow: 0 6px 15px rgba(255,105,180,0.5);}50% {box-shadow: 0 15px 30px rgba(255,20,147,0.8);}100% {box-shadow: 0 6px 15px rgba(255,105,180,0.5);}}
@keyframes fireworks {0% {transform: scale(0.5); opacity: 1;}50% {transform: scale(1.5);}100% {transform: scale(2.5); opacity: 0;}}
@keyframes itemBounce {0%, 100% {transform: translateY(0);}50% {transform: translateY(-10px);}}

.stApp {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ff69b4);
    font-family: 'Nanum Gothic', sans-serif;
    color: #6a0d53;
    text-align: center;
    overflow: hidden;
}

.stButton>button {
    background: #ff69b4;
    color: white;
    border-radius: 25px;
    padding: 12px 40px;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: #ff1493;
    transform: scale(1.15) rotate(-3deg);
}

.result-box {
    background: #fff0f4;
    border: 2px solid #ff69b4;
    border-radius: 25px;
    padding: 30px;
    margin: 30px auto;
    max-width: 600px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 600;
    color: #7b2a5a;
    animation: boxGlow 2s infinite;
    position: relative;
    z-index: 10;
}

.item {
    display: inline-block;
    margin: 5px 10px;
    padding: 5px 10px;
    border-radius: 12px;
    background: #ffd1e8;
    font-weight: 600;
    animation: glow 2s infinite, itemBounce 1s infinite;
}

.position-icon {display: inline-block; animation: glow 1.5s infinite;}

.fade1 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.3s; font-size:2rem; color:#ff1493;}
.fade2 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.6s;}
.fade3 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.9s; font-weight:700; color:#d61a8d;}
.fade4 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.2s;}
.fade5 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.5s;}
.fade6 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.8s;}

/* 폭죽 */
.firework {
    position: absolute;
    width: 12px;
    height: 12px;
    background: radial-gradient(circle, #ff1493 0%, #ff69b4 70%);
    border-radius: 50%;
    animation: fireworks 1.2s ease-out forwards;
    mix-blend-mode: screen;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- UI --------------------
st.title("🩷 내가 웹툰 속에 들어간다면? 🩷")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다! 🌟")

name = st.text_input("당신의 이름을 입력하세요:")

# -------------------- 캐릭터 데이터 --------------------
roles = ["⚽ 다정한 공", "❄ 차가운 공", "😏 능글맞은 공", "🙈 츤데레 공",
         "🌸 순진한 수", "🐰 새침한 수", "🍀 털털한 수", "🌑 상처 많은 수"]
appearances = ["짧은 흑발에 강한 인상", "긴 생머리에 차가운 눈매", "은은한 미소를 가진 얼굴",
               "눈이 크고 인형 같은 외모", "스포티한 스타일에 건강미 넘침", "항상 후드를 쓰고 다니는 미스터리한 모습",
               "붉은 염색머리에 개성 넘치는 분위기", "단정한 안경과 깔끔한 헤어스타일"]
personalities = ["겉은 차가워 보이지만 속은 따뜻한 스타일 💖", "모든 사람에게 친절한 인싸 ✨",
                 "혼자 있는 걸 좋아하는 무뚝뚝한 타입 😶", "정의감 넘치고 다혈질 🔥",
                 "감성적이고 눈물이 많은 성격 😢", "장난기 많고 유쾌한 분위기 메이커 😆"]
items = ["🏆 트로피", "🎧 헤드폰", "📚 책", "🌸 꽃", "⚡ 전기볼", "🦄 마법봉", "🎨 팔레트"]

# -------------------- 캐릭터 생성 함수 --------------------
def generate_character(name):
    height = random.randint(150, 190)
    role = random.choice(roles)
    appearance = random.choice(appearances)
    personality = random.choice(personalities)
    item = random.choice(items)
    height_str = f"<b>{height}cm</b> 🔥" if height >= 180 else f"<b>{height}cm</b>"
    
    return f"""
    <div class='result-box'>
        <h2 class='fade1'>{name}님의 웹툰 캐릭터</h2>
        <p class='fade2'>📏 키: {height_str}</p>
        <p class='fade3'>포지션: <b class='position-icon'>{role}</b></p>
        <p class='fade4'>외형: <b>{appearance}</b></p>
        <p class='fade5'>성격: <b>{personality}</b></p>
        <p class='fade6'>아이템: <span class='item'>{item}</span><br><br>
        🎯 오늘의 운세: {random.choice(['행운 가득! 🍀', '도전의 날! 🔥', '느긋한 하루 🐢', '새로운 만남 기대 ✨'])}</p>
    </div>
    """

# -------------------- 폭죽 랜덤 생성 --------------------
def fireworks_effect():
    firework_html = ""
    for i in range(10):  # 폭죽 수 늘림
        x = random.randint(5, 95)
        y = random.randint(10, 80)
        firework_html += f"<div class='firework' style='top:{y}%; left:{x}%; animation-delay:{random.uniform(0,1)}s;'></div>"
    st.markdown(firework_html, unsafe_allow_html=True)

# -------------------- 결과 출력 --------------------
if name and st.button("✨ 캐릭터 생성!"):
    fireworks_effect()
    st.markdown(generate_character(name), unsafe_allow_html=True)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", start_time=0)
