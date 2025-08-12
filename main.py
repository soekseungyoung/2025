import streamlit as st
import time
import random
import datetime

# 확장된 사주 기반 직업 추천 함수
def get_saju_recommendations(birth_date, birth_time):
    year = int(birth_date.split('-')[0])
    month = int(birth_date.split('-')[1])
    day = int(birth_date.split('-')[2])
    hour = int(birth_time.split(':')[0])

    # 더 정교한 오행 판정: 년도 천간/지지 포함 계산
    heavenly_stems = ["갑", "을", "병", "정", "무", "기", "경", "신", "임", "계"]
    earthly_branches = ["자", "축", "인", "묘", "진", "사", "오", "미", "신", "유", "술", "해"]
    stem = heavenly_stems[(year - 4) % 10]
    branch = earthly_branches[(year - 4) % 12]

    element_map = {
        "갑": "목(木)", "을": "목(木)",
        "병": "화(火)", "정": "화(火)",
        "무": "토(土)", "기": "토(土)",
        "경": "금(金)", "신": "금(金)",
        "임": "수(水)", "계": "수(水)"
    }
    element = element_map[stem]

    strengths = {
        "목(木)": ["성장 지향", "창의성과 직관", "계획성과 조직력", "변화를 이끄는 힘"],
        "화(火)": ["뜨거운 열정", "도전 정신", "리더십과 카리스마", "강력한 추진력"],
        "토(土)": ["안정과 신뢰", "체계적 분석", "인내와 성실함", "현실적인 문제 해결"],
        "금(金)": ["정확한 분석력", "결단력과 추진력", "전략적 사고", "규율과 질서"],
        "수(水)": ["유연성과 적응력", "소통과 협력", "감정이입과 배려", "창의적 발상"],
    }

    jobs = {
        "목(木)": ["교사", "작가", "도시 계획가", "정원 디자이너"],
        "화(火)": ["기업가", "운동선수", "군 장교", "영업 관리자"],
        "토(土)": ["회계사", "부동산 전문가", "행정가", "데이터 매니저"],
        "금(金)": ["변호사", "데이터 분석가", "전략 컨설턴트", "재무 설계사"],
        "수(水)": ["심리상담가", "외교관", "여행 기획자", "마케팅 전문가"],
    }

    return f"{stem}{branch}년 ({element})", strengths[element], jobs[element]

# 페이지 제목
st.markdown(
    """
    <h1 style='text-align:center; color:gold; font-size:48px;'>⚜️ 사주 기반 적성 & 직업 추천 ⚜️</h1>
    """,
    unsafe_allow_html=True
)

st.write("<div style='text-align:center; font-size:18px;'>생년월일과 태어난 시간을 입력하면, 사주를 기반으로 당신의 숨겨진 적성과 직업을 알려드립니다.</div>", unsafe_allow_html=True)

# 입력 받기 (년도 제한 2000~2025)
min_date = datetime.date(2000, 1, 1)
max_date = datetime.date(2025, 12, 31)
birth_date = st.date_input("📅 생년월일 입력", min_value=min_date, max_value=max_date)
birth_time = st.time_input("⏰ 태어난 시간 입력")

# 추천 받기 버튼
if st.button("🔮 근엄하게 추천 받기"):
    with st.spinner("천문과 지리를 읽고 있습니다...🌌"):
        time.sleep(2)
    element, strengths, jobs = get_saju_recommendations(str(birth_date), str(birth_time))
    st.markdown(f"<h2 style='color:gold;'>🏯 당신의 사주: {element}</h2>", unsafe_allow_html=True)
    st.markdown("### 📜 강점")
    for s in strengths:
        st.write(f"- {s}")
    st.markdown("### 🏆 추천 직업")
    for j in jobs:
        st.write(f"- {j}")

    # 웅장한 효과
    if random.choice([True, False]):
        st.balloons()
    else:
        st.snow()

    st.success("운명을 따라, 당신의 길을 걸으십시오! ⚔️")

st.write("---")
st.caption("Made with 🏮 using Streamlit")
