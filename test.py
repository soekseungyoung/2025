import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="🩷", layout="centered")

# -------------------- CSS --------------------
css = """
<style>
@keyframes fadeIn {from {opacity: 0; transform: translateY(-20px);} to {opacity:1; transform: translateY(0);}}
@keyframes glow {0% {text-shadow: 0 0 5px #ff69b4, 0 0 10px #ff1493;}50% {text-shadow: 0 0 20px #ff69b4, 0 0 35px #ff1493;}100% {text-shadow: 0 0 5px #ff69b4, 0 0 10px #ff1493;}}
@keyframes boxGlow {0% {box-shadow: 0 6px 15px rgba(255,105,180,0.5);}50% {box-shadow: 0 15px 30px rgba(255,20,147,0.9);}100% {box-shadow: 0 6px 15px rgba(255,105,180,0.5);}}
@keyframes fireworks {0% {transform: scale(0.5); opacity: 1;}50% {transform: scale(2); opacity: 0.8;}100% {transform: scale(3); opacity: 0;}}
@keyframes sparkle {0%,100% {opacity:0.2;}50% {opacity:1;}}
@keyframes itemBounce {0%, 100% {transform: translateY(0);}50% {transform: translateY(-12px) scale(1.1);}}

/* 전체 앱 */
.stApp {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ff69b4, #ff1493, #d61a8d);
    font-family: 'Nanum Gothic', sans-serif;
    color: #6a0d53;
    text-align: center;
    overflow: hidden;
}

/* 버튼 */
.stButton>button {
    background: linear-gradient(90deg, #ff69b4, #ff1493);
    color: white;
    border-radius: 30px;
    padding: 14px 45px;
    font-size: 20px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0px 0px 15px rgba(255,20,147,0.6);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #ff1493, #ff69b4);
    transform: scale(1.15) rotate(-4deg);
    box-shadow: 0px 0px 30px rgba(255,20,147,0.9);
}

/* 캐릭터 박스 */
.result-box {
    background: #fff0f9;
    border: 3px solid #ff69b4;
    border-radius: 30px;
    padding: 40px;
    margin: 30px auto;
    max-width: 650px;
    text-align: center;
    font-size: 1.4rem;
    font-weight: 700;
    color: #7b2a5a;
    animation: boxGlow 2s infinite;
    position: relative;
    z-index: 10;
    box-shadow: 0px 0px 20px rgba(255,105,180,0.6);
}

/* 아이템 */
.item {
    display: inline-block;
    margin: 8px 12px;
    padding: 6px 12px;
    border-radius: 15px;
    background: linear-gradient(135deg, #ffd1e8, #ffe4f2);
    font-weight: 700;
    animation: glow 2s infinite, itemBounce 1.2s infinite;
}

/* 포지션 강조 */
.position-icon {
    display: inline-block;
    animation: glow 1.5s infinite, sparkle 1s infinite alternate;
}

/* 텍스트 등장 애니메이션 */
.fade1 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.3s; font-size:2.3rem; color:#ff1493; text-shadow:0 0 10px #ff69b4;}
.fade2 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.7s;}
.fade3 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.0s; font-weight:800; color:#d61a8d;}
.fade4 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.3s;}
.fade5 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.6s;}
.fade6 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 2.0s;}

/* 폭죽 */
.firework {
    position: absolute;
    width: 14px;
    height: 14px;
    background: radial-gradient(circle, #ff1493 0%, #ff69b4 50%, #ffd700 100%);
    border-radius: 50%;
    animation: fireworks 1.5s ease-out forwards;
    mix-blend-mode: screen;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- UI --------------------
st.title("🩷 내가 웹툰 속에 들어간다면? 🩷")
st.markdown("이름을 입력하면 화려한 웹툰 속 캐릭터로 등장합니다! 🌟✨")

name = st.text_input("당신의 이름을 입력하세요:")

# -------------------- 캐릭터 데이터 --------------------
roles = ["⚡ 카리스마 주인공", "🌸 청순한 히로인", "🔥 열혈 파이터", "❄ 차가운 천재",
         "🌑 비밀스러운 라이벌", "🎭 능청스러운 조력자", "🌟 모두의 아이돌", "🌀 어두운 과거의 인물"]
appearances = ["짧은 흑발에 강렬한 눈빛", "은은한 미소를 가진 금발", "차분한 흑단 머리에 서늘한 눈매",
               "화려한 염색머리와 자신감 넘치는 포즈", "단정한 안경과 지적인 분위기", "항상 후드를 쓰고 다니는 미스터리한 모습",
               "햇살 같은 미소와 따뜻한 인상", "날렵한 이목구비와 도도한 표정"]
personalities = ["겉은 차갑지만 속은 따뜻한 츤데레 💖", "항상 웃음을 주는 분위기 메이커 🎉",
                 "모두를 지키려는 정의감 넘치는 성격 🔥", "예술적 감각이 빛나는 감성파 🎨",
                 "고집이 강하지만 신념을 지키는 타입 🛡", "자신감 넘치고 도전적인 성격 🚀",
                 "소박하지만 다정한 마음씨 💕", "조용하지만 존재감이 큰 캐릭터 🌌"]
items = ["🏆 트로피", "🎧 헤드폰", "📚 책", "🌸 꽃", "⚡ 전기볼", "🦄 마법봉", "🎨 팔레트", "🗡 전설의 검"]

# -------------------- 캐릭터 생성 함수 --------------------
def generate_character(name):
    height = random.randint(150, 190)
    role = random.choice(roles)
    appearance = random.choice(appearances)
    personality = random.choice(personalities)
    item = random.choice(items)
    height_str = f"<b>{height}cm</b> 🌟" if height >= 180 else f"<b>{height}cm</b>"
    
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
    for i in range(15):  # 폭죽 수 더 많게
        x = random.randint(5, 95)
        y = random.randint(5, 80)
        color = random.choice(["#ff1493", "#ff69b4", "#ffd700", "#00ffff", "#ff4500"])
        firework_html += f"<div class='firework' style='top:{y}%; left:{x}%; background: radial-gradient(circle, {color} 0%, white 80%); animation-delay:{random.uniform(0,1)}s;'></div>"
    st.markdown(firework_html, unsafe_allow_html=True)

# -------------------- 결과 출력 --------------------
if name and st.button("✨ 캐릭터 생성!"):
    fireworks_effect()
    st.markdown(generate_character(name), unsafe_allow_html=True)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", start_time=0)
