import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("MBTI 유형별 비율이 가장 높은 국가 Top10")

# 기본 파일 경로
default_file = "countriesMBTI_16types.csv"

# 파일 불러오기 시도
df = None
if os.path.exists(default_file):
    st.success(f"기본 파일을 불러왔습니다: {default_file}")
    df = pd.read_csv(default_file)
else:
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

if df is not None:
    # MBTI 타입 리스트
    mbti_types = ["ISTJ","ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP",
                  "ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]

    # 국가별 합계 계산
    df["Total"] = df[mbti_types].sum(axis=1)

    # 국가별 MBTI 비율 계산
    for t in mbti_types:
        df[f"{t}_ratio"] = df[t] / df["Total"]

    # 선택 박스: MBTI 유형 선택
    selected_type = st.selectbox("MBTI 유형 선택", mbti_types)

    # 선택한 유형의 비율 기준 Top10 국가 추출
    top10 = df[["Country", f"{selected_type}_ratio"]].sort_values(
        by=f"{selected_type}_ratio", ascending=False
    ).head(10)

    # Altair 차트
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(f"{selected_type}_ratio:Q", title="비율"),
            y=alt.Y("Country:N", sort="-x"),
            tooltip=["Country", f"{selected_type}_ratio"]
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    # 데이터 표도 함께 표시
    st.dataframe(top10.reset_index(drop=True))
else:
    st.warning("기본 파일이 없으면 CSV를 업로드해주세요.")
