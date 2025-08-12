import streamlit as st
import time
import random
import datetime
from collections import Counter

# 천간과 지지 리스트
heavenly_stems = ["갑", "을", "병", "정", "무", "기", "경", "신", "임", "계"]
earthly_branches = ["자", "축", "인", "묘", "진", "사", "오", "미", "신", "유", "술", "해"]

# 천간과 지지에 따른 오행 매핑
element_map = {
    "갑": "목(木)", "을": "목(木)",
    "병": "화(火)", "정": "화(火)",
    "무": "토(土)", "기": "토(土)",
    "경": "금(金)", "신": "금(金)",
    "임": "수(水)", "계": "수(水)",
    "자": "수(水)", "축": "토(土)", "인": "목(木)", "묘": "목(木)", "진": "토(土)",
    "사": "화(火)", "오": "화(火)", "미": "토(土)", "신": "금(金)", "유": "금(金)", "술": "토(土)", "해": "수(水)"
}

# 월 천간 계산 참고 (월간은 보통 년간과 월에 따라 달라짐)
def get_month_stem(year_stem_idx, month):
    # 월간은 년간 천간에 따라 시작점이 다름
    # 년간 천간 인덱스에 따라 월간 첫 천간 위치 지정
    start = {
        0: 2,  # 갑
        1: 4,  # 을
        2: 6,  # 병
        3: 8,  # 정
        4: 0,  # 무
        5: 2,  # 기
        6: 4,  # 경
        7: 6,  # 신
        8: 8,  # 임
        9: 0,  # 계
    }
    idx = (start[year_stem_idx] + month -1) % 10
    return heavenly_stems[idx]

def get_saju_elements(birth_date, birth_time):
    year = int(birth_date.split('-')[0])
    month = int(birth_date.split('-')[1])
    day = int(birth_date.split('-')[2])
    hour = int(birth_time.split(':')[0])

    # 년간, 년지
    year_stem_idx = (year - 4) % 10
    year_branch_idx = (year - 4) % 12
    year_stem = heavenly_stems[year_stem_idx]
    year_branch = earthly_branches[year_branch_idx]

    # 월간, 월지
    month_stem = get_month_stem(year_stem_idx, month)
    month_branch = earthly_branches[(month + 1) % 12]  # 월지는 음력 1월=인부터 시작, 양력 기준 대략

    # 일간, 일지는 계산 복잡, 여기서는 간단히 day로 대체 (정확하지 않음)
    day_stem = heavenly_stems[(day + 1) % 10]
    day_branch = earthly_branches[(day + 1) % 12]

    # 시간은 2시간 단위로 지지 결정
    hour_branch_idx = ((hour + 1) // 2) % 12
    hour_branch = earthly_branches[hour_branch_idx]

    # 시간 간은 보통 시간 지지 기준 첫 간인 병으로 간주 (간단 처리)
    hour_stem = heavenly_stems[(hour_branch_idx * 2) % 10]

    elements = [
        element_map[year_stem], element_map[year_branch],
        element_map[month_stem], element_map[month_branch],
        element_map[day_stem], element_map[day_branch],
        element_map[hour_stem], element_map[hour_branch],
    ]

    # 가장 많이 나온 오행을 대표 오행으로
    counter = Counter(elements)
    main_element = counter.most_common(1)[0][0]

    return main_element, elements

def get_strengths_and_jobs(element):
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

    return strengths.get(element, []), jobs.get(element, [])

# Streamlit 앱 UI
st.markdown(
    "<h1 style='text-align:center; color:gold; font-size:48px;'>⚜️ 정밀 사주 기반 적성 & 직업 추천 ⚜️</h1>",
    unsafe_allow_html=True
)

st.write("<div style='text-align:center; font-size:18px;'>생년월일과 태어난 시간을 입력하면, 사주팔자를 통해 당신의 숨겨진 적성과 직업을 알려드립니다.</div>", unsafe_allow_html=True)

min_date = datetime.date(2000, 1, 1)
max_date = datetime.date(2025, 12, 31)
birth_date = st.date_input("📅 생년월일 입력", min_value=min_date, max_value=max_date)
birth_time = st.time_input("⏰ 태어난 시간 입력")

if st.button("🔮 근엄하게 추천 받기"):
    with st.spinner("천문과 지리를 읽고 있습니다...🌌"):
        time.sleep(2)
    main_element, all_elements = get_saju_elements(str(birth_date), str(birth_time))
    strengths, jobs = get_strengths_and_jobs(main_element)
    st.markdown(f"<h2 style='color:gold;'>🏯 당신의 대표 오행: {main_element}</h2>", unsafe_allow_html=True)
    st.write(f"🪶 상세 오행 구성: {', '.join(all_elements)}")
    st.markdown("### 📜 강점")
    for s in strengths:
        st.write(f"- {s}")
    st.markdown("### 🏆 추천 직업")
    for j in jobs:
        st.write(f"- {j}")

    if random.choice([True, False]):
        st.balloons()
    else:
        st.snow()

    st.success("운명을 따라, 당신의 길을 걸으십시오! ⚔️")
