import streamlit as st
import pandas as pd
import re

def clean_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)

    # 모든 열에 대해 숫자와 마침표로 시작하는 텍스트 제거
    for col in df.columns:
        df[col] = df[col].apply(lambda x: re.sub(r'^\d+\.', '', str(x)))

    return df

st.title("숫자와 점으로 시작하는 텍스트 삭제")

uploaded_file = st.file_uploader("엑셀 파일 업로드", type=["xlsx"])

if uploaded_file is not None:
    df = clean_excel(uploaded_file)
    
    # 다운로드 버튼 추가
    st.download_button(
        label="다운로드",
        data=df.to_excel(index=False, engine='openpyxl'),
        file_name='cleaned_data.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
