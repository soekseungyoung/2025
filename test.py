import streamlit as st
import random
from datetime import datetime

# ------------------ 페이지 설정 ------------------
st.set_page_config(page_title="타로 미래 자아 리포트", page_icon="🃏", layout="centered")

# ------------------ 스타일 ------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #0b0c10, #1f2833, #162447);
        color: #ffffff;
    }
    div.stButton > button:first-child {
        background-color: #ffd700;
        color: black;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        box-shadow: 2px 2px 12px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🃏 타로 미래 자아 리포트")
st.markdown(
    "이름과 생년월일을 입력하면, 타로 카드 3장을 통해 과거·현재·미래의 당신을 점쳐드립니다."
)

# ------------------ 입력 ------------------
name = st.text_input("이름을 입력하세요")
birth = st.date_input("생년월일을 입력하세요", min_value=datetime(1950,1,1), max_value=datetime.today())

if st.button("🔮 리포트 생성"):
    if name.strip() == "":
        st.warning("이름을 입력하세요!")
    else:
        # ------------------ 현실적 직업 ------------------
        careers = [
            "편의점 알바", "프리랜서 디자이너", "회사원", "교사", "택배 기사",
            "요리사", "프로그래머", "작가", "배달 라이더", "전업주부",
            "학생", "대학원생", "사회복지사", "공무원", "아르바이트생",
            "카페 바리스타", "사진작가", "음악 강사", "헬스 트레이너", "정비사",
            "온라인 마케터", "유튜버", "블로거", "소규모 사업자", "봉사 활동가",
            "패션 디자이너", "게임 개발자", "연구원", "환경 운동가", "택시 기사"
        ]

        # ------------------ 현실적 업적 / 서사형 ------------------
        achievements = [
            "아르바이트로 근근이 살아가면서도 작은 꿈을 포기하지 않습니다. 가끔 친구들과 술잔을 기울이며 내일을 다짐합니다.",
            "직장에서 작은 성공을 거두지만, 예상치 못한 프로젝트 때문에 고민이 깊어집니다. 그러나 꾸준히 배우며 성장합니다.",
            "자신만의 블로그와 소셜 미디어를 운영하며 팬을 모으고, 소소한 수익을 얻습니다.",
            "집세와 생활비를 내느라 바쁘지만, 주말에는 작은 여행과 취미생활로 삶의 즐거움을 찾습니다.",
            "작은 가게를 운영하며 하루하루를 살아가고, 고객과의 관계 속에서 작은 행복을 발견합니다.",
            "공부와 자격증 준비에 매진하며 미래를 준비하지만, 가끔 지치고 방황하기도 합니다.",
            "프리랜서로 일하며 자유를 즐기지만, 경제적 불안정과 외로움을 동시에 경험합니다.",
            "동호회와 봉사활동으로 사람들과 만나며, 작은 인간관계의 기쁨을 느낍니다.",
            "대학원에서 연구에 몰두하며, 가끔 작은 발견으로 스스로를 뿌듯하게 합니다.",
            "가족과 함께 보내는 시간을 소중히 여기며, 소소하지만 안정적인 삶을 쌓아갑니다."
        ]

        # ------------------ 장소 ------------------
        places = [
            "동네 점집", "오래된 찻집", "조용한 골목길", "집 거실", "도서관 구석", 
            "카페 한켠", "회사 회의실", "시장 골목", "작은 가게", "공원 벤치"
        ]

        # ------------------ 랜덤 선택 ------------------
        job1 = random.choice(careers)
        job2 = random.choice(careers)
        job3 = random.choice(careers)

        ach1 = random.choice(achievements)
        ach2 = random.choice(achievements)
        ach3 = random.choice(achievements)

        place1 = random.choice(places)
        place2 = random.choice(places)
        place3 = random.choice(places)

        # ------------------ 타로 카드 이름 ------------------
        cards = ["과거", "현재", "미래"]

        # ------------------ 리포트 제목 ------------------
        st.markdown(
            f"<h2 style='color:#ffd700; text-shadow:3px 3px 8px #000000;'>{name}님의 타로 점 미래 리포트</h2>", 
            unsafe_allow_html=True
        )

        # ------------------ 결과 카드 ------------------
        reports = [
            f"{place1} | 직업: {job1} | 상황: {ach1}",
            f"{place2} | 직업: {job2} | 상황: {ach2}",
            f"{place3} | 직업: {job3} | 상황: {ach3}"
        ]

        for i in range(3):
            st.markdown(
                f"""
                <div style='background: rgba(0,0,0,0.8); 
                            padding:25px; 
                            border-radius:20px; 
                            margin-bottom:20px; 
                            border: 3px dashed #ffd700;
                            box-shadow: 0 0 40px #ffcc00, 0 0 80px #ff9900 inset;'>
                    <h3 style='text-align:center; color:#ffd700; text-shadow:2px 2px 6px #000000;'>{cards[i]} 카드</h3>
                    <p style='font-size:18px; line-height:1.6; text-shadow:2px 2px 4px #000000;'>{reports[i]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")
        st.info("※ 본 리포트는 현실적 상황과 점괘 느낌을 기반으로 한 시뮬레이션이며 실제 미래와 다를 수 있습니다.")
