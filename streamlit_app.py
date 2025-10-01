import streamlit as st
import google.generativeai as genai
import os
import json

# Gemini API 키 설정 (환경 변수 사용 권장)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI 레시피 생성기", page_icon="🧑‍🍳", layout="centered")

st.title("🧑‍🍳 AI 레시피 생성기")
st.write("궁금한 음식 이름을 입력하면 Gemini가 레시피를 만들어 드립니다.")

# 입력창
food_name = st.text_input("음식 이름을 입력하세요", placeholder="예시: 김치찌개, 스테이크, 잡채...")

# 버튼
if st.button("레시피 찾기") and food_name:
    with st.spinner("맛있는 레시피를 생성하는 중입니다..."):
        # JSON 스키마 정의
        recipe_schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "prepTime": {"type": "string"},
                "cookTime": {"type": "string"},
                "ingredients": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "quantity": {"type": "string"},
                        },
                    },
                },
                "instructions": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": ["title", "description", "ingredients", "instructions"],
        }

        # 프롬프트
        prompt = f"""
        당신은 세계 최고의 요리사이자 레시피 전문가입니다. 
        사용자가 요청한 음식에 대해 JSON 형식에 맞게 한국어 레시피를 생성하세요. 
        음식: {food_name}
        """

        # Gemini 모델 불러오기
        model = genai.GenerativeModel(
            "gemini-1.5-flash", 
            generation_config={
                "response_mime_type": "application/json",
                "response_schema": recipe_schema
            }
        )

        try:
            response = model.generate_content(prompt)
            recipe = json.loads(response.text)

            # 출력 카드
            st.subheader(f"🍽️ {recipe['title']}")
            st.write(recipe.get("description", ""))

            # 시간
            col1, col2 = st.columns(2)
            col1.metric("🕒 준비 시간", recipe.get("prepTime", "정보 없음"))
            col2.metric("🔥 조리 시간", recipe.get("cookTime", "정보 없음"))

            # 재료
            st.markdown("### 🥕 재료")
            for ing in recipe.get("ingredients", []):
                st.write(f"- {ing['name']} : {ing['quantity']}")

            # 조리 순서
            st.markdown("### 📝 조리 순서")
            for i, step in enumerate(recipe.get("instructions", []), 1):
                st.write(f"{i}. {step}")

        except Exception as e:
            st.error(f"레시피 생성 중 오류가 발생했습니다: {e}")
