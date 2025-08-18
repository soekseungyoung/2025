import streamlit as st
import random
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="웅장한 미래 자아 리포트", page_icon="🌌", layout="centered")

# 배경 그라데이션 및 버튼 스타일
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #0f2027, #203a43, #2c5364);
        color: #ffffff;
    }
    div.stButton > button:first-child {
        background-color: #ff4500;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        box-shadow: 2px 2px 10px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌌 웅장한 미래 자아 리포트")
st.markdown(
    "당신의 이름과 생년월일을 입력하면, 다른 차원의 웅장한 미래 삶을 예측합니다.\n"
    "10년, 20년, 30년 후의 서사적 인생 리포트를 확인하세요."
)

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

        # 업그레이드된 웅장한 achievements
        achievements = [
            "은하 연방 최초의 자율 항성 항로를 개척했습니다.",
            "수천만 인류가 경험할 가상 문명을 설계하고 완성했습니다.",
            "인류 최초의 다차원 탐사 기록을 남겼습니다.",
            "차원 간 문명 교류를 성공적으로 이끌었습니다.",
            "우주 탐사 역사에 기록될 발견을 완성했습니다.",
            "심우주 거주지의 문명 구축을 주도했습니다.",
            "미래 사회의 핵심 기술을 혁신했습니다.",
            "인류의 삶과 문명을 바꾼 획기적인 연구를 완수했습니다.",
            "후세에 길이 남을 위대한 예술 작품을 창조했습니다.",
            "국제 무대에서 인류 평화와 협력을 증진시켰습니다.",
            "지구 환경 회복 프로젝트를 성공적으로 완수했습니다.",
            "디지털 세계와 현실 세계를 연결하는 혁신적 시스템을 구축했습니다.",
            "우주 생명체 탐사에 기여하며 새로운 생태계를 발견했습니다.",
            "차세대 AI 윤리 기준을 정립하며 사회적 영향력을 발휘했습니다."
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

        # 웅장한 리포트 제목
        st.markdown(
            f"<h2 style='color:#ffd700; text-shadow:2px 2px 8px #000000;'>{name}님의 웅장한 미래 리포트</h2>", 
            unsafe_allow_html=True
        )

        # 결과 카드 스타일
        report_list = [
            f"**10년 후:** {place1}에서 {job1}로 활동하며, {ach1}",
            f"**20년 후:** {place2}에서 {job2}로 성장하며, {ach2}",
            f"**30년 후:** {place3}에서 {job3}로 인생을 정리하며, {ach3}"
        ]

        for report in report_list:
            st.markdown(
                f"""
                <div style='background: rgba(255,255,255,0.05); 
                            padding:20px; 
                            border-radius:15px; 
                            margin-bottom:15px; 
                            box-shadow: 0 0 20px rgba(0,0,0,0.5);'>
                    <p style='font-size:18px; text-shadow:1px 1px 3px #000000;'>{report}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")
        st.info("※ 본 리포트는 상상력을 기반으로 한 시뮬레이션이며 실제 미래와는 다를 수 있습니다.")
