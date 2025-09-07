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

# -------------------- 판타지 웹툰식 사주풀이 --------------------
element_report = {
    "목":{
        "성격":"당신은 모험을 사랑하는 주인공, 언제나 새로운 세계로 뛰어드는 용기 있는 인물이다!",
        "연애":"동료들과 함께하는 여정 속에서 마음을 나누며, 사랑의 전투를 즐기리라!",
        "재물":"탐험 속에서 얻는 보물과 경험이 재물과 지혜를 함께 가져다주리라!",
        "현재":"이 순간, 새로운 시련과 도전이 당신을 기다리니, 활력을 폭발시키라!",
        "미래":"장차 전설이 될 모험을 거쳐 지도자 혹은 영웅으로 성장하리라!",
        "웹툰":"빛나는 검을 든 모험가, 위험 속에서도 결코 물러서지 않는 주인공!"
    },
    "화":{
        "성격":"불꽃같은 추진력으로 모든 적과 난관을 태워버리는 전사형 캐릭터!",
        "연애":"강렬한 동료애와 연애가 뒤섞여, 이야기의 중심에서 사랑을 쟁취하리라!",
        "재물":"창의적 전략과 모험으로 보물을 쟁취하며 재물운을 끌어올리리라!",
        "현재":"모든 갈등과 전투 속에서 당신의 힘이 빛나는 시기!",
        "미래":"전장을 지배하고 강력한 영웅으로 이름을 남기리라!",
        "웹툰":"폭풍을 몰고 오는 불꽃 전사, 액션의 중심에서 모든 갈등을 주도하는 캐릭터!"
    },
    "토":{
        "성격":"튼튼한 방패를 든 조력자, 주인공이 어려움에 처할 때 언제나 곁에 있는 인물!",
        "연애":"안정된 사랑과 우정을 이어가며, 팀을 단단하게 결속시키리라!",
        "재물":"꾸준한 노력으로 금전적 안정과 모험 속 보상을 얻으리라!",
        "현재":"팀과 함께 목표를 달성하며 안정적 진전을 이룰 시기!",
        "미래":"믿음직한 조력자, 전략가로서 전설 속에 남으리라!",
        "웹툰":"주인공을 든든히 받쳐주는 멘토형 캐릭터, 지혜와 힘의 조화!"
    },
    "금":{
        "성격":"칼날처럼 날카로운 지혜와 결단력, 라이벌 혹은 지도자로서 빛나리라!",
        "연애":"상대에게 강렬한 인상을 남기며, 냉철한 매력을 발산하리라!",
        "재물":"전략과 권위를 활용하여 재물을 쟁취하리라!",
        "현재":"적과 동료를 분석하며 전략을 세우는 시기!",
        "미래":"영웅적 라이벌로 성장하며 이야기의 큰 전환점에 서리라!",
        "웹툰":"강력한 라이벌, 카리스마와 지혜를 겸비한 캐릭터!"
    },
    "수":{
        "성격":"신비로운 마법사, 숨겨진 능력과 통찰력으로 운명을 조율하리라!",
        "연애":"조용히 마음을 나누며, 비밀스러운 매력으로 동료를 이끌리라!",
        "재물":"숨겨진 지식과 전략으로 보물과 운을 얻으리라!",
        "현재":"신비로운 힘이 깨어나는 시기, 계획과 직관을 발휘하라!",
        "미래":"전설적인 현자로 성장하며, 이야기의 흐름을 바꾸리라!",
        "웹툰":"비밀을 간직한 현자, 스토리의 핵심에서 운명을 좌우하는 캐릭터!"
    }
}

# -------------------- 무지개 색상 효과 --------------------
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
