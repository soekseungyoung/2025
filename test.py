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
    font-size: 18px;
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
st.write("✨ 판타지 세계 속, 황금빛 사주풀이로 너의 운명을 확인하거라 ✨")

# -------------------- 입력 --------------------
with st.form("user_form"):
    name = st.text_input("이름을 입력하거라")
    gender = st.radio("성별을 선택하거라", ["여자", "남자"])
    birth_date = st.date_input("생년월일을 입력하거라", min_value=datetime(1900,1,1), max_value=datetime.today())
    submitted = st.form_submit_button("결과 보기")

# -------------------- 천간/지지 --------------------
heavenly_stems = ["갑","을","병","정","무","기","경","신","임","계"]
earthly_branches = ["자","축","인","묘","진","사","오","미","신","유","술","해"]
stem_to_element = {"갑":"목","을":"목","병":"화","정":"화","무":"토","기":"토","경":"금","신":"금","임":"수","계":"수"}

# -------------------- 판타지 웹툰형 사주 리포트 --------------------
element_report = {
    "목":{
        "성격":"너는 끊임없이 성장과 탐험을 추구하는구나. 낯선 길도 두려워하지 말고, 새로운 세상을 열어 주변에 영감을 주거라.",
        "연애":"연애에서는 자유롭고 솔직함을 잃지 말거라. 상대와 새로운 경험을 만들며 진심을 나누거라.",
        "재물":"계획과 끈기로 안정적인 재물운을 쌓거라. 노력 끝에 얻는 보상은 반드시 네 것이 될 것이니라.",
        "현재":"지금 중요한 도전의 길목에 서 있구나. 시련을 피하지 말고 성장의 발판으로 삼거라.",
        "미래":"앞으로 큰 성취를 이루어 지도자의 길을 걷거나 새로운 세상을 개척하는 인물이 되거라.",
        "웹툰":"이야기 속 모험가 주인공으로 등장하여, 주변에 활력을 불어넣는 핵심 캐릭터가 되거라."
    },
    "화":{
        "성격":"열정과 추진력이 강하구나. 행동력으로 상황을 장악하고 리더십을 발휘하거라.",
        "연애":"사랑에 진심을 다하거라. 강렬한 인상을 남기지만 감정 기복에 주의하거라.",
        "재물":"도전과 창의성으로 재물을 얻거라. 기회를 포착함이 네 무기라.",
        "현재":"목표를 향해 힘차게 나아가거라. 강한 에너지가 너를 지탱할 것이니라.",
        "미래":"큰 성공을 거둘 수 있으나 조급함을 다스리거라. 안정된 성취가 뒤따르리니라.",
        "웹툰":"불꽃 전사로 등장하여 갈등의 중심에서 서사를 이끌거라."
    },
    "토":{
        "성격":"안정적이고 성실한구나. 신뢰받는 조력자가 되거라.",
        "연애":"사랑에서는 진중하게, 안정적 관계를 추구하거라. 함께 성장하는 사랑을 이상으로 삼거라.",
        "재물":"꾸준히 노력하여 재물운을 쌓거라. 장기적인 안정을 추구하거라.",
        "현재":"지금은 성실함과 책임감이 인정받는 시기라.",
        "미래":"존경받는 조언자, 든든한 조력자로 남을 가능성이 크구나.",
        "웹툰":"주인공을 지탱하는 멘토형 캐릭터로, 신뢰와 지혜를 상징하거라."
    },
    "금":{
        "성격":"명확한 목표와 결단력을 지니고 있구나. 냉철한 판단과 카리스마를 잃지 말거라.",
        "연애":"다소 차갑게 보일 수 있으나, 깊은 신뢰와 책임을 중시하거라.",
        "재물":"전략적 사고로 재물을 끌어올리거라. 권위와 명예를 기대하거라.",
        "현재":"결단과 집중이 필요한 시기임을 명심하거라.",
        "미래":"중요한 순간에 영향력을 발휘하며 강렬한 존재로 남거라.",
        "웹툰":"카리스마 있는 라이벌 캐릭터로 등장해, 주인공의 성장을 이끌거라."
    },
    "수":{
        "성격":"지혜롭고 직관이 뛰어나구나. 신비로움이 네 매력이 되거라.",
        "연애":"상대의 마음을 깊이 이해하고, 조용히 끌어당기는 매력을 잃지 말거라.",
        "재물":"현명한 판단으로 재물운을 얻고, 기회를 놓치지 말거라.",
        "현재":"통찰과 창의력이 필요한 시기임을 명심하거라.",
        "미래":"독창적인 성취를 이루며 특별한 길을 걷거라.",
        "웹툰":"비밀을 가진 현자로 등장해, 서사 흐름의 중요한 지점을 지휘하거라."
    }
}

# -------------------- 랜덤 컬러 --------------------
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
effect_color = random.choice(colors)

# -------------------- 결과 계산 및 출력 --------------------
if submitted:
    year, month, day = birth_date.year, birth_date.month, birth_date.day

    # 연주
    year_stem = heavenly_stems[(year-4)%10]
    year_branch = earthly_branches[(year-4)%12]

    # 월주
    month_stem = heavenly_stems[(year + month)%10]
    month_branch = earthly_branches[(month+1)%12]

    # 일주
    day_stem = heavenly_stems[(year + month + day)%10]
    day_branch = earthly_branches[(day+2)%12]

    # 오행
    element = stem_to_element[day_stem]
    report = element_report[element]

    # -------------------- 음악 --------------------
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    # -------------------- 리포트 출력 --------------------
    st.markdown(f"""
    <div class="report" style="border-color:{effect_color}; box-shadow:0 0 40px {effect_color};">
        <h3>🌌 {name}의 판타지 웹툰 사주 리포트 🌌</h3>
        <p><b>사주:</b> {year_stem}{year_branch}년, {month_stem}{month_branch}월, {day_stem}{day_branch}일</p>
        <hr>
        <p><b>성격:</b> {report['성격']}</p>
        <p><b>연애:</b> {report['연애']}</p>
        <p><b>재물:</b> {report['재물']}</p>
        <p><b>현재:</b> {report['현재']}</p>
        <p><b>미래:</b> {report['미래']}</p>
        <p><b>웹툰 캐릭터:</b> {report['웹툰']}</p>
    </div>
    """, unsafe_allow_html=True)
