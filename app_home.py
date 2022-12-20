import streamlit as st

def run_home_app() :
    st.subheader('Welcome~~')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('데이터분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지를 예측해 줍니다.')

    img_url = 'https://img.hankyung.com/photo/202203/0ad0cd5a2df34e36cd91fd08dcbb46c2.jpg'
    st.image(img_url)