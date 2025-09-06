import streamlit as st
from datetime import datetime

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

# -------------------- 스타일 --------------------
st.markdown(
    """
    <style>
    /* stApp 배경에 별자리 애니메이션 추가 */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: black;
        z-index: -2;
    }

    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 1px;
        height: 1px;
        background: transparent;
        box-shadow: 
            100px 200px #FFD700, 
            300px 600px #FFD700,
            700px 150px #FFD700,
            900px 400px #FFD700,
            1200px 250px #FFD700,
            500px 800px #FFD700,
            1300px 700px #FFD700;
        animation: animStar 50s linear infinite;
        z-index: -1;
    }

    .stars:after {
        content: " ";
        position: absolute;
        top: 2000px;
        width: 1px;
        height: 1px;
        background: transparent;
        box-shadow: 
            100px 200px #FFD700, 
            300px 600px #FFD700,
            700px 150px #FFD700,
            900px 400px #FFD700,
            1200px 250px #FFD700,
            500px 800px #FFD700,
            1300px 700px #FFD700;
    }

    @keyframes animStar {
        from { transform: translateY(0px); }
        to { transform: translateY(-2000px); }
    }

    /* 제목 */
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 25px;
        color: #FFD700;
        text-shadow: 0px 0px 15px rgba(255,215,0,0.9), 0px 0px 30px rgba(255,215,0,0.7);
    }

    /* 결과 박스 */
    .result-box {
        background: rgba(20,20,20,0.85);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #FFD700;
        box-shadow: 0px 0px 20px rgba(255,215,0,0.6);
        margin-top: 30px;
    }

    h2, h3 {
        color: #FFD700;
        text-shadow: 0px 0px 6px rgba(255,215,0,0.7);
    }

    p {
        font-size: 16px;
        line-height: 1.8;
        color: #f5f5dc;
    }

    hr {
        border: 1px solid #FFD700;
        margin: 20px 0;
    }

    .stRadio label {
        color: #FFD700 !important;
    }
    </style>

    <div class="stars"></div>
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

# 오행별 상세 리포트
element_report = {
    "목": {"성격": "끊임없는 성장과 도전을 추구하는 타입. 웹툰 속에서는 늘 새로운 세계를 개척하는 인물입니다.",
          "대인관계": "주변에 활력을 주고 리더십을 발휘하지만, 고집이 강할 수 있습니다.",
          "현재": "새로운 기회가 다가오고 있으며, 모험심이 강하게 발휘되는 시기입니다.",
          "미래": "큰 성취를 이루고 지도자적 위치에 설 가능성이 큽니다.",
          "웹툰캐릭터": "웹툰 속 모험가, 도전적인 주인공"},
    "화": {"성격": "열정과 추진력이 강한 타입. 카리스마가 넘치며 감정에 솔직합니다.",
          "대인관계": "사람들에게 활력을 주지만 때로는 과열된 감정으로 갈등이 생길 수 있습니다.",
          "현재": "불꽃 같은 에너지로 원하는 것을 향해 돌진하는 시기입니다.",
          "미래": "큰 성공을 이루지만 조급함을 다스려야 합니다.",
          "웹툰캐릭터": "불꽃 전사, 액션의 중심 인물"},
    "토": {"성격": "안정적이고 든든한 타입. 성실하고 믿음을 주는 성격입니다.",
          "대인관계": "사람들을 편안하게 만들며 버팀목이 되어줍니다.",
          "현재": "성실함이 인정받고 있으며 안정적인 흐름이 이어지고 있습니다.",
          "미래": "오랫동안 존경받는 조언자나 멘토가 될 수 있습니다.",
          "웹툰캐릭터": "지혜로운 조력자, 든든한 멘토"},
    "금": {"성격": "냉철하고 결단력 있는 타입. 카리스마와 강한 의지를 가졌습니다.",
          "대인관계": "존경을 받지만 차갑게 보일 수 있습니다.",
          "현재": "목표를 향해 집중할 수 있는 시기입니다.",
          "미래": "권위와 명예를 얻으며 강렬한 인상을 남깁니다.",
          "웹툰캐릭터": "강력한 라이벌, 카리스마 캐릭터"},
    "수": {"성격": "지혜롭고 신비로운 타입. 직관력이 뛰어나며 상황에 유연합니다.",
          "대인관계": "타인의 마음을 이해하며 신비로운 매력으로 이끕니다.",
          "현재": "직관이 빛나고 새로운 아이디어가 떠오르는 시기입니다.",
          "미래": "지혜를 바탕으로 특별한 길을 걸어갑니다.",
          "웹툰캐릭터": "비밀을 간직한 현자, 신비로운 인물"}
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
        "성격": "독창적이고 개성 있는 성격을 지녔습니다.",
        "대인관계": "특별한 인연을 만들어내는 힘이 있습니다.",
        "현재": "지금은 변화를 앞두고 있는 중요한 시점입니다.",
        "미래": "앞으로 당신의 길은 특별하고 독창적으로 펼쳐집니다.",
        "웹툰캐릭터": "개성 강한 독특한 캐릭터"
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
