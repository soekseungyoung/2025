import streamlit as st
from datetime import datetime

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

# -------------------- 스타일 --------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8e1f4, #e1f0ff, #fcefe3);
        font-family: "Nanum Gothic", sans-serif;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #222;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
    }
    .result-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.25);
        margin-top: 30px;
    }
    h2, h3 {
        color: #ff4081;
    }
    p {
        font-size: 16px;
        line-height: 1.7;
    }
    hr {
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- 제목 --------------------
st.markdown('<div class="title">내가 웹툰에 들어간다면?</div>', unsafe_allow_html=True)
st.write("✨ 사주를 기반으로 당신의 웹툰 캐릭터 운명을 풀어드립니다! ✨")

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

# 오행별 상세 리포트
element_report = {
    "목": {
        "성격": "당신은 끊임없이 성장과 발전을 추구하며, 새로운 아이디어와 창의력을 발휘하는 인물입니다. 성실하면서도 자유로운 기질을 지녔습니다.",
        "대인관계": "주변 사람들에게 영감을 주는 존재이며, 리더십을 발휘할 때 더욱 빛납니다. 하지만 고집이 강해 갈등이 생기기도 합니다.",
        "현재": "지금은 새로운 기회를 찾는 시기로, 도전적인 에너지가 강하게 흐르고 있습니다. 주변이 당신의 활발한 움직임에 주목하고 있습니다.",
        "미래": "앞으로는 노력과 도전이 결실을 맺어 큰 성취를 이룰 것입니다. 다만 성급함을 조절한다면 더 큰 안정과 성공을 얻을 수 있습니다.",
        "웹툰캐릭터": "웹툰 속에서는 끊임없이 전진하는 모험가이자, 새로운 세계를 개척하는 주인공으로 등장합니다."
    },
    "화": {
        "성격": "열정과 추진력이 강하며, 감정 표현이 솔직하고 카리스마 넘치는 인물입니다. 사람들을 끌어당기는 매력을 지녔습니다.",
        "대인관계": "친구나 동료들에게 활력소 같은 존재지만, 때로는 과열된 감정으로 갈등이 생길 수 있습니다.",
        "현재": "지금은 당신의 열정이 주변에 강한 영향을 미치는 시기입니다. 노력한 만큼 결과가 빠르게 나타납니다.",
        "미래": "앞으로는 당신의 에너지가 큰 성과를 이루게 하지만, 조급함을 다스려야 장기적인 성취가 가능합니다.",
        "웹툰캐릭터": "웹툰 속에서는 불꽃 같은 전사, 혹은 카리스마 넘치는 액션 주인공으로 묘사됩니다."
    },
    "토": {
        "성격": "안정적이고 든든하며 책임감이 강한 인물입니다. 차분하고 신뢰할 수 있는 성격으로 주위의 존경을 받습니다.",
        "대인관계": "사람들을 편안하게 만드는 능력이 있으며, 어려움 속에서도 버팀목이 되어줍니다.",
        "현재": "지금은 안정과 성실이 강조되는 시기입니다. 당신의 꾸준함이 인정을 받고 있습니다.",
        "미래": "앞으로는 믿음직한 조언자나 지도자로 성장하며, 오랫동안 존경받는 인물이 될 것입니다.",
        "웹툰캐릭터": "웹툰 속에서는 든든한 조력자이자, 지혜로운 멘토로서 주인공을 이끄는 역할을 합니다."
    },
    "금": {
        "성격": "강한 의지와 결단력을 지녔으며, 냉철하면서도 카리스마 있는 인물입니다. 목표를 향해 흔들림 없이 나아갑니다.",
        "대인관계": "사람들에게 존경을 받지만, 때로는 차갑고 거리를 두는 모습으로 오해를 사기도 합니다.",
        "현재": "지금은 집중력과 추진력이 강해, 원하는 목표를 성취하기 좋은 시기입니다.",
        "미래": "앞으로는 권위와 명예를 얻으며, 강렬한 인상을 남기는 인물이 될 것입니다.",
        "웹툰캐릭터": "웹툰 속에서는 주인공의 강력한 라이벌이자, 매혹적인 카리스마 캐릭터로 등장합니다."
    },
    "수": {
        "성격": "지혜롭고 신비로운 기질을 가진 인물입니다. 감각적이고 직관력이 뛰어나며, 상황에 따라 유연하게 변화합니다.",
        "대인관계": "타인의 마음을 잘 이해하고, 신비로운 매력으로 주변을 끌어당깁니다.",
        "현재": "지금은 직관과 감각이 빛나는 시기입니다. 새로운 아이디어와 통찰이 떠오릅니다.",
        "미래": "앞으로는 지혜를 바탕으로 어려운 상황을 극복하며, 특별한 인생을 만들어갑니다.",
        "웹툰캐릭터": "웹툰 속에서는 비밀을 간직한 신비로운 인물, 또는 주인공을 돕는 현자 같은 캐릭터로 등장합니다."
    }
}

# -------------------- 결과 계산 --------------------
if submitted:
    # 1. 사주 → 천간/지지
    year = birth_date.year
    month = birth_date.month
    day = birth_date.day
    hour = birth_time.hour

    year_stem = heavenly_stems[year % 10]
    year_branch = earthly_branches[year % 12]
    month_stem = heavenly_stems[month % 10]
    month_branch = earthly_branches[month % 12]
    day_stem = heavenly_stems[day % 10]
    day_branch = earthly_branches[day % 12]
    hour_stem = heavenly_stems[hour % 10]
    hour_branch = earthly_branches[hour % 12]

    # 2. 오행 추출 → 주요 성향 결정
    elements = [s[-2] for s in [year_stem, month_stem, day_stem, hour_stem]]
    main_element = max(set(elements), key=elements.count)

    report = element_report.get(main_element, {
        "성격": "독창적이고 개성 있는 성격을 지녔습니다.",
        "대인관계": "특별한 인연을 만들어내는 힘이 있습니다.",
        "현재": "지금은 변화를 앞두고 있는 중요한 시점입니다.",
        "미래": "앞으로 당신의 길은 특별하고 독창적으로 펼쳐집니다.",
        "웹툰캐릭터": "웹툰 속에서는 개성 강한 독특한 캐릭터로 등장합니다."
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
            <h3>🌟 성격 (본성)</h3>
            <p>{report['성격']}</p>
            <h3>🤝 대인관계 (인연)</h3>
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
