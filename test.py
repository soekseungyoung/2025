import streamlit as st
import random
import base64

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="📘", layout="centered")

st.title("📘 내가 웹툰 속에 들어간다면?")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다!")

# 이미지 4장 업로드 받기
uploaded_imgs = []
for i in range(1,5):
    uploaded_img = st.file_uploader(f"배경 이미지 {i} 업로드 (선택)", type=["png", "jpg", "jpeg"], key=f"img{i}")
    uploaded_imgs.append(uploaded_img)

def get_base64(file):
    if file is None:
        return None
    return base64.b64encode(file.read()).decode()

# 업로드된 이미지가 모두 있으면 base64로 변환
base64_imgs = []
if all(uploaded_imgs):
    for img in uploaded_imgs:
        base64_imgs.append(get_base64(img))

    # CSS에 이미지 넣기
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-color: #ffd1dc;  /* 연한 핑크 배경 */
        background-image:
            url("data:image/png;base64,{base64_imgs[0]}"),
            url("data:image/png;base64,{base64_imgs[1]}"),
            url("data:image/png;base64,{base64_imgs[2]}"),
            url("data:image/png;base64,{base64_imgs[3]}");
        background-repeat: no-repeat, no-repeat, no-repeat, no-repeat;
        background-position: left top, right top, left bottom, right bottom;
        background-size: 150px 200px, 150px 200px, 150px 200px, 150px 200px;
        opacity: 0.15;
        background-blend-mode: lighten;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
else:
    st.info("배경 이미지 4장을 모두 업로드 해주세요. (선택시 배경 이미지가 표시됩니다)")

# 이름 입력 및 캐릭터 생성
name = st.text_input("당신의 이름을 입력하세요:")

def generate_character(name):
    height = random.randint(150, 190)
    roles = [
        "다정한 공", "차가운 공", "능글맞은 공", "츤데레 공",
        "순진한 수", "새침한 수", "털털한 수", "상처 많은 수"
    ]
    role = random.choice(roles)

    appearances = [
        "짧은 흑발에 강한 인상", "긴 생머리에 차가운 눈매", "은은한 미소를 가진 얼굴",
        "눈이 크고 인형 같은 외모", "스포티한 스타일에 건강미 넘침",
        "항상 후드를 쓰고 다니는 미스터리한 모습"
    ]
    appearance = random.choice(appearances)

    personalities = [
        "겉은 차가워 보이지만 속은 따뜻한 스타일",
        "모든 사람에게 친절한 인싸",
        "혼자 있는 걸 좋아하는 무뚝뚝한 타입",
        "정의감 넘치고 다혈질",
        "감성적이고 눈물이 많은 성격",
        "장난기 많고 유쾌한 분위기 메이커"
    ]
    personality = random.choice(personalities)

    result = (f"{name}님의 웹툰 캐릭터는 키 {height}cm에 '{role}' 포지션이며, "
              f"외형은 {appearance}, 성격은 {personality}입니다.")
    return result

if name:
    st.write(generate_character(name))

    if st.button("다시 하기"):
        st.experimental_rerun()
