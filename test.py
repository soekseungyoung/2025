import streamlit as st
import random

st.set_page_config(page_title="평행우주 인생 시뮬레이터", page_icon="🌀", layout="centered")

st.title("🌀 평행우주 인생 시뮬레이터")
st.markdown("당신은 다른 우주에서 어떤 인생을 살고 있을까요? 버튼을 눌러 확인해보세요!")

# 입력
name = st.text_input("이름을 입력하세요", "")
universe_count = st.slider("생성할 평행우주 개수", 1, 5, 3)

if st.button("🌌 평행우주 생성하기"):
    if name.strip() == "":
        st.warning("이름을 입력하세요!")
    else:
        # 무작위 데이터 풀
        eras = ["조선시대", "미래 사이버펑크 도시", "공룡시대", "우주 식민지 시대", "중세 판타지 왕국", "현대 평행세계"]
        jobs = ["용병", "왕의 측근", "프로게이머", "치킨집 사장", "천재 발명가", "밈 제작자", "우주 해적", "철학자"]
        fates = [
            "예상치 못한 사랑을 만납니다 💕",
            "큰 부자가 되지만 친구를 잃습니다 💰",
            "세계의 구원자가 됩니다 🌍",
            "평생 숙제를 끝내지 못합니다 📚",
            "운명의 장난으로 닌자가 됩니다 🥷",
            "치킨 한 마리에 인생을 바칩니다 🍗",
        ]
        
        for i in range(universe_count):
            era = random.choice(eras)
            job = random.choice(jobs)
            fate = random.choice(fates)
            
            st.subheader(f"🌠 우주 #{i+1}")
            st.write(f"이름: **{name}**")
            st.write(f"시대: **{era}**")
            st.write(f"직업: **{job}**")
            st.write(f"운명: {fate}")
            st.markdown("---")

