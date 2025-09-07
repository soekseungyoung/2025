import streamlit as st
from datetime import datetime
import random

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

# -------------------- CSS 스타일 --------------------
st.markdown("""
<style>
.stApp {
    background-color: #0a0a0a;
    color: #FFD700;
    font-family: 'Arial', sans-serif;
}
.title {
    font-size: 48px;
    text-align: center;
    margin-top: 20px;
    font-weight: bold;
    color: #FFD700;
    text-shadow: 0 0 20px #FFD700;
}
.report {
    background: rgba(20,20,20,0.95);
    border: 2px solid #FFD700;
    border-radius: 15px;
    padding: 30px;
    margin-top: 30px;
    line-height: 1.8;
    box-shadow: 0 0 25px rgba(255,215,0,0.5);
    font-size: 20px;
}
.report h3 {
    color: #FFD700;
    text-shadow: 0 0 10px #FFD700;
}
hr {
    border: 1px solid #FFD700;
}
</style>
""", unsafe_allow_html=True)

# -------------------- 제목 --------------------
st.markdown('<div class="title">내가 웹툰에 들어간다면?</div>', unsafe_allow_html=True)
st.write("✨ 판타지 세계 속, 황금빛 사주풀이로 당신의 운명을 확인하세요 ✨")

# -------------------- 입력 --------------------
with st.form("user_form"):
    name = st.text_input("이름을 입력하세요")
    gender = st.radio("성별을 선택하세요", ["여자", "남자"])
    birth_date = st.date_input("생년월일", min_value=datetime(1900,1,1), max_value=datetime.today())
    submitted = st.form_submit_button("결과 보기")

# -------------------- 천간/지지 --------------------
heavenly_stems = ["갑","을","병","정","무","기","경","신","임","계"]
earthly_branches = ["자","축","인","묘","진","사","오","미","신","유","술","해"]
stem_to_element = {"갑":"목","을":"목","병":"화","정":"화","무":"토","기":"토","경":"금","신":"금","임":"수","계":"수"}

