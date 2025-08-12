import streamlit as st

# MBTI별 적성 및 직업 추천 데이터
type_to_info = {
    "INTJ": {
        "strengths": ["전략적 사고", "계획 수립", "분석 능력"],
        "jobs": ["전략 기획자", "데이터 분석가", "연구원"]
    },
    "ENTP": {
        "strengths": ["창의성", "문제 해결 능력", "사람 설득"],
        "jobs": ["창업가", "마케팅 기획자", "광고 크리에이티브 디렉터"]
    },
    "INFJ": {
        "strengths": ["공감 능력", "심층적 사고", "비전 제시"],
        "jobs": ["심리상담가", "작가", "비영리 단체 활동가"]
    },
    "ENFP": {
        "strengths": ["열정", "사람 중심 사고", "아이디어 발산"],
        "jobs": ["홍보 전문가", "방송 PD", "이벤트 기획자"]
    },
    "ISTJ": {
        "strengths": ["성실함", "책임감", "정확성"],
        "jobs": ["회계사", "행정 공무원", "데이터 관리자"]
    },
    "ESTJ": {
        "strengths": ["조직 관리", "결단력", "실행력"],
        "jobs": ["경영 관리자", "프로젝트 매니저", "군 장교"]
    },
    "ISFP": {
        "strengths": ["예술적 감각", "세심함", "적응력"],
        "jobs": ["디자이너", "사진작가", "작곡가"]
    },
    "ESFP": {
        "strengths": ["사교성", "즉흥성", "에너지"],
        "jobs": ["배우", "MC", "여행 가이드"]
    },
    "ISTP": {
        "strengths": ["문제 해결", "위기 대처", "기술 활용"],
        "jobs": ["엔지니어", "정비사", "응급구조사"]
    },
    "ESTP": {
        "strengths": ["도전 정신", "리더십", "상황 판단력"],
        "jobs": ["기업가", "세일즈 전문가", "스포츠 코치"]
    },
    "ISFJ": {
        "strengths": ["헌신", "관심과 배려", "꾸준함"],
        "jobs": ["간호사", "교사", "사회복지사"]
    },
    "ESFJ": {
        "strengths": ["협력", "의사소통", "책임감"],
        "jobs": ["인사 담당자", "영업 관리자", "이벤트 플래너"]
    },
    "INTP": {
        "strengths": ["논리적 분석", "창의적 문제 해결", "독립성"],
        "jobs": ["연구원", "프로그래머", "발명가"]
    },
    "ENTJ": {
        "strengths": ["리더십", "전략적 사고", "목표 달성"],
        "jobs": ["CEO", "전략 컨설턴트", "변호사"]
    },
    "INFP": {
        "strengths": ["이상주의", "창의성", "감수성"],
        "jobs": ["작가", "예술가", "심리상담가"]
    },
    "ENFJ": {
        "strengths": ["리더십", "공감", "사람을 동기부여"],
        "jobs": ["교사", "코치", "HR 전문가"]
    },
}

# 페이지 제목
st.title("MBTI 기반 적성 및 직업 추천 웹앱")

st.write("자신의 MBTI를 선택하면, 해당 성향에 맞는 잘하는 것들과 추천 직업을 알려드립니다.")

# MBTI 선택
mbti_types = list(type_to_info.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 추천 결과 출력
if st.button("추천 받기"):
    st.subheader(f"{selected_mbti} 유형의 잘하는 것 & 추천 직업")
    st.write("### 잘하는 것:")
    for strength in type_to_info[selected_mbti]["strengths"]:
        st.write(f"- {strength}")
    st.write("### 추천 직업:")
    for job in type_to_info[selected_mbti]["jobs"]:
        st.write(f"- {job}")

st.write("---")
st.caption("Made with ❤️ using Streamlit")
