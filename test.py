import streamlit as st
import random
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="현실적 미래 자아 리포트", page_icon="📜", layout="centered")

# 배경과 버튼 스타일
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #1c1c1c, #2e2e2e, #3f3f3f);
        color: #ffffff;
    }
    div.stButton > button:first-child {
        background-color: #ff6f00;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        box-shadow: 2px 2px 8px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📜 현실적 미래 자아 리포트")
st.markdown(
    "이름과 생년월일을 입력하면, 10년 후 / 20년 후 / 30년 후 당신의 현실적이고 다양한 미래를 예측합니다."
)

# 입력
name = st.text_input("이름을 입력하세요")
birth = st.date_input("생년월일을 입력하세요", min_value=datetime(1950,1,1), max_value=datetime.today())

if st.button("🔮 리포트 생성"):
    if name.strip() == "":
        st.warning("이름을 입력하세요!")
    else:
        # 현실적 직업 예시
        careers = [
            "편의점 알바", "프리랜서 디자이너", "회사원", "교사", "택배 기사",
            "요리사", "프로그래머", "작가", "배달 라이더", "전업주부",
            "학생", "대학원생", "사회복지사", "공무원", "아르바이트생",
            "카페 바리스타", "사진작가", "음악 강사", "헬스 트레이너", "정비사",
            "온라인 마케터", "유튜버", "블로거", "소규모 사업자", "봉사 활동가",
            "패션 디자이너", "게임 개발자", "연구원", "환경 운동가", "택시 기사"
        ]

        # 현실적 업적 예시
        achievements = [
            "그럭저럭 생계를 이어갑니다.",
            "월세를 내며 살아갑니다.",
            "좋은 친구를 많이 사귀었습니다.",
            "건강하게 하루하루를 보냅니다.",
            "소소한 취미생활을 즐깁니다.",
            "일을 바꿔 새로운 경험을 쌓습니다.",
            "적은 돈으로 여행을 다닙니다.",
            "집을 마련하기 위해 노력합니다.",
            "가끔 힘든 일이 생기지만 극복합니다.",
            "작은 성취를 쌓아갑니다.",
            "직장을 잃고 잠시 방황합니다.",
            "투자 실패로 돈이 줄었습니다.",
            "새로운 도전을 시도합니다.",
            "동네 카페에서 알바를 시작합니다.",
            "프리랜서로 살아가며 경험을 쌓습니다.",
            "자격증 공부를 시작합니다.",
            "온라인 수업을 통해 새로운 기술을 배웁니다.",
            "작은 가게를 운영하며 생활합니다.",
            "동호회 활동으로 친구를 만듭니다.",
            "가족과 함께 시간을 보냅니다."
        ]

        # 현실적 장소 예시
        places = [
            "서울", "부산", "대전", "대구", "광주", "동네 카페", "집", "직장 근처", 
            "근교", "학교", "도서관", "공원", "헬스장", "친구 집", "온라인",
            "작은 마을", "해외 여행지", "버스/지하철", "공공기관", "시장"
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

        # 리포트 제목
        st.markdown(
            f"<h2 style='color:#ffd700; text-shadow:2px 2px 5px #000000;'>{name}님의 현실적 미래 리포트</h2>", 
            unsafe_allow_html=True
        )

        # 결과 카드 스타일
        report_list = [
            f"**10년 후:** {place1} | 직업: {job1} | 상황: {ach1}",
            f"**20년 후:** {place2} | 직업: {job2} | 상황: {ach2}",
            f"**30년 후:** {place3} | 직업: {job3} | 상황: {ach3}"
        ]

        for report in report_list:
            st.markdown(
                f"""
                <div style='background: rgba(255,255,255,0.05); 
                            padding:18px; 
                            border-radius:12px; 
                            margin-bottom:12px; 
                            box-shadow: 0 0 15px rgba(0,0,0,0.5);'>
                    <p style='font-size:18px; text-shadow:1px 1px 2px #000000;'>{report}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")
        st.info("※ 본 리포트는 현실적 상황을 기반으로 한 시뮬레이션이며 실제 미래와 다를 수 있습니다.")
