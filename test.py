import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="미래 자아 리포트", page_icon="📜", layout="centered")

st.title("📜 미래 자아 리포트")
st.markdown("당신의 이름과 생년월일을 입력하면, 10년 후 / 20년 후 / 30년 후의 삶을 예측합니다.")

# 입력
name = st.text_input("이름을 입력하세요")
birth = st.date_input("생년월일을 입력하세요", min_value=datetime(1950,1,1), max_value=datetime.today())

if st.button("🔮 리포트 생성"):
    if name.strip() == "":
        st.warning("이름을 입력하세요!")
    else:
        # 직업/삶 시나리오 데이터 풀
        careers = [
    # 비즈니스/경제
    "광고 마케터", "브랜드 매니저", "기업가", "스타트업 창업가", "국제 무역가",
    "투자 분석가", "경영 컨설턴트", "재무 설계사", "AI 비즈니스 전략가",
    
    # 과학/기술
    "과학자", "연구자", "데이터 사이언티스트", "AI 엔지니어", "로봇공학자",
    "양자 물리학자", "바이오테크 전문가", "환경 과학자", "우주 항공 엔지니어",
    
    # 인문/사회
    "작가", "철학자", "역사가", "언론인", "사회학자",
    "정치가", "국제 외교관", "법조인", "사회운동가",
    
    # 예술/문화
    "예술가", "화가", "영화 감독", "건축가", "디자이너",
    "음악가", "무용가", "패션 디렉터", "게임 크리에이터",
    
    # 교육/연구
    "교수", "교육가", "멘토", "연구원", "국제 강연가",
    
    # 미래/신직업
    "메타버스 건축가", "우주 여행 가이드", "디지털 아티스트",
    "가상현실 치료사", "사이버 보안 전문가", "기후 위기 해결사",
    "생명 연장 연구자", "인공지능 윤리 전문가", "우주 개척자"
]

        ]
        achievements = [
            "새로운 브랜드 론칭을 주도했습니다.",
            "혁신적인 프로젝트로 세상의 주목을 받았습니다.",
            "국제 무대에서 명성을 얻었습니다.",
            "후학을 양성하며 지혜를 나누었습니다.",
            "세계적인 상을 수상했습니다.",
            "사람들의 삶에 깊은 영향을 남겼습니다."
        ]
        places = [
            "서울", "뉴욕", "파리", "베를린", "도쿄", "상하이", "런던", "실리콘밸리"
        ]

        # 랜덤 선택
        job1 = random.choice(careers)
        job2 = random.choice(careers)
        job3 = random.choice(careers)

        ach1 = random.choice(achievements)
        ach2 = random.choice(achievements)
        ach3 = random.choice(achievements)

        place1 = random.choice(places)
        place2 = random.choice(places)
        place3 = random.choice(places)

        # 출력
        st.subheader(f"✨ {name}님의 미래 리포트")
        st.write(f"**10년 후:** {place1}에서 {job1}로 활동하며, {ach1}")
        st.write(f"**20년 후:** {place2}에서 {job2}로 성장하며, {ach2}")
        st.write(f"**30년 후:** {place3}에서 {job3}로 인생을 정리하며, {ach3}")
        st.markdown("---")
        st.info("※ 본 리포트는 오락용으로 제작되었으며 실제 미래와는 다를 수 있습니다.")
