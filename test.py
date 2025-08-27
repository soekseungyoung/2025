import streamlit as st
import random

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="🩷", layout="centered")

# -------------------- CSS --------------------
css = """
<style>
@keyframes fadeIn {
  from {opacity: 0; transform: translateY(-20px);}
  to {opacity: 1; transform: translateY(0);}
}
.stApp {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ff69b4);
    font-family: 'Nanum Gothic', sans-serif;
    color: #6a0d53;
    text-align: center;
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
    transform: scale(1.1);
}
.result-box {
    background: #fff0f4;
    border: 2px solid #ff69b4;
    border-radius: 20px;
    padding: 25px;
    margin: 30px auto;
    max-width: 550px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 600;
    color: #7b2a5a;
    box-shadow: 0 6px 15px rgba(255, 105, 180, 0.5);
}
.item {
    display: inline-block;
    margin: 5px 10px;
    padding: 5px 10px;
    border-radius: 12px;
    background: #ffd1e8;
    font-weight: 500;
}
.fade1 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.3s;}
.fade2 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.6s;}
.fade3 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 0.9s;}
.fade4 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.2s;}
.fade5 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.5s;}
.fade6 {animation: fadeIn 0.5s ease forwards; opacity:0; animation-delay: 1.8s;}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- UI --------------------
st.title("🩷 내가 웹툰 속에 들어간다면? 🩷")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다! ⚽️")

name = st.text_input("당신의 이름을 입력하세요:")

# -------------------- 캐릭터 데이터 --------------------
roles = ["⚽ 다정한 공", "❄ 차가운 공", "😏 능글맞은 공", "🙈 츤데레 공",
         "🌸 순진한 수", "🐰 새침한 수", "🍀 털털한 수", "🌑 상처 많은 수"]
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
    "귀여운 단발머리에 발랄한 스타일", "항상 피곤해 보이는 무심한 인상"
]
personalities = [
    "겉은 차가워 보이지만 속은 따뜻한 스타일 💖", "모든 사람에게 친절한 인싸 ✨",
    "혼자 있는 걸 좋아하는 무뚝뚝한 타입 😶", "정의감 넘치고 다혈질 🔥",
    "감성적이고 눈물이 많은 성격 😢", "장난기 많고 유쾌한 분위기 메이커 😆",
    "책임감이 강하고 팀을 이끄는 리더십 💪", "새로운 걸 좋아하는 모험가 타입 🌍",
    "귀찮음을 많이 타지만 할 건 하는 성격 😴", "배려심 많고 남을 잘 챙기는 스타일 🤗",
    "분위기를 주도하는 파티 메이커 🎉", "예술적 감각이 뛰어난 감성파 🎨",
    "고집이 강하지만 신념을 지키는 성격 🛡", "조용하지만 존재감이 큰 타입 🌌",
    "허당끼가 있는 귀여운 성격 🐣", "상상력이 풍부하고 몽상가 같은 스타일 ☁️",
    "마이페이스지만 매력적인 캐릭터 😎", "자신감 넘치고 항상 도전하는 타입 🚀",
    "섬세하고 공감 능력이 뛰어난 따뜻한 성격 💕", "겉으로는 무심해 보여도 은근 다정한 츤데레 🐺",
    "열정적이고 목표에 몰두하는 노력가 🔥", "어색하지만 은근히 귀여운 성격 🐱",
    "사소한 것에 행복을 느끼는 소박한 성격 🌼"
]
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
        <p class='fade3'>포지션: <b>{role}</b></p>
        <p class='fade4'>외형: <b>{appearance}</b></p>
        <p class='fade5'>성격: <b>{personality}</b></p>
        <p class='fade6'>아이템: <span class='item'>{item}</span><br><br>
        🎯 오늘의 운세: {random.choice(['행운 가득! 🍀', '도전의 날! 🔥', '느긋한 하루 🐢', '새로운 만남 기대 ✨'])}</p>
    </div>
    """

# -------------------- 결과 출력 --------------------
if name and st.button("✨ 캐릭터 생성!"):
    st.markdown(generate_character(name), unsafe_allow_html=True)
