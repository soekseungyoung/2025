import streamlit as st
import random

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="🩷", layout="centered")

# -------------------- 스타일 --------------------
css = """
<style>
@keyframes fadeIn {
  from {opacity: 0; transform: translateY(30px);}
  to {opacity: 1; transform: translateY(0);}
}
@keyframes glow {
  0% { text-shadow: 0 0 5px #fff, 0 0 10px #ff69b4, 0 0 20px #ff1493; }
  50% { text-shadow: 0 0 20px #fff, 0 0 40px #ff69b4, 0 0 60px #ff1493; }
  100% { text-shadow: 0 0 5px #fff, 0 0 10px #ff69b4, 0 0 20px #ff1493; }
}
@keyframes aurora {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}
.stApp {
    background: linear-gradient(270deg, #0f0c29, #302b63, #24243e);
    background-size: 600% 600%;
    animation: aurora 20s ease infinite;
    font-family: 'Georgia', serif;
    color: white;
}
.result-box {
    animation: fadeIn 1.5s ease-in-out;
    background: rgba(0,0,0,0.6);
    border-radius: 20px;
    padding: 30px;
    margin-top: 30px;
    font-size: 22px;
    text-align: center;
    color: #fff;
    box-shadow: 0 0 30px rgba(255, 105, 180, 0.9), inset 0 0 20px rgba(255,255,255,0.2);
    border: 2px solid rgba(255,255,255,0.2);
}
.result-box b {
    animation: glow 2s infinite;
    font-size: 24px;
}
.stButton>button {
    background: linear-gradient(135deg, #ff7eb3, #ff758c);
    border: none;
    padding: 12px 24px;
    color: white;
    font-size: 18px;
    border-radius: 12px;
    box-shadow: 0px 5px 20px rgba(255, 118, 136, 0.6);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 8px 30px rgba(255, 118, 136, 0.9);
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- 데이터 --------------------
roles = ["주인공", "조력자", "빌런", "라이벌", "은밀한 관찰자", "숨겨진 영웅", "어둠의 지배자", "전설 속 인물"]
personalities = ["차가운 카리스마", "엉뚱 발랄", "잔혹한 천재", "순수한 정의감", "예측 불가능", "고독한 천재", "배신자", "희생자"]
items = ["운명의 검", "마법의 펜던트", "불멸의 반지", "비밀의 책", "시간을 거스르는 시계", "검은 망토", "빛나는 수정", "금지된 주문서"]

fates = [
    "뜻밖의 배신으로 무너졌다.", "친구를 구하고 자신은 사라졌다.", "가장 소중한 것을 지키고 산산조각 났다.",
    "끝내 외롭게 무너져 갔다.", "결국 악마가 되어버렸다.", "영웅으로 살았으나, 이름조차 잊혀졌다.",
    "전설로 남아 후대의 이야기 속에 살아간다.", "마지막 순간, 모든 이를 지켜냈다.",
    "불멸의 상징으로 기억되었다.", "스스로를 희생해 세상을 구했다.",
    "사랑을 지키기 위해 모든 것을 버렸다.", "연인과 재회한 순간, 생이 다했다.",
    "제국을 세웠으나 왕좌에서 홀로 죽었다.", "야망을 위해 달려갔으나 결국 패망했다.",
    "흔적도 없이 사라져 전설로 남았다.", "끝내 정체가 밝혀지지 않았다."
]

# -------------------- UI --------------------
st.title("🌌 내가 웹툰 속에 들어간다면? 🌌")
st.markdown("당신의 운명을 장엄한 웹툰 서사로 확인해보세요. ⚔️")

name = st.text_input("✨ 이름을 입력하세요:")

if st.button("운명 확인하기"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요!")
    else:
        role = random.choice(roles)
        personality = random.choice(personalities)
        item = random.choice(items)
        fate = random.choice(fates)

        result = f"""
        <div class="result-box">
        🌟 <b>{name}</b> 님은 웹툰 속에서... <br><br>
        🎭 역할: <b>{role}</b><br>
        💫 성격: <b>{personality}</b><br>
        🔮 아이템: <b>{item}</b><br>
        ⚔️ 최후: <b>{fate}</b>
        </div>
        """
        st.markdown(result, unsafe_allow_html=True)
