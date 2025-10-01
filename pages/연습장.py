import streamlit as st

st.title("민경이의 첫 번째 앱🎈")
st.success(" nct wish ")
st.info(" nct wish ")
st.image("https://pbs.twimg.com/media/Gj6D4GIacAECKkK.jpg:large")

# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")

# 페이지 구조용 제목 출력
st.title("레시피 생성기")
st.header("오늘의 레시피 추천입니다.")
st.subheader("맘스터치 싸이버거")

# LaTeX 수식 출력
st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}")

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

# 이미지 출력
st.image("https://static.streamlit.io/examples/cat.jpg", caption="귀여운 고양이", use_container_width=True)
st.image("https://via.placeholder.com/300", caption="예시 이미지")

# 영상 출력
st.video("https://www.youtube.com/watch?v=4nU-Fp96p8E")
st.video("https://www.youtube.com/watch?v=B1J6Ou4q8vE")

# 오디오 출력
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 지도 출력
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=12)

# 데이터프레임 테이블 출력
st.dataframe(pd.DataFrame({
    "이름": ["홍길동", "김철수"],
    "점수": [85, 92]
}))

st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

st.link_button("네이버!!", "https://naver.com")

# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
#
# st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
st.write("안녕")

## 입력
age = st.number_input("나이를 입력해주세요", step=1)
st.write(2025-age)
st.write(f"{2025-age}년에 태어나셨군요!")

# 여러 옵션 중 하나 선택
gender = st.radio("유우시를 좋아합니다", ["네", "아니오"])
if(gender=="아니오"):
    st.write("그러지마라")

# 드롭다운에서 하나 선택
color = st.selectbox("좋아하는 색을 선택하세요", ["빨강", "초록", "파랑"])
st.write("선택한 색상:", color)
if color=="빨강":
    st.error("빨강을 좋아하시는군요!")
elif color=="초록":
    st.success("푸릇푸릇")
# 여러 개 선택
subjects = st.multiselect("관심 있는 과목을 선택하세요", ["수학", "영어", "과학"])
st.write("선택한 과목:", subjects)

# 범위 내 숫자 슬라이드 선택
level = st.slider("난이도를 선택하세요", 1, 10, 5)
st.write("선택한 난이도:", level)

# 날짜 입력
date = st.date_input("날짜를 선택하세요")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("시간을 선택하세요")
st.write("선택한 시간:", time)

# 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)