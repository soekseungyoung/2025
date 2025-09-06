import streamlit as st
from datetime import datetime

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="내가 웹툰에 들어간다면?", page_icon="📖", layout="centered")

# -------------------- CSS 배경 + 스타일 --------------------
st.markdown("""
<style>
.stApp {
    background-color: black;
    background-image: radial-gradient(circle, #FFD700 1px, transparent 1px);
    background-size: 20px 20px;
    color: #f5f5dc;
}
.title {
    font-size: 42px;
    color: #FFD700;
    text-align: center;
    margin-top: 30px;
    text-shadow: 0 0 15px #FFD700;
}
.report {
    position: relative;
    z-index: 1;
    background: rgba(20,20,20,0.85);
    border: 2px solid #FFD700;
    border-radius: 10px;
    padding: 25px;
    margin-top: 30px;
    font-size: 18px;
    line-height: 1.7;
    box-shadow: 0 0 20px rgba(255,215,0,0.5);
}
.report h3 {
    color: #FFD700;
    text-shadow: 0 0 6px #FFD700;
}
</style>
""", unsafe_allow_html=True)

# -------------------- 제목 --------------------
st.markdown('<h1 class="title">내가 웹툰에 들어간다면?</h1>', unsafe_allow_html=True)
st.write("✨ 황금빛 별이 반짝이는 실제 사주풀이로 당신의 웹툰 캐릭터 운명을 알려드립니다 ✨")

# -------------------- 입력폼 --------------------
with st.form("user_form"):
    name = st.text_input("이름을 입력하세요")
    gender = st.radio("성별을 선택하세요", ["여자", "남자"])
    birth_date = st.date_input("생년월일", min_value=datetime(1900,1,1), max_value=datetime.today())
    birth_time = st.time_input("출생 시간")
    submitted = st.form_submit_button("결과 보기")

# -------------------- 천간/지지 --------------------
heavenly_stems = ["갑","을","병","정","무","기","경","신","임","계"]
earthly_branches = ["자","축","인","묘","진","사","오","미","신","유","술","해"]
stem_to_element = {"갑":"목","을":"목","병":"화","정":"화","무":"토","기":"토","경":"금","신":"금","임":"수","계":"수"}

# -------------------- 사주풀이 --------------------
if submitted:
    year, month, day, hour = birth_date.year, birth_date.month, birth_date.day, birth_time.hour

    # 연주 (년주)
    year_stem = heavenly_stems[(year-4)%10]
    year_branch = earthly_branches[(year-4)%12]

    # 월주 계산 (단순화)
    month_stem = heavenly_stems[(year*12 + month + 3)%10]
    month_branch = earthly_branches[(month+1)%12]

    # 일주 계산 (단순화)
    day_stem = heavenly_stems[(year*365 + month*30 + day)%10]
    day_branch = earthly_branches[(year*365 + month*30 + day)%12]

    # 시주 계산
    hour_branch_index = (hour+1)//2 % 12
    hour_branch = earthly_branches[hour_branch_index]
    hour_stem = heavenly_stems[(hour_branch_index + day_stem.count(''))%10]

    # -------------------- 오행 분석 --------------------
    day_element = stem_to_element[day_stem]

    element_report = {
        "목":{"성격":"끊임없는 성장과 도전을 추구하는 타입. 모험과 개척을 즐깁니다.",
              "연애":"자유롭고 열정적인 연애를 즐깁니다.",
              "재물":"계획적 투자와 노력이 재물운으로 이어집니다.",
              "현재":"새로운 기회가 다가오는 시기입니다.",
              "미래":"큰 성취를 이루고 지도자적 위치에 설 가능성이 큽니다.",
              "웹툰":"모험가, 도전적인 주인공"},
        "화":{"성격":"열정과 추진력이 강하며, 감정에 솔직합니다.",
              "연애":"불꽃같은 연애를 하며 상대에게 강한 인상을 남깁니다.",
              "재물":"도전적 투자가 좋은 결과를 가져올 수 있습니다.",
              "현재":"원하는 목표를 향해 돌진하는 시기입니다.",
              "미래":"큰 성공을 이루지만 조급함을 다스려야 합니다.",
              "웹툰":"불꽃 전사, 액션의 중심 인물"},
        "토":{"성격":"안정적이며 성실합니다. 신뢰와 믿음을 줍니다.",
              "연애":"편안하고 안정적인 관계를 선호합니다.",
              "재물":"꾸준한 노력이 재물로 이어집니다.",
              "현재":"성실함이 인정받고 안정적인 흐름이 이어집니다.",
              "미래":"오랫동안 존경받는 조언자나 멘토가 될 수 있습니다.",
              "웹툰":"지혜로운 조력자, 든든한 멘토"},
        "금":{"성격":"냉철하고 결단력 있으며 카리스마가 있습니다.",
              "연애":"매력적이지만 차가운 인상을 줄 수 있습니다.",
              "재물":"권위와 명예를 얻으며 재물운도 좋습니다.",
              "현재":"목표를 향해 집중할 수 있는 시기입니다.",
              "미래":"강렬한 인상을 남기며 중요한 위치에 설 수 있습니다.",
              "웹툰":"강력한 라이벌, 카리스마 캐릭터"},
        "수":{"성격":"지혜롭고 신비로우며 직관력이 뛰어납니다.",
              "연애":"상대의 마음을 잘 읽고 이해합니다.",
              "재물":"지혜로운 선택이 재물로 이어집니다.",
              "현재":"직관이 빛나고 새로운 아이디어가 떠오르는 시기입니다.",
              "미래":"지혜와 경험을 바탕으로 특별한 길을 걸어갑니다.",
              "웹툰":"비밀을 간직한 현자, 신비로운 인물"}
    }

    report = element_report[day_element]

    # -------------------- 결과 출력 --------------------
    st.markdown(f"""
    <div class="report">
        <h3>🔮 {name}님의 웹툰형 사주 리포트</h3>
        <p><b>성별:</b> {gender}</p>
        <p><b>생년월일:</b> {birth_date.strftime('%Y-%m-%d')}</p>
        <p><b>출생시각:</b> {birth_time.strftime('%H:%M')}</p>
        <hr>
        <p><b>사주팔자:</b><br>
           {year_stem}{year_branch} / {month_stem}{month_branch} / {day_stem}{day_branch} / {hour_stem}{hour_branch}
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
