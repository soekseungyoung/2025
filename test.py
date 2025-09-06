import streamlit as st
from datetime import datetime
import random

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="🌟", layout="centered")

# -------------------- 별 생성 --------------------
# 100개 별 무작위 위치 & 속성
stars_html = ""
for i in range(100):
    left = random.randint(0, 100)   # 화면 가로 %
    size = random.choice([1, 2, 3]) # 별 크기
    duration = random.randint(10, 25) # 애니메이션 시간
    delay = random.randint(0, 20)   # 딜레이
    stars_html += f'<div class="star" style="left:{left}%; width:{size}px; height:{size}px; animation-duration:{duration}s; animation-delay:{delay}s;"></div>\n'

# -------------------- 스타일 --------------------
st.markdown(
    f"""
    <style>
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

    /* 별 하나 */
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

    hr {{
        border: 1px solid #FFD700;
        margin: 20px 0;
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
st.write("✨ 별빛과 황금빛으로 완성된 사주풀이, 당신이 웹툰 속에서 어떤 캐릭터로 살아갈지 알려드립니다 ✨")

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

# 오행별 상세 리포트 (문장 확장)
element_report = {
    "목": {
        "성격": "당신은 성장과 확장을 상징하는 기운을 타고난 사람입니다. 끊임없이 배우고 도전하며, 틀에 갇히기를 거부합니다. 웹툰 속에서라면 언제나 새로운 세계를 열고, 독자들에게 변화를 상징하는 인물로 그려질 것입니다.",
        "대인관계": "당신은 사람들에게 신선한 자극과 동기를 부여합니다. 그러나 때로는 자신의 고집과 확고한 주장이 갈등을 일으킬 수 있습니다. 하지만 결과적으로 사람들은 당신의 열정을 인정하고 따르게 될 것입니다.",
        "현재": "지금은 성장의 에너지가 강하게 작동하는 시기입니다. 새로운 기회가 다가오고 있으며, 그 안에서 당신의 모험심이 발휘됩니다.",
        "미래": "앞으로 당신은 지도자적 위치에 서서 사람들을 이끌 가능성이 큽니다. 당신의 이야기는 끝없는 도전과 성취로 채워질 것입니다.",
        "웹툰캐릭터": "웹툰 속에서 당신은 미지의 세계로 발을 내딛는 모험가이자, 늘 새로운 가능성을 탐색하는 도전적인 주인공입니다."
    },
    "화": {
        "성격": "불꽃처럼 뜨겁고 에너지가 넘치는 사람입니다. 추진력이 강하고 감정에 솔직해, 어떤 상황에서도 자신을 드러내는 데 주저하지 않습니다. 사람들에게는 카리스마와 강렬한 인상을 남기는 인물로 다가갑니다.",
        "대인관계": "당신은 주변 사람들에게 활력을 불어넣습니다. 하지만 때로는 지나친 열정이 갈등을 불러일으킬 수 있습니다. 그럼에도 불구하고 사람들은 당신의 진심 어린 열정에 감동받습니다.",
        "현재": "현재 당신은 불꽃처럼 타오르는 시기를 보내고 있습니다. 원하는 것을 향해 곧바로 달려가는 기세가 대단합니다.",
        "미래": "앞으로 당신은 커다란 성공을 거둘 수 있으나, 조급함을 다스린다면 더욱 오래 지속되는 성취를 누릴 수 있습니다.",
        "웹툰캐릭터": "웹툰 속에서 당신은 전장을 불태우는 전사이자, 액션과 드라마의 중심에 선 주인공으로 표현됩니다."
    },
    "토": {
        "성격": "흔들림 없는 안정감을 가진 사람입니다. 성실하고 든든하며, 언제나 중심을 잡아주는 역할을 합니다. 사람들이 의지할 수 있는 묵직한 기둥 같은 존재로 그려집니다.",
        "대인관계": "당신은 언제나 사람들에게 신뢰와 안정감을 줍니다. 다소 느리게 보일 수 있으나, 당신이 있기에 다른 사람들이 안심하고 움직일 수 있습니다.",
        "현재": "지금은 당신의 성실함이 빛을 발하는 시기입니다. 차분한 태도로 꾸준히 나아가는 모습이 인정받습니다.",
        "미래": "앞으로 당신은 존경받는 조언자나 멘토로서 오랫동안 영향력을 발휘할 수 있습니다.",
        "웹툰캐릭터": "웹툰 속에서 당신은 주인공 곁을 지켜주는 현명한 조력자, 또는 모두에게 안정감을 주는 든든한 멘토로 표현됩니다."
    },
    "금": {
        "성격": "당신은 단단하고 결단력 있는 기운을 타고났습니다. 냉철한 판단력과 강한 의지를 바탕으로, 자신이 세운 목표를 향해 흔들림 없이 나아갑니다.",
        "대인관계": "당신은 존경을 받지만, 차갑게 느껴질 수 있습니다. 그러나 진정으로 가까워진 이들은 당신의 강인함 속 따뜻함을 발견하게 됩니다.",
        "현재": "지금은 목표에 집중하고 결단을 내릴 시기입니다. 흔들림 없는 자세가 주위에 큰 울림을 줍니다.",
        "미래": "앞으로 당신은 권위와 명예를 얻으며, 강렬한 인상을 남기는 인물이 될 것입니다.",
        "웹툰캐릭터": "웹툰 속에서 당신은 주인공의 강력한 라이벌, 또는 스토리를 이끄는 카리스마 넘치는 인물로 등장합니다."
    },
    "수": {
        "성격": "당신은 지혜롭고 신비로운 사람입니다. 직관력이 뛰어나고, 상황에 따라 부드럽게 흘러가는 유연성을 지녔습니다. 사람들에게는 쉽게 이해할 수 없는 매력으로 다가옵니다.",
        "대인관계": "당신은 타인의 마음을 깊이 이해하며, 마치 비밀을 간직한 듯한 신비로운 분위기로 사람들을 끌어당깁니다.",
        "현재": "지금은 직관과 감각이 빛나는 시기입니다. 새로운 아이디어와 영감이 떠올라 당신을 이끌고 있습니다.",
        "미래": "앞으로 당신은 지혜를 바탕으로 특별한 길을 걸어갈 것입니다. 다른 이들과는 다른 독특한 운명을 써 내려갑니다.",
        "웹툰캐릭터": "웹툰 속에서 당신은 비밀을 간직한 현자, 신비로운 기운을 뿜어내는 인물로 표현됩니다."
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
    report = element_report.get(main_element, {
        "성격": "당신은 독창적이고 개성 있는 성격을 지녔습니다.",
        "대인관계": "사람들과 특별한 인연을 만들어내는 힘이 있습니다.",
        "현재": "지금은 중요한 전환점에 서 있으며, 변화가 다가오고 있습니다.",
        "미래": "앞으로의 길은 특별하고 독창적인 방식으로 펼쳐질 것입니다.",
        "웹툰캐릭터": "웹툰 속에서 당신은 독특하고 개성 강한 캐릭터입니다."
    })

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
