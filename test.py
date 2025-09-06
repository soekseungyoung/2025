import streamlit as st
from datetime import datetime

st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

# -------------------- 별 배경 --------------------
stars_html = ""
for i in range(50):  # 안정적 50개
    left = (i * 2) % 100
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
        top: 0; left:0;
        overflow: hidden;
        z-index:-1;
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
        from {{ transform: translateY(0); opacity:1; }}
        to {{ transform: translateY(-110vh); opacity:0; }}
    }}
    @keyframes twinkle {{
        0%,100% {{ opacity:0.8; }}
        50% {{ opacity:0.3; }}
    }}
    .title {{
        font-size: 42px;
        color: #FFD700;
        text-align: center;
        margin-top: 30px;
        text-shadow: 0 0 15px #FFD700;
    }}
    .report {{
        background: rgba(20,20,20,0.85);
        border: 2px solid #FFD700;
        border-radius: 10px;
        padding: 25px;
        margin-top: 20px;
        color: #f5f5dc;
        font-size: 18px;
        line-height: 1.7;
        box-shadow: 0 0 20px rgba(255,215,0,0.5);
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

# -------------------- 제목 --------------------
st.markdown('<h1 class="title">내가 웹툰에 들어간다면?</h1>', unsafe_allow_html=True)
st.write("✨ 별빛 아래 황금빛 사주풀이로 당신의 웹툰 캐릭터 운명을 알려드립니다 ✨")

# -------------------- 입력폼 --------------------
with st.form("user_form"):
    name = st.text_input("이름을 입력하세요")
    gender = st.radio("성별을 선택하세요", ["여자", "남자"])
    birth_date = st.date_input("생년월일", min_value=datetime(1900,1,1), max_value=datetime.today())
    birth_time = st.time_input("출생 시간")
    submitted = st.form_submit_button("결과 보기")

# -------------------- 사주 풀이 --------------------
if submitted:
    # Stem / Branch 간단 계산
    year, month, day, hour = birth_date.year, birth_date.month, birth_date.day, birth_time.hour
    heavenly_stems = ["갑", "을", "병", "정", "무", "기", "경", "신", "임", "계"]
    earthly_branches = ["자", "축", "인", "묘", "진", "사", "오", "미", "신", "유", "술", "해"]
    
    # 년/월/일/시 Stem & Branch
    stems = [heavenly_stems[year%10], heavenly_stems[month%10], heavenly_stems[day%10], heavenly_stems[hour%10]]
    branches = [earthly_branches[year%12], earthly_branches[month%12], earthly_branches[day%12], earthly_branches[hour%12]]

    # 간단 점수 기반 오행 체크
    element_score = {"목":0, "화":0, "토":0, "금":0, "수":0}
    stem_to_element = {"갑":"목","을":"목","병":"화","정":"화","무":"토","기":"토","경":"금","신":"금","임":"수","계":"수"}
    for s in stems:
        element_score[stem_to_element[s]] +=1

    # 성격/현재/미래/연애/재물 운세 문장 선택
    def pick_sentence(options, score):
        idx = score % len(options)
        return options[idx]

    personality_options = [
        "솔직하며 추진력이 강하고, 세심한 내면을 가진 성격입니다. 주변 사람들에게 신뢰와 안정감을 주며, 위기 상황에서도 침착하게 판단할 수 있습니다.",
        "외향적이며 사교성이 뛰어나고, 도전을 즐기는 성격입니다. 새로운 관계에서도 적극적으로 나섭니다.",
        "분석적이고 신중한 성격으로, 계획을 세우고 실행하는 능력이 뛰어납니다.",
        "창의적이며 감수성이 풍부해 예술적 감각이 뛰어난 편입니다.",
        "책임감이 강하고 꾸준함을 지닌 성격으로, 목표를 끝까지 달성하려는 성향이 강합니다."
    ]
    current_options = [
        "현재는 활발한 시기이며 새로운 기회를 적극적으로 맞이할 수 있습니다. 주변 변화에 민감하게 대응하며 올바른 선택을 내릴 수 있습니다.",
        "지금은 자신의 능력을 점검하고 전략을 세우기에 적합한 시기입니다. 집중력을 발휘하면 큰 성과를 얻을 수 있습니다.",
        "현재는 주위 상황에 따라 판단력이 중요한 시기입니다. 계획과 실행의 균형이 요구됩니다.",
        "잠시 숨을 고르며 내면을 돌아보는 시기입니다. 성찰과 준비가 미래의 성공을 돕습니다.",
        "중요한 결정을 내리기에 다소 혼란스러운 시기입니다. 신중하게 선택하는 것이 필요합니다."
    ]
    future_options = [
        "앞으로 큰 성취를 이룰 가능성이 높으며, 새로운 도전에서 주도적인 역할을 할 수 있습니다. 노력과 인내가 결실을 맺는 시기입니다.",
        "미래에는 안정적인 성과와 꾸준한 성장의 기회가 찾아옵니다. 계획적으로 행동하면 큰 보상을 얻습니다.",
        "다가오는 시기에는 예상치 못한 변화가 찾아오지만 유연하게 대응하면 기회로 바뀝니다.",
        "주변의 도움과 협력이 중요한 역할을 합니다. 협력과 조율이 미래의 성취를 돕습니다.",
        "자신의 노력과 인내가 결실을 맺는 시기입니다. 꾸준함이 장기적 성공으로 이어집니다."
    ]
    love_options = [
        "연애운이 좋으며 새로운 인연이 찾아올 가능성이 높습니다. 솔직한 소통과 배려가 관계를 깊게 만듭니다.",
        "연애보다 자기 성장에 집중하면 좋은 시기입니다. 자기 계발이 미래의 사랑을 돕습니다.",
        "연애에서는 작은 배려와 관심이 큰 결실로 이어질 수 있습니다. 세심한 마음이 중요합니다.",
        "연애운은 평온하며 안정적인 관계를 유지하기 좋은 시기입니다.",
        "새로운 만남이 찾아오지만 상대를 신중하게 관찰하는 것이 좋습니다."
    ]
    finance_options = [
        "재물운이 좋아 계획적 투자가 성과를 가져올 수 있습니다. 장기적 계획이 중요합니다.",
        "조금 더 신중한 금전 관리가 필요합니다. 충동적 소비를 피하세요.",
        "꾸준한 노력과 계획이 장기적으로 재물 안정으로 이어집니다.",
        "금전적 변동이 있을 수 있으므로 계획을 세우는 것이 중요합니다.",
        "재물운은 양호하지만 충동적 결정은 피해야 합니다."
    ]

    # 메인 오행 점수 높은 것 기준으로 선택
    max_element = max(element_score, key=element_score.get)
    p_score = element_score[max_element]
    
    personality_text = pick_sentence(personality_options, p_score)
    current_text = pick_sentence(current_options, p_score)
    future_text = pick_sentence(future_options, p_score)
    love_text = pick_sentence(love_options, p_score)
    finance_text = pick_sentence(finance_options, p_score)

    # -------------------- 출력 --------------------
    st.markdown(f"""
    <div class="report">
        <h3>🔮 {name}님의 디테일 사주 리포트</h3>
        <p><b>성별:</b> {gender}</p>
        <p><b>생년월일:</b> {birth_date.strftime('%Y-%m-%d')}</p>
        <p><b>출생시각:</b> {birth_time.strftime('%H:%M')}</p>
        <hr>
        <p><b>사주팔자:</b><br>
           {stems[0]} {branches[0]} / {stems[1]} {branches[1]} / {stems[2]} {branches[2]} / {stems[3]} {branches[3]}
        </p>
        <hr>
        <h3>🌟 성격</h3>
        <p>{personality_text}</p>
        <h3>📍 현재 운세</h3>
        <p>{current_text}</p>
        <h3>🔮 미래 운세</h3>
        <p>{future_text}</p>
        <h3>💖 연애운</h3>
        <p>{love_text}</p>
        <h3>💰 재물운</h3>
        <p>{finance_text}</p>
    </div>
    """, unsafe_allow_html=True)
