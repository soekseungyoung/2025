import streamlit as st
from datetime import datetime

st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #0a0a0a;
    font-family: 'Arial', sans-serif;
    position: relative;
    overflow: hidden;
    color: #FFD700;
}
.title {
    font-size: 48px;
    text-align: center;
    margin-top: 20px;
    font-weight: bold;
    color: #FFD700;
    text-shadow: 0 0 20px #FFD700;
    position: relative;
    z-index: 2;
}
.report {
    background: rgba(30,30,30,0.95);
    border: 2px solid #FFD700;
    border-radius: 15px;
    padding: 30px;
    margin-top: 30px;
    line-height: 1.8;
    box-shadow: 0 0 25px rgba(255,215,0,0.5);
    position: relative;
    z-index: 2;
}
.report h3 {
    color: #FFD700;
    text-shadow: 0 0 10px #FFD700;
}
hr {
    border: 1px solid #FFD700;
}

/* 불꽃 효과 */
.fire {
    position: fixed;
    top: 0;
    width: 50px;
    height: 100%;
    background: linear-gradient(to top, rgba(255,140,0,0.7), rgba(255,69,0,0.0));
    z-index: 1; /* 리포트 위로 안 올라오도록 */
}
.fire.right { right: 0; }
.fire.left { left: 0; }
</style>

<div class="fire left"></div>
<div class="fire right"></div>
""", unsafe_allow_html=True)

st.markdown('<div class="title">내가 웹툰에 들어간다면?</div>', unsafe_allow_html=True)
st.write("✨ 판타지 세계 속, 황금빛 사주풀이로 운명을 확인하라! ✨")

with st.form("user_form"):
    name = st.text_input("이름을 입력하세요")
    gender = st.radio("성별을 선택하세요", ["여자", "남자"])
    birth_date = st.date_input("생년월일", min_value=datetime(1900,1,1), max_value=datetime.today())
    submitted = st.form_submit_button("결과 보기")

heavenly_stems = ["갑","을","병","정","무","기","경","신","임","계"]
earthly_branches = ["자","축","인","묘","진","사","오","미","신","유","술","해"]
stem_to_element = {"갑":"목","을":"목","병":"화","정":"화","무":"토","기":"토","경":"금","신":"금","임":"수","계":"수"}

element_report = {
    "목":{"성격":"끊임없는 도전과 탐험을 추구하는 인물이로다. 새로운 지식과 세계를 개척하며, 동료들에게 희망을 불어넣으리라!",
          "연애":"자유롭고 열정적인 사랑을 즐기리니, 상대에게 신선한 충격과 활력을 선사하리라!",
          "재물":"계획적 노력과 꾸준함으로 재물운이 안정되리라. 새로운 기회가 찾아오면 척척 쟁취하리라!",
          "현재":"지금은 시련과 기회가 동시에 다가오는 시기이니, 능력을 시험하고 성장할 때이니라!",
          "미래":"장차 큰 성취를 이루고, 지도자적 위치에 서거나 새로운 영역을 개척할 것이니라!",
          "웹툰":"모험가, 도전적인 주인공으로 주변에 활력을 불어넣는 캐릭터이리라!"}
    # (다른 오행도 동일한 구조로 추가)
}

if submitted:
    year, month, day = birth_date.year, birth_date.month, birth_date.day
    year_stem = heavenly_stems[(year-4)%10]
    year_branch = earthly_branches[(year-4)%12]
    month_stem = heavenly_stems[(year + month)%10]
    month_branch = earthly_branches[(month+1)%12]
    day_stem = heavenly_stems[(year + month + day)%10]
    day_branch = earthly_branches[(year + month + day)%12]
    day_element = stem_to_element[day_stem]
    report = element_report[day_element]

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
