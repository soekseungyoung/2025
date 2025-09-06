import streamlit as st
from datetime import datetime

st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

# -------------------- 별 배경 --------------------
stars_html = ""
for i in range(60):  # 별 60개
    left = (i * 3) % 100
    duration = 15 + (i % 10)
    delay = i % 5
    size = 2 if i % 3 else 3
    stars_html += f'<div class="star" style="left:{left}%; width:{size}px; height:{size}px; animation-duration:{duration}s; animation-delay:{delay}s;"></div>'

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: black;
        position: relative;
        overflow: hidden;
    }}
    .stars {{
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        overflow: hidden;
        z-index: -1;
    }}
    .star {{
        position: absolute;
        top: 100vh;
        background: #FFD700;
        border-radius: 50%;
        animation: moveUp linear infinite, twinkle ease-in-out infinite;
        opacity: 0.8;
    }}
    @keyframes moveUp {{
        from {{ transform: translateY(0); opacity: 1; }}
        to {{ transform: translateY(-110vh); opacity: 0; }}
    }}
    @keyframes twinkle {{
        0%, 100% {{ opacity: 0.8; }}
        50% {{ opacity: 0.3; }}
    }}
    .title {{
        font-size: 42px;
        color: #FFD700;
        text-align: center;
        margin-top: 30px;
        text-shadow: 0 0 15px #FFD700;
    }}
    .report {{
        background: rgba(20, 20, 20, 0.85);
        border: 1px solid #FFD700;
        border-radius: 10px;
        padding: 25px;
        margin-top: 20px;
        color: #f5f5dc;
        font-size: 18px;
        line-height: 1.7;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
    }}
    .report h3 {{
        color: #FFD700;
        text-shadow: 0 0 6px #FFD700;
    }}
    </style>
    <div class="stars">
        {stars_html}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">내가 웹툰에 들어간다면?</div>', unsafe_allow_html=True)

# -------------------- 입력 폼 --------------------
with st.form("user_info"):
    name = st.text_input("이름")
    gender = st.radio("성별", ["남자", "여자"])
    birth_date = st.date_input("생년월일", min_value=datetime(1900,1,1), max_value=datetime.today())
    birth_time = st.time_input("출생 시각", value=datetime.strptime("12:00", "%H:%M").time())
    submitted = st.form_submit_button("결과 보기")

# -------------------- 디테일 리포트 --------------------
if submitted:
    # 사주 스타일 디테일 리포트 예시
    past = f"{name}님은 과거에 많은 경험을 통해 자신만의 색깔을 찾아왔습니다. 어려움 속에서도 포기하지 않고 성장해 온 힘이 지금의 기반이 되었습니다."
    current = f"현재 {name}님은 자신만의 방향성을 탐색하며 주위 변화에 적응하고 있습니다. 특히 지금은 중요한 결정이나 새로운 기회를 맞이할 수 있는 시기입니다."
    future = f"미래에는 {gender}로서의 장점이 더욱 부각되며, 노력과 인내가 결실을 맺어 큰 성취를 이루게 될 것입니다. 새로운 도전과 모험에서 주도적인 역할을 할 가능성이 높습니다."
    personality = "타고난 성격은 솔직하며 추진력이 강하고, 동시에 세심하고 깊은 내면을 가진 사람입니다. 주변 사람들에게 신뢰와 안정감을 주는 성격입니다."
    love = "연애운은 부드러운 매력과 솔직한 표현으로 인연을 이끌어갈 수 있습니다. 다만 상대방의 마음을 세심히 살피고 배려하는 것이 중요합니다."
    finance = "재물운은 꾸준한 노력과 계획이 결실을 맺는 시기입니다. 단기적 욕심보다는 장기적인 계획과 준비가 재물과 안정으로 이어집니다."

    st.markdown(
        f"""
        <div class="report">
            <h3>🔮 {name}님의 디테일 사주 리포트</h3>
            <p><b>과거:</b> {past}</p>
            <p><b>현재:</b> {current}</p>
            <p><b>미래:</b> {future}</p>
            <p><b>성격:</b> {personality}</p>
            <p><b>연애운:</b> {love}</p>
            <p><b>재물운:</b> {finance}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
