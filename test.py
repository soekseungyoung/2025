import streamlit as st
import random

# 배경 이미지 4장 경로 (로컬 파일을 base64로 인코딩하거나 웹에 업로드해서 URL로 대체)
# 여기서는 이미지 파일을 base64 인코딩해서 CSS에 넣는 예시입니다.

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    import base64
    return base64.b64encode(data).decode()

img1 = get_base64_of_bin_file("/mnt/data/43d95ac7f42847d5b91fcbd4f39c889c.png")
img2 = get_base64_of_bin_file("/mnt/data/cbc22f0b73224ffa93a6b79adc4ae1a5.png")
img3 = get_base64_of_bin_file("/mnt/data/96c7810b83384063ba21899e5bcd32ab.png")
img4 = get_base64_of_bin_file("/mnt/data/ff3f1811f4e1419eb905df876e236b89.png")

st.set_page_config(page_title="내가 웹툰 속에 들어간다면?", page_icon="📘", layout="centered")

# 배경 스타일 적용
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background: linear-gradient(rgba(255,182,193,0.3), rgba(255,182,193,0.3)), url("data:image/png;base64,{img1}"), url("data:image/png;base64,{img2}"), url("data:image/png;base64,{img3}"), url("data:image/png;base64,{img4}");
    background-repeat: no-repeat, no-repeat, no-repeat, no-repeat, no-repeat;
    background-position: center top, left bottom, right bottom, left top, right top;
    background-size: 200px 300px, 200px 300px, 200px 300px, 200px 300px, 200px 300px;
    filter: brightness(0.8);
    background-blend-mode: lighten;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("📘 내가 웹툰 속에 들어간다면?")
st.markdown("이름을 입력하면 웹툰 속 당신의 모습을 알려드립니다!")

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
