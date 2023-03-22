# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
from PIL import Image

def main():
    """코드 작성"""
    st.title("Hello world")

    st.text('This is {}'.format('good, Happy day!~'))

    """ 기능들 입력 및 소개 """
    st.header('This is header')

    st.subheader('Thins is subheader')

    st.markdown('## This is Markdown Header')

    # colored text
    st.success('성공! 굿~!! Streamlit! ')   
    st.warning('위험') 
    st.info('This is information')
    st.error('This is an error')
    st.exception('This is an exception')
    
    # super function
    st.write(1+1) 
    st.write(type("normal"))
    st.write(type(3))

    a=1
    b=2
    st.write(a+b)
    st.write(dir(str))
    st.help(range) 

    iris = pd.read_csv("data/iris.csv")
    # st.dataframe(iris)
    st.dataframe(iris,200,100)

    # 색상 추가
    st.title('Addinf color on table')
    st.dataframe(iris.style.highlight_max(axis=0))  # 스크롤바있음

    # static table : 정적인 데이터 테이블 # 스크롤바 없음
    # st.table(iris.head())
    st.table(iris.head(30))

    #st.write : 스크롤바 있음
    st.write(iris)

    # 나의 코드를 보여줘
    myCode = """
    def hello():
        print("Hello world!)
    """
    st.code(myCode, language = 'Python')

    # widget, 버튼, 체크박스 사용
    name = "Chloey"
    if st.button('Submit'):
      st.write(f'name : {name.upper()}')

    if st.button('Submit', key = 'name02'):
         st.write(f'name : {name.lower()}')

    #ratio button
    status = st.radio("Status", ("활성화", "비활성화"))
    st.write(status)
    if status == "활성화":
        st.success("활성화 상태")
    elif status == "비활성화":
        st.info("비활성화 상태")
    else:
        pass

    # check Box
    if st.checkbox('Show/Hide'):
        st.text('보여줘')

        










if __name__ =="__main__":
        main()
        