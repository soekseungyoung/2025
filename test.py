import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

# -------------------- 스타일 --------------------
# 별 100개 생성 (랜덤 위치, 속도, 지연)
stars_html = ""
for i in range(100):
    left = random.randint(0, 100)      # 가로 위치 %
    duration = random.randint(12, 30)  # 위로 올라가는 시간 (s)
    delay = random.randint(0, 20)      # 시작 딜레이 (s)
    size = random.choice([1, 2, 2, 3]) # 별 크기 (랜덤, 작은 게 많음)
    stars_html += f'<div class="star" style="left:{left}%; width:{size}px; height:{size}px; animation-duration:{duration}s; animation-delay:{delay}s;"></div>'

st.markdown(
    f"""
    <style>
    /* 전체 배경 */
    .stApp {{
        background-color: black;
        position: relative;
        overflow: hidden;
    }}

    /* 별 컨테이너 */
    .stars {{
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        overflow: hidden;
        z-index: -1;
    }}

    /* 별 스타일 */
    .star {{
        position: absolute;
        background: #FFD700;
        border-radius: 50%;
        animation: moveUp linear infinite;
        opacity: 0.8;
    }}

    /* 위로 흐르는 애니메이션 */
    @keyframes moveUp {{
        from {{ transform: translateY(100vh); opacity: 1; }}
        to {{ transform: translateY(-10vh); opacity: 0; }}
    }}

    /* 제목 */
    .title {{
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 25px;
        color: #FFD700;
        text-shadow: 0px 0px 15px rgba(255,215,0,0.9), 0px 0px 30px rgba(255,215,0,0.7);
    }}

    /* 결과 박스 */
    .result-box {{
        background: rgba(20,20,20,0.85);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #FFD700;
        box-shadow: 0px 0px 20px rgba(255,215,0,0.6);
        margin-top: 30px;
    }}

    h2, h3 {{
        color: #FFD700;
        text-shadow: 0px 0px 6px rgba(255,215,0,0.7);
    }}

    p {{
        font-size: 16px;
        line-height: 1.8;
        color: #f5f5dc;
    }}
    </style>

    <div class="stars">
        {stars_html}
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- 제목 --------------------
st.markdown('<div class="title">내가 웹툰에 들어간다면?</div>', unsafe_allow_html=True)
st.write("✨ 별빛 아래 황금빛 사주풀이로 당신의 웹툰 캐릭터 운명을 알려드립니다 ✨")

# -------------------- 입력 --------------------
with st.form("user_form"):
    name = st.text_input("이름을 입력하세요")
    gender = st.radio("성별을 선택하세요", ["여자", "남자"])
    birth_date = st.date_input("생년월일", min_value=datetime(1900,1,1), max_value=datetime(2025,12,31))
    birth_time = st.time_input("출생 시간")
    submitted = st.form_submit_button("결과 보기")

# -------------------- 사주 기본 데이터 --------------------
heavenly_stems = ["갑(목)", "을(목)", "병(화)", "정(화)", "무(토)", "기(토)", "경(금)", "신(금)", "임(수)", "계(수)"]
earthly_branches = ["자(수)", "축(토)", "인(목)", "묘(목)", "진(토)", "사(화)", "오(화)", "미(토)", "신(금)", "유(금)", "술(토)", "해(수)"]

# 오행별 상세 리포트 (길게 작성)
element_report = {
    "목": {
        "성격": "당신은 끊임없는 성장과 변화를 추구하는 사람으로, 한 자리에 머물기보다는 늘 더 넓은 세상으로 나아가고자 합니다. 도전과 모험을 두려워하지 않고, 스스로의 가능성을 믿고 밀어붙이는 힘이 있습니다.",
        "대인관계": "활발한 에너지로 사람들을 이끌고 주변에 활력을 주는 리더형 인물입니다. 다만 지나친 고집은 갈등을 만들 수 있으니 조율이 필요합니다.",
        "현재": "지금은 새로운 기회의 문이 열리고 있는 시기입니다. 당신의 모험심이 강하게 발휘되며, 조금만 더 밀어붙인다면 큰 성과를 이룰 수 있습니다.",
        "미래": "앞으로 당신은 누군가의 길을 밝히는 개척자가 될 것입니다. 지도자적 위치에 설 가능성이 크며, 당신의 이름이 오랫동안 기억될 수 있습니다.",
        "웹툰캐릭터": "미지의 세계를 탐험하는 주인공. 끊임없이 모험하며 사람들에게 영감을 주는 인물."
    },
    "화": {
        "성격": "당신은 불꽃처럼 강렬하고 열정적인 사람입니다. 추진력이 대단해 하고자 마음먹은 일은 끝까지 밀어붙이며, 감정 표현이 솔직하고 직선적입니다.",
        "대인관계": "따뜻한 열정으로 사람들에게 활력을 주지만, 때로는 과도한 열기로 주변과 충돌할 수 있습니다.",
        "현재": "지금은 당신의 열정이 최고조에 달해 원하는 것을 향해 힘차게 달려가는 시기입니다. 다만 성급함을 조심하세요.",
        "미래": "큰 성취와 명성을 얻게 되지만, 감정을 다스리지 못하면 스스로를 소진시킬 수도 있습니다.",
        "웹툰캐릭터": "불꽃 전사. 전투와 드라마의 중심에서 모든 사건을 불러일으키는 핵심 인물."
    },
    "토": {
        "성격": "안정적이고 든든한 사람입니다. 주변 사람들이 의지할 수 있는 믿음을 주며, 성실하고 책임감이 강합니다.",
        "대인관계": "사람들을 편안하게 하고 조화롭게 어울리며, 신뢰를 쌓아가는 데 탁월합니다.",
        "현재": "지금은 안정과 성실함이 빛을 발하는 시기입니다. 노력한 만큼 인정받고 있으며, 주변에서도 당신의 신뢰를 높게 평가하고 있습니다.",
        "미래": "앞으로는 존경받는 멘토나 조언자로서 오랫동안 영향력을 미칠 수 있습니다.",
        "웹툰캐릭터": "지혜로운 조력자. 주인공 곁에서 든든하게 지켜주며 길을 안내하는 인물."
    },
    "금": {
        "성격": "당신은 결단력 있고 카리스마 있는 사람입니다. 날카로운 판단력으로 사람들을 압도하고, 목표를 향해 나아가는 힘이 강합니다.",
        "대인관계": "존경을 받지만 차갑게 보일 수 있어, 따뜻한 소통이 필요합니다.",
        "현재": "집중력이 강해져 원하는 바를 이룰 수 있는 시기입니다. 기회가 오면 놓치지 말아야 합니다.",
        "미래": "권위와 명예를 얻으며, 사람들에게 강렬한 인상을 남기는 인물이 됩니다.",
        "웹툰캐릭터": "강력한 라이벌. 냉철하면서도 누구보다도 뜨거운 내면을 가진 카리스마 있는 캐릭터."
    },
    "수": {
        "성격": "당신은 깊은 지혜와 직관을 지닌 사람입니다. 상황에 유연하게 대처하며 신비로운 매력을 발산합니다.",
        "대인관계": "타인의 마음을 이해하고 공감하며, 보이지 않는 힘으로 사람들을 끌어당깁니다.",
        "현재": "직관이 번뜩이며 새로운 아이디어와 통찰이 떠오르는 시기입니다.",
        "미래": "지혜를 바탕으로 특별한 길을 걸어가며, 신비로운 존재로 기억될 것입니다.",
        "웹툰캐릭터": "비밀을 간직한 현자. 주인공에게 신비로운 힘을 전해주는 인물."
    }
}

# -------------------- 결과 계산 --------------------
if submitted:
    year, month, day, hour = birth_date.year, birth_date.month, birth_date.day, birth_time.hour
    year_stem, year_branch = heavenly_stems[year % 10], earthly_branches[year % 12]
    month_stem, month_branch = heavenly_stems[month % 10], earthly_branches[month % 12]
    day_stem, day_branch = heavenly_stems[day % 10], earthly_branches[day % 12]
    hour_stem, hour_branch = heavenly_stems[hour % 10], earthly_branches[hour % 12]

    # 오행 추출
    elements = [s[-2] for s in [year_stem, month_stem, day_stem, hour_stem]]
    main_element = max(set(elements), key=elements.count)
    report = element_report.get(main_element, element_report["토"])

    # -------------------- 출력 --------------------
    st.markdown(
        f"""
        <div class="result-box">
            <h2>🔮 {name}님의 웹툰 캐릭터 리포트</h2>
            <p><b>성별:</b> {gender}</p>
            <p><b>생년월일:</b> {birth_date.strftime('%Y-%m-%d')}</p>
            <p><b>출생시각:</b> {birth_time.strftime('%H:%M')}</p>
            <hr>
            <p><b>사주팔자:</b><br>
               {year_stem} {year_branch} / {month_stem} {month_branch} / {day_stem} {day_branch} / {hour_stem} {hour_branch}
            </p>
            <hr>
            <h3>🌟 성격</h3>
            <p>{report['성격']}</p>
            <h3>🤝 대인관계</h3>
            <p>{report['대인관계']}</p>
            <h3>📍 현재 운세</h3>
            <p>{report['현재']}</p>
            <h3>🔮 미래 운세</h3>
            <p>{report['미래']}</p>
            <h3>📖 웹툰 캐릭터 해석</h3>
            <p>{report['웹툰캐릭터']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
