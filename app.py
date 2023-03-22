# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
from PIL import Image
import datetime


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
        st.success("활성화 상태!")
    elif status == "비활성화":
        st.info("비활성화 상태")
    else:
        pass   

    # check Box
    if st.checkbox('Show/Hide'):
        st.text('보여진다')

    # calendar : 달력 표시
    d = st.date_input(
        "When\'s your birthday",
        datetime.date(2023, 3, 6))
    st.write('Your birthday is:', d)

    # selectbox
    programings = ['Python', 'Java', 'HTML', 'CSS', 'JS']
    choice = st.selectbox('프로그래밍 언어: ', programings)
    st.write(f'{choice} 언어를 선택함')

    # multiple selection
    spoken_lang =("영어", "일본어", "중국어", "독일어")   
    mylangchoice = st.multiselect("언어선택", spoken_lang, default ="영어")
    st.write("선택:", mylangchoice)

    # options 창 
    options = st.multiselect(
        'What are your favoirate colors',
        ['Viloet', 'Margetna', 'Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])
    st.write('You seleted:', options)

     
    # https://docs.streamlit.io/library/api-reference/widgets/st.multiselect


    # Slider
    age = st.slider('나이',1,120)
    st.write(age)

    """ 
    color = st.select_slider('색상 선택:',
                            options=['노란색', '빨건색', '녹색', '파란색'],
                            value = ("노란색", "녹색"))

    st.write(color)
     
    """


    start_color, end_color = st.select_slider('색상 선택:',
                             options=['노란색', '빨간색', '녹색', '파란색'],
                             value = ("노란색", "녹색"))
    st.write(start_color, end_color)

    # 멀티미디어
    # image
    image = Image.open('data/tullip.jpg')
    st.image(image, caption='Beautiful Flower')

    image = Image.open('data/flower.jpg')
    st.image(image, caption='Beautiful Flower')

    image = Image.open('data/universe.jpg')
    st.image(image, caption='Universe')

    img_url = 'https://hips.hearstapps.com/hmg-prod/images/types-of-garden-flowers-purple-allium-1674847068.jpeg?crop=1xw:1xh;center,top&resize=980:*'
    st.image(img_url, caption='Pretty flower')
    
    # video file 출력    
    video_file = open('data/secret_of_success.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    # 컨텍스트 매니저 : chatGPT물어보기 : 자원을 사용하고 다시 반납하는 용어 'with'
    with open('data/secret_of_success.mp4', 'rb') as rb:
        video_file = rb.read()
        st.video(video_file, start_time=1)    
    
    st.video('https://www.youtube.com/watch?v=fhdX3Wcxwas')

   
    # 오디오 출력
    '''with open('data/song.mp3', 'rb') as rb:
        audio_file =rb.read()
        st.audio(audio_file, format=audio/mp3)'''
    
    audio_file = open('data/song.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='song/mp3')

    # text 입력
    fname = st.text_input('입력해 주세요')
    st.title(fname)

    message = st.text_area('입력해 주세요!', height=100)
    st.write(message)

    nums= st.number_input('숫자 입력하세요')
    st.write(nums)

    mytime = st.time_input('시간입력')
    st.write(mytime)

    # color Picker
    color = st.color_picker('색상 선택')
    st.write(color)

    # col1, col2 
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.checkbox("Disable selectbox widget", key="disabled")
        st.radio(
            "Set selectbox label visibility 👉",
            key="visibility",
            options=["visible", "hidden", "collapsed"],
    )

    with col2:
        option = st.selectbox(
            "연락 방식을 선택하세요",
            ("Email", "Home phone", "Mobile phone"),
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
    )
        
    with col3:
        st.video('https://www.youtube.com/watch?v=fhdX3Wcxwas')




    # widget
    #st.sidebar.<widget>
    #a = st.sidebar.radio('R:',[1,2])

    # 사이드 바 출력
    add_selectbox = st.sidebar.selectbox("왼쪽 사이드바 Select Box", ("A", "B", "C"))
    

    


        
if __name__ =="__main__":
        main()
        