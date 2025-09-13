import streamlit as st
import random

# --------------------
# 데이터: MBTI별 책 추천
# --------------------
book_recommendations = {
    "INTJ": [
        ("니코마코스 윤리학", "아리스토텔레스"),
        ("총, 균, 쇠", "재레드 다이아몬드"),
        ("사피엔스", "유발 하라리"),
    ],
    "ENTP": [
        ("돈키호테", "세르반테스"),
        ("넛셸", "이언 매큐언"),
        ("원더", "R.J. 팔라시오"),
    ],
    "INFJ": [
        ("데미안", "헤르만 헤세"),
        ("연금술사", "파울로 코엘료"),
        ("작은 것들의 신", "아룬다티 로이"),
    ],
    "ENFP": [
        ("오만과 편견", "제인 오스틴"),
        ("모모", "미하엘 엔데"),
        ("지구 끝의 온실", "김초엽"),
    ],
    # 다른 유형들도 다양하게 추가
    "ISTJ": [
        ("군주론", "마키아벨리"),
        ("자유론", "존 스튜어트 밀"),
        ("팩트풀니스", "한스 로슬링"),
    ],
    "ISFP": [
        ("월든", "헨리 데이비드 소로"),
        ("채식주의자", "한강"),
        ("파친코", "이민진"),
    ],
    "ENTJ": [
        ("손자병법", "손자"),
        ("제국", "닐 퍼거슨"),
        ("넛셸", "이언 매큐언"),
    ],
    "INFP": [
        ("어린 왕자", "생텍쥐페리"),
        ("종이 여자", "기욤 뮈소"),
        ("보건교사 안은영", "정세랑"),
    ],
}

# --------------------
# Streamlit UI
# --------------------

st.set_page_config(page_title="MBTI 📖 Book Recommender", page_icon="📚", layout="centered")

st.title("✨ MBTI로 보는 인생 책 추천 ✨")
st.markdown("#### 당신의 MBTI를 선택하면, 딱 어울리는 책을 추천해드려요! 🚀")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 골라주세요 😎", options=sorted(book_recommendations.keys()))

if mbti:
    st.markdown(f"### 당신은 **{mbti}** 타입이군요! 🌟")

    # 랜덤으로 책 하나 추천
    book, author = random.choice(book_recommendations[mbti])

    st.success(f"{mbti} 타입에게 어울리는 책은... 🎉")

    st.markdown(
        f"## 📖 *{book}*  \\\n        ✍️ {author}  \\\n        👉 지금 바로 읽어보세요! 🚀✨"
    )

    # 재미있는 효과 (풍선, 눈뽕)
    st.balloons()

    if st.button("✨ 다른 책도 추천받기 ✨"):
        book, author = random.choice(book_recommendations[mbti])
        st.info(f"이번에는 📖 *{book}* (✍️ {author}) 어때요? 😍")