# -------------------- 결과값 (주신 그대로) --------------------
element_report = {
    "목":{
        "성격":"당신은 끊임없이 성장과 탐험을 추구하는 인물입니다. 낯선 길을 두려워하지 않고, 새로운 세계를 열며 주변에 영감을 줍니다.",
        "연애":"연애에 있어 자유롭고 솔직합니다. 상대와 함께 새로운 경험을 만들고, 진심 어린 관계를 중시합니다.",
        "재물":"계획과 끈기를 바탕으로 안정적인 재물운을 만들어 갑니다. 노력 끝에 얻는 보상은 결코 헛되지 않을 것입니다.",
        "현재":"현재 당신은 중요한 도전의 길목에 서 있습니다. 배움과 시련이 함께 찾아오니, 이를 통해 성장하게 될 것입니다.",
        "미래":"앞으로 큰 성취를 이루어, 지도자의 길을 걷거나 새로운 세상을 개척할 인물로 남게 될 것입니다.",
        "웹툰":"이야기 속에서 모험가 주인공으로 등장하여, 주변에 활력을 불어넣는 핵심 캐릭터가 될 것입니다."
    },
    "화":{
        "성격":"열정과 추진력이 강한 성격으로, 행동력이 뛰어나며 상황에 따라 리더십을 발휘합니다.",
        "연애":"사랑에 있어 뜨겁고 진실하며, 상대에게 강렬한 인상을 남깁니다. 다만 감정의 기복이 갈등을 만들 수도 있습니다.",
        "재물":"도전적인 태도와 창의성으로 재물을 얻습니다. 기회를 빠르게 포착하는 능력이 강점입니다.",
        "현재":"목표를 향해 힘 있게 나아가야 할 시기입니다. 강한 에너지가 당신의 무기가 됩니다.",
        "미래":"큰 성공을 거두지만, 조급함을 다스린다면 더욱 안정된 성취를 이루게 됩니다.",
        "웹툰":"불꽃 같은 전사로 등장하여, 갈등의 중심에서 서사를 이끄는 캐릭터가 될 것입니다."
    },
    "토":{
        "성격":"안정적이고 성실한 성격으로, 신뢰받는 조력자가 되는 경우가 많습니다.",
        "연애":"사랑에 있어 진중하며 안정적인 관계를 추구합니다. 함께 성장하는 사랑을 이상으로 삼습니다.",
        "재물":"꾸준한 노력으로 재물운을 쌓아 올립니다. 장기적인 안정을 중시합니다.",
        "현재":"지금은 성실함과 책임감이 인정받는 시기입니다.",
        "미래":"앞으로는 존경받는 조언자, 든든한 조력자의 위치에 설 가능성이 큽니다.",
        "웹툰":"주인공을 지탱하는 멘토나 조력자 캐릭터로, 신뢰와 지혜를 상징하게 됩니다."
    },
    "금":{
        "성격":"명확한 목표와 결단력을 지닌 성격입니다. 냉철한 판단과 카리스마가 두드러집니다.",
        "연애":"사랑에 있어 다소 차갑게 보일 수 있으나, 깊은 신뢰와 책임을 중시합니다.",
        "재물":"전략적 사고로 재물운을 끌어올립니다. 권위와 명예를 얻게 될 가능성이 있습니다.",
        "현재":"지금은 결단과 집중이 필요한 시기입니다.",
        "미래":"중요한 순간에 영향력을 발휘하며 강렬한 존재로 남게 됩니다.",
        "웹툰":"카리스마 넘치는 라이벌 캐릭터로 등장해, 주인공의 성장을 이끄는 존재가 될 것입니다."
    },
    "수":{
        "성격":"지혜롭고 직관이 뛰어난 성격입니다. 신비로움이 당신의 매력이 됩니다.",
        "연애":"상대의 마음을 깊이 이해하며, 조용히 끌어당기는 매력이 있습니다.",
        "재물":"현명한 판단으로 재물운을 얻으며, 기회를 놓치지 않는 능력이 있습니다.",
        "현재":"지금은 통찰과 창의력이 필요한 시기입니다.",
        "미래":"앞으로 독창적인 성취를 이루며, 특별한 길을 걸을 가능성이 큽니다.",
        "웹툰":"비밀을 간직한 현자로서 등장해, 서사의 중요한 흐름을 이끄는 캐릭터가 될 것입니다."
    }
}

# -------------------- 무작위 색상 효과 --------------------
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
effect_color = random.choice(colors)

# -------------------- 결과 출력 --------------------
if submitted:
    year, month, day = birth_date.year, birth_date.month, birth_date.day

    # 연주
    year_stem = heavenly_stems[(year-4)%10]
    year_branch = earthly_branches[(year-4)%12]

    # 월주 (단순화)
    month_stem = heavenly_stems[(year + month)%10]
    month_branch = earthly_branches[(month+1)%12]

    # 일주 (단순화)
    day_stem = heavenly_stems[(year + month + day)%10]
    day_branch = earthly_branches[(day+2)%12]

    # 오행
    element = stem_to_element[day_stem]
    report = element_report[element]

    # -------------------- 리포트 출력 --------------------
    st.markdown(f"""
    <div class="report" style="border-color:{effect_color}; box-shadow:0 0 25px {effect_color};">
        <h3>🌌 {name}님의 판타지 사주 리포트 🌌</h3>
        <p><b>사주 구성:</b> {year_stem}{year_branch}년, {month_stem}{month_branch}월, {day_stem}{day_branch}일</p>
        <hr>
        <p><b>성격:</b> {report['성격']}</p>
        <p><b>연애:</b> {report['연애']}</p>
        <p><b>재물:</b> {report['재물']}</p>
        <p><b>현재:</b> {report['현재']}</p>
        <p><b>미래:</b> {report['미래']}</p>
        <p><b>웹툰 속 캐릭터:</b> {report['웹툰']}</p>
    </div>
    """, unsafe_allow_html=True)
