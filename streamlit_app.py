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