import streamlit as st

# MBTI별 직업 추천 데이터
type_to_jobs = {
    "INTJ": ["전략 기획자", "데이터 분석가", "연구원"],
    "ENTP": ["창업가", "마케팅 기획자", "광고 크리에이티브 디렉터"],
    "INFJ": ["심리상담가", "작가", "비영리 단체 활동가"],
    "ENFP": ["홍보 전문가", "방송 PD", "이벤트 기획자"],
    "ISTJ": ["회계사", "행정 공무원", "데이터 관리자"],
    "ESTJ": ["경영 관리자", "프로젝트 매니저", "군 장교"],
    "ISFP": ["디자이너", "사진작가", "작곡가"],
    "ESFP": ["배우", "MC", "여행 가이드"],
    # 필요에 따라 다른 MBTI 유형도 추가
}

# 페이지 제목
st.title("MBTI 기반 적성 및 직업 추천 웹앱")

# 설명
st.write("자신의 MBTI를 선택하면, 해당 성향에 맞는 적성과 직업을 추천해드립니다.")

# MBTI 선택
mbti_types = list(type_to_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 추천 결과 출력
if st.button("추천 받기"):
    st.subheader(f"{selected_mbti} 유형의 적성 & 추천 직업")
    # 적성 설명 (간단 예시)
    st.write(f"**{selected_mbti}** 유형은 자신의 가치관과 목표에 따라 행동하며, 강한 동기부여와 분석력을 지니고 있습니다.")
    st.write("### 추천 직업:")
    for job in type_to_jobs[selected_mbti]:
        st.write(f"- {job}")

# 푸터
st.write("---")
st.caption("Made with ❤️ using Streamlit")

