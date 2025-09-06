import streamlit as st
from datetime import datetime

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
st.write("✨ 웅장한 판타지 세계 속, 황금빛 사주풀이로 당신의 운명을 확인하라! ✨")

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

# -------------------- 판타지 스타일 사주풀이 --------------------
element_report = {
    "목":{
        "성격":"끊임없는 도전과 탐험을 추구하는 인물이로다. 새로운 지식과 세계를 개척하며, 동료들에게 희망을 불어넣으리라!",
        "연애":"자유롭고 열정적인 사랑을 즐기리니, 상대에게 신선한 충격과 활력을 선사하리라. 구속은 결코 참지 못할 것이니라!",
        "재물":"계획적 노력과 꾸준함으로 재물운이 안정되리라. 새로운 기회가 찾아오면 척척 쟁취하리라!",
        "현재":"지금은 시련과 기회가 동시에 다가오는 시기이니, 능력을 시험하고 성장할 때이니라!",
        "미래":"장차 큰 성취를 이루고, 지도자적 위치에 서거나 새로운 영역을 개척할 것이니라!",
        "웹툰":"모험가, 도전적인 주인공으로 주변에 활력을 불어넣는 캐릭터이리라!"
    },
    "화":{
        "성격":"열정과 추진력이 폭발하는 자여, 감정을 솔직히 드러내며 카리스마를 뿜어내리라!",
        "연애":"강렬하고 불꽃 같은 사랑을 즐기리니, 상대에게 깊은 인상을 남기리라!",
        "재물":"창의적 사업과 도전적 투자가 재물운을 상승시키리라. 기회를 놓치지 말 것이니라!",
        "현재":"목표를 향해 돌진할 시기이니, 에너지를 아낌없이 쏟으리라!",
        "미래":"큰 성공을 거두겠지만, 조급함을 다스려야 장기적 성취가 가능하리라!",
        "웹툰":"불꽃 전사, 액션의 중심에서 모든 갈등을 휘어잡는 캐릭터이리라!"
    },
    "토":{
        "성격":"안정적이고 든든한 자여, 주변에 신뢰를 주고 버팀목이 되리라!",
        "연애":"편안하고 안정적인 관계를 선호하니, 상대와 함께 성장하는 사랑을 이어가리라!",
        "재물":"꾸준한 노력과 성실함으로 재물운이 탄탄하리라. 장기적 안정성을 중시하리라!",
        "현재":"성실함이 인정받는 시기이니, 능력을 발휘하라!",
        "미래":"오랫동안 존경받는 조언자, 든든한 조력자가 되리라!",
        "웹툰":"지혜로운 조력자, 주인공을 든든히 받쳐주는 캐릭터이리라!"
    },
    "금":{
        "성격":"냉철하고 결단력 있는 자여, 목표를 명확히 하고 효율적으로 행동하리라!",
        "연애":"매력적이되 다소 차가워 보일지니, 상대에게 깊은 신뢰를 요구하리라!",
        "재물":"권위와 전략적 선택으로 재물운을 상승시키리라!",
        "현재":"집중과 결단이 필요한 시기이니, 전력을 다하라!",
        "미래":"중요한 위치에서 영향력을 발휘하고 강렬한 인상을 남기리라!",
        "웹툰":"강력한 라이벌, 카리스마 있는 지도자형 캐릭터이리라!"
    },
    "수":{
        "성격":"지혜롭고 신비로운 자여, 직관과 통찰로 운명을 읽으리라!",
        "연애":"상대의 마음을 꿰뚫어 보며 신비로운 매력으로 사람을 끌어당기리라!",
        "재물":"현명한 선택과 직관으로 재물운이 상승하리라!",
        "현재":"직관과 창의력이 폭발하는 시기이니, 새로운 아이디어를 펼치라!",
        "미래":"지혜와 경험으로 독창적 성취를 이루리라!",
        "웹툰":"비밀을 간직한 현자, 이야기의 핵심에서 운명을 좌우하는 캐릭터이리라!"
    }
}

# -------------------- 결과 계산 및 출력 --------------------
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
    day_branch = earthly_branches[(year + month + day)%12]

    # 오행 분석
    day_element = stem_to_element[day_stem]
    report = element_report[day_element]

    # 출력
    st.markdown(f"""
    <div class="report">
        <h3>🔮 {name}님의 판타지 웹툰형 사주 리포트</h3>
        <p><b>성별:</b> {gender}</p>
        <p><b>생년월일:</b> {birth_date.strftime('%Y-%m-%d')}</p>
        <hr>
        <p><b>사주팔자:</b><br>
           {year_stem}{year_branch} / {month_stem}{month_branch} / {day_stem}{day_branch}
        </p>
        <hr>
        <h3>🌟 성격</h3>
        <p>{report['성격']}</p>
        <h3>📍 현재 운세</h3>
        <p>{report['현재']}</p>
        <h3>🔮 미래 운세</h3>
        <p>{report['미래']}</p>
        <h3>💖 연애운</h3>
        <p>{report['연애']}</p>
        <h3>💰 재물운</h3>
        <p>{report['재물']}</p>
        <h3>📖 웹툰 캐릭터</h3>
        <p>{report['웹툰']}</p>
    </div>
    """, unsafe_allow_html=True)
